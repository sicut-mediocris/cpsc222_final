import pygame
import random
from player import Player
from utils import extract_single_frame, extract_hit_frames, isCollision
from assets import load_assets
from testenemy import TestEnemy
#from testenemy1 import TestEnemy
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load everything
assets = load_assets()
player_frame = extract_single_frame(assets["sprite_sheet"], assets["frame_width"], assets["frame_height"])
player = Player(270, 280, player_frame)

enemyx = random.randint(20, 700)
enemyy = 100
enemyx_change = 4

arrowx = 0
arrowy = 280
arrowy_change = 20
arrow_state = "ready"

hit_frames = extract_hit_frames(assets["hit_sprite_sheet"], assets["hit_frame_width"], assets["hit_frame_height"])
hit_effect_active = False
hit_effect_index = 0
hit_effect_timer = 0
hit_effect_duration = 5

score = 0
running = True
IMPACT_SOUND_EVENT = pygame.USEREVENT + 1

test_enemy_initialized = False

while running:
    screen.fill((222, 200, 180))
    screen.blit(assets["background"], (0, 0))

    if not test_enemy_initialized:
        test = TestEnemy(player, screen)
        test_enemy_initialized = True
    test.draw(screen)

    player.update()
    player.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_change = -4
            if event.key == pygame.K_RIGHT:
                player.x_change = 4
            if event.key == pygame.K_UP:
                player.y_change = -4
            if event.key == pygame.K_DOWN:
                player.y_change = 4
            if event.key == pygame.K_SPACE and arrow_state == "ready":
                arrowx = player.hitBox.x
                arrowy = player.hitBox.y
                arrow_state = "fire"
                assets["arrow_sound"].play()

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.x_change = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player.y_change = 0

        if event.type == IMPACT_SOUND_EVENT:
            assets["impact_sound"].play()
            pygame.time.set_timer(IMPACT_SOUND_EVENT, 0)

    # Arrow logic
    if arrow_state == "fire":
        screen.blit(assets["arrow"], (arrowx, arrowy))
        arrowy -= arrowy_change
        if arrowy <= 0:
            arrow_state = "ready"

    # Collision
    if isCollision(enemyx, enemyy, arrowx, arrowy):
        arrow_state = "ready"
        score += 1
        print("Score:", score)
        hit_effect_active = True
        hit_effect_index = 0
        hit_effect_timer = 0
        pygame.time.set_timer(IMPACT_SOUND_EVENT, 360)

    # Enemy Movement
    enemyx += enemyx_change
    if enemyx <= 0 or enemyx >= 600:
        enemyx_change *= -1

    # Draw Hit Effect
    if hit_effect_active:
        screen.blit(hit_frames[hit_effect_index], (enemyx, enemyy))
        hit_effect_timer += 1
        if hit_effect_timer >= hit_effect_duration:
            hit_effect_timer = 0
            hit_effect_index += 1
            if hit_effect_index >= len(hit_frames):
                hit_effect_active = False
    else:
        screen.blit(assets["duck_enemy"], (enemyx, enemyy))

    pygame.display.update()
    clock.tick(40)

pygame.quit()
