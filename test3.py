# ====================== IMPORTS ======================
import pygame
import random
import math
import testenemy
from testenemy import TestEnemy  # Importing the class for our enemy

# ====================== INITIAL SETUP ======================
pygame.init()
screen = pygame.display.set_mode((800, 600))

# ====================== ASSETS ======================
# --- Background ---
background = pygame.image.load('background.jpeg')
background = pygame.transform.scale(background, (800, 600))

# --- Sprite Sheet for Player ---
sprite_sheet = pygame.image.load('Soldier-Idle.png')
sprite_sheet = pygame.transform.scale(sprite_sheet, (sprite_sheet.get_width() * 3, sprite_sheet.get_height() * 3))
frame_width = 64 * 3
frame_height = 64 * 3

# ====================== UTILITY FUNCTIONS ======================
def extract_single_frame(sheet, frame_width, frame_height, row=0, col=0):
    frame = sheet.subsurface((col * frame_width, row * frame_height, frame_width, frame_height))
    return frame

# ====================== PLAYER SETUP ======================
player_frame = extract_single_frame(sprite_sheet, frame_width, frame_height)

class Player:
    def __init__(self, x, y, frame):
        self.x = x
        self.y = y
        self.frame = frame
        self.x_change = 0
        self.y_change = 0

    def update(self):
        self.x += self.x_change
        self.y += self.y_change

        # Screen boundaries
        self.x = max(0, min(self.x, 760))
        self.y = max(0, min(self.y, 555))

    def draw(self, screen):
        screen.blit(self.frame, (self.x, self.y))

    def get_position(self):
        return (self.x, self.y)

player = Player(270, 280, player_frame)

# ====================== ENEMY SETUP ======================
enemy1 = pygame.image.load('duck_man_og.png')
enemy1 = pygame.transform.scale(enemy1, (frame_width, frame_height))
enemyx = random.randint(20, 700)
enemyy = 100
enemyx_change = 4

def enemy(x, y):
    screen.blit(enemy1, (x, y))

# ====================== ARROW SETUP ======================
arrow = pygame.image.load('arrow.png')
arrow = pygame.transform.scale(arrow, (arrow.get_width() * 2, arrow.get_height() * 2))
arrow = pygame.transform.rotate(arrow, 90)

arrowx = 0
arrowy = 280
arrowx_change = 0
arrowy_change = 20
arrow_state = "ready"

arrow_sound = pygame.mixer.Sound('arrow_swish.mp3')
impact_sound = pygame.mixer.Sound('arrow_impact.mp3')

def fire_arrow(x, y):
    global arrow_state
    arrow_state = "fire"
    screen.blit(arrow, (x, y))

def isCollision(enemyx, enemyy, arrowx, arrowy):
    distance = math.sqrt((enemyx - arrowx) ** 2 + (enemyy - arrowy) ** 2)
    return distance < 97

# ====================== HIT EFFECT SETUP ======================
hit_sprite_sheet = pygame.image.load('duck_man_sprite.png')
hit_sprite_sheet = pygame.transform.scale(hit_sprite_sheet, (hit_sprite_sheet.get_width() * 2, hit_sprite_sheet.get_height() * 2))
hit_frame_width = 200
hit_frame_height = 200

def extract_hit_frames(sheet, frame_width, frame_height):
    frames = []
    for row in range(sheet.get_height() // frame_height):
        for col in range(sheet.get_width() // frame_width):
            frame = sheet.subsurface((col * frame_width, row * frame_height, frame_width, frame_height))
            frames.append(frame)
    return frames

hit_frames = extract_hit_frames(hit_sprite_sheet, hit_frame_width, hit_frame_height)
hit_effect_active = False
hit_effect_index = 0
hit_effect_timer = 0
hit_effect_duration = 5

IMPACT_SOUND_EVENT = pygame.USEREVENT + 1

# ====================== GAME LOOP ======================
score = 0
running = True
clock = pygame.time.Clock()
count = 0

while running:
    screen.fill((222, 200, 180))
    screen.blit(background, (0, 0))

    # --- Player Updates ---
    player.update()
    player.draw(screen)

    # --- Initialize Threaded Enemy ---
    if count == 0:
        test = TestEnemy(player, screen)
        count += 1
    test.draw(screen)

    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement and Arrow Firing
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_change = -4
            if event.key == pygame.K_RIGHT:
                player.x_change = 4
            if event.key == pygame.K_UP:
                player.y_change = -4
            if event.key == pygame.K_DOWN:
                player.y_change = 4
            if event.key == pygame.K_SPACE:
                arrowx = player.x + 100
                arrowy = player.y + 100
                arrow_state = "fire"
                arrow_sound.play()

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.x_change = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player.y_change = 0

        if event.type == IMPACT_SOUND_EVENT:
            impact_sound.play()
            pygame.time.set_timer(IMPACT_SOUND_EVENT, 0)

    # --- Arrow Movement ---
    if arrow_state == "fire":
        fire_arrow(arrowx, arrowy)
        arrowy -= arrowy_change

    if arrowy <= 0:
        arrowy = player.y
        arrow_state = "ready"

    # --- Collision Detection ---
    if isCollision(enemyx, enemyy, arrowx, arrowy):
        arrow_state = "ready"
        arrowy = player.y
        score += 1
        print("Score:", score)
        hit_effect_active = True
        hit_effect_index = 0
        hit_effect_timer = 0
        pygame.time.set_timer(IMPACT_SOUND_EVENT, 360)

    # --- Enemy Movement ---
    enemyx += enemyx_change
    if enemyx <= 0:
        enemyx_change = 4
    elif enemyx >= 600:
        enemyx_change = -4

    # --- Hit Animation ---
    if hit_effect_active:
        screen.blit(hit_frames[hit_effect_index], (enemyx, enemyy))
        hit_effect_timer += 1
        if hit_effect_timer >= hit_effect_duration:
            hit_effect_timer = 0
            hit_effect_index += 1
            if hit_effect_index >= len(hit_frames):
                hit_effect_active = False
    else:
        enemy(enemyx, enemyy)

    pygame.display.update()
    clock.tick(40)

pygame.quit()
