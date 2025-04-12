import pygame
from player import Player
from utils import isCollision
from assets import load_assets
from arrowVector import Arrow
from testenemy import TestEnemy
from random import randint
import asyncio

pygame.init()
screen = pygame.display.set_mode((800, 600))


clock = pygame.time.Clock()
pygame.display.set_caption("Archer Game")
icon = pygame.image.load('assets/monkey1.jpg')
pygame.display.set_icon(icon)

assets = load_assets()
player = Player(270, assets)

arrows = []
attackers = []

direction_map = {
        pygame.K_q: (-1, -1),
        pygame.K_w: (0, -1),
        pygame.K_e: (1, -1),
    }

async def main():
    
    

    score = 0
    running = True
    IMPACT_SOUND_EVENT = pygame.USEREVENT + 1

    test_enemy_initialized = False
    

    # Movement state tracking
    keys_held = {
        "left": False,
        "right": False
    }
    last_direction_key = None
    timeInterval = pygame.time.get_ticks()


    running = True
    while running:
        screen.fill((222, 200, 180))
        screen.blit(assets["background"], (0, 0))

        # Spawn animated enemy
        if pygame.time.get_ticks() % 50 == 0:
            test = TestEnemy(player, screen, randint(0, 600), randint(0, 300), assets["enemy_frames"], assets["enemy_explosions"])
            test_enemy_initialized = True
            attackers.append(test)

        # Check collision with player
        colide = player.hitBox.collidelist([a.rect for a in attackers])
        if colide != -1 and player.alive:
            print("Player hit!")
            player.die()

        for x in attackers:
            x.draw(screen)

        # Player movement
        if last_direction_key == "left":
            player.x_change = -4
        elif last_direction_key == "right":
            player.x_change = 4
        else:
            player.x_change = 0

        player.update()
        player.draw(screen)

        # Arrow logic
        for arrow in arrows[:]:
            arrow.update()
            arrow.draw(screen)
            if arrow.is_off_screen(800, 600):
                arrows.remove(arrow)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    keys_held["left"] = True
                    last_direction_key = "left"

                if event.key == pygame.K_d:
                    keys_held["right"] = True
                    last_direction_key = "right"

                if event.key in direction_map and player.alive:
                    dx, dy = direction_map[event.key]
                    px, py = player.get_position()
                    arrow = Arrow(px + player.width // 2, py + player.height // 2, dx, dy, assets["arrow"])
                    arrows.append(arrow)
                    assets["arrow_sound"].play()
                    player.is_shooting = True
                    player.shoot_frame_timer = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    keys_held["left"] = False
                    if last_direction_key == "left":
                        last_direction_key = "right" if keys_held["right"] else None

                if event.key == pygame.K_d:
                    keys_held["right"] = False
                    if last_direction_key == "right":
                        last_direction_key = "left" if keys_held["left"] else None

            if event.type == IMPACT_SOUND_EVENT:
                assets["impact_sound"].play()
                pygame.time.set_timer(IMPACT_SOUND_EVENT, 0)

        # Arrow-enemy collision
        for arrow in arrows[:]:
            colide = arrow.arrow.collideobjects(attackers, key=lambda x: x.rect)
            if colide !=None:
            
                colide.trigger_explosion()
                arrows.remove(arrow)
                attackers.remove(colide)
                score += 1
                print("Score:", score)
                pygame.time.set_timer(IMPACT_SOUND_EVENT, 360)
        
        pygame.display.update()
        clock.tick(40)
        await asyncio.sleep(0)
        #await asyncio.wait([x.thread for x in attackers])

    pygame.quit()

asyncio.run(main())
