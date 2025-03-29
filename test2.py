import pygame
import random
import math
import testenemy
from testenemy import TestEnemy

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((800,600))

# Title and icon
pygame.display.set_caption("Monkeys and Watermelons")
icon = pygame.image.load('monkey1.jpg')
pygame.display.set_icon(icon)

# Adding background image
background = pygame.image.load('background.jpeg')
background = pygame.transform.scale(background, (800, 600))

# Load the sprite sheet and scale it
sprite_sheet = pygame.image.load('Soldier-Idle.png')
sprite_sheet = pygame.transform.scale(sprite_sheet, (sprite_sheet.get_width() * 3, sprite_sheet.get_height() * 3))
frame_width = 64 * 3
frame_height = 64 * 3

def extract_single_frame(sheet, frame_width, frame_height, row=0, col=0):
    frame = sheet.subsurface((col * frame_width, row * frame_height, frame_width, frame_height))
    return frame

# Extract the first frame for the player
player_frame = extract_single_frame(sprite_sheet, frame_width, frame_height)

# Define a Player class
class Player:
    def __init__(self, x, y, frame):
        self.x = x
        self.y = y
        self.frame = frame
        self.x_change = 0
        self.y_change = 0

    def update(self):
        # Update position based on current movement changes
        self.x += self.x_change
        self.y += self.y_change

        # Enforce screen boundaries
        if self.x < 0:
            self.x = 0
        elif self.x > 760:
            self.x = 760
        if self.y < 0:
            self.y = 0
        elif self.y > 555:
            self.y = 555

    def draw(self, screen):
        screen.blit(self.frame, (self.x, self.y))

    def get_position(self):
        return (self.x, self.y)

# Create a player instance
player = Player(270, 280, player_frame)

# (The rest of your game code such as enemy, arrow, hit effect, etc. remains unchanged.)

# For example, enemy setup:
enemy1 = pygame.image.load('duck_man_og.png')
enemy1 = pygame.transform.scale(enemy1, (frame_width, frame_height))
enemyx = random.randint(20,700)
enemyy = 100
enemyx_change = 4

def enemy(x, y):
    screen.blit(enemy1, (x, y))

# Arrow setup
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

# Setup for hit effect animation
hit_sprite_sheet = pygame.image.load('duck_man_sprite.png')
hit_sprite_sheet = pygame.transform.scale(hit_sprite_sheet, (hit_sprite_sheet.get_width()*2, hit_sprite_sheet.get_height()*2))
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







screen.fill((222, 200, 180))
screen.blit(background, (0, 0))
    

score = 0
running = True
clock = pygame.time.Clock()
count = 0
while running:
    screen.fill((222, 200, 180))
    screen.blit(background, (0, 0))

    player.update()
    player.draw(screen)


    if (count == 0):
        test = TestEnemy(player, screen)
        count += 1
    test.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key events for player movement and firing arrow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_change = -10
            if event.key == pygame.K_RIGHT:
                player.x_change = 10
            if event.key == pygame.K_UP:
                player.y_change = -10
            if event.key == pygame.K_DOWN:
                player.y_change = 10
            if event.key == pygame.K_SPACE:
                # Set arrow starting position relative to player
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

    # Update player and draw it
    player.update()
    player.draw(screen)
    # Retrieve and optionally use the player's current position:
    # current_position = player.get_position()
    # print("Player position:", current_position)


    
    # Arrow movement
    if arrow_state == "fire":
        fire_arrow(arrowx, arrowy)
        arrowy -= arrowy_change
    if arrowy <= 0:
        arrowy = player.y  # Reset arrow to player's y position
        arrow_state = "ready"

    # Check for collision between arrow and enemy
    if isCollision(enemyx, enemyy, arrowx, arrowy):
        arrow_state = "ready"
        arrowy = player.y
        score += 1
        print("Score:", score)
        hit_effect_active = True
        hit_effect_index = 0
        hit_effect_timer = 0
        pygame.time.set_timer(IMPACT_SOUND_EVENT, 360)

    # Update enemy position
    enemyx += enemyx_change
    if enemyx <= 0:
        enemyx_change = 4
    elif enemyx >= 600:
        enemyx_change = -4

    # Hit effect drawing (if active)
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
    clock.tick(10)

pygame.quit()






