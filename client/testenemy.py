import pygame
import time
import asyncio
class TestEnemy:
    def __init__(self, player, screen, spawnx, spawny, enemy_frames, explosion_frames):
        self.rect = pygame.Rect(spawnx, spawny, 30, 30)
        self.player = player
        self.speed = 2
        self.screen = screen

        self.enemy_frames = enemy_frames
        self.explosion_frames = explosion_frames

        self.alive = True
        self.exploding = False
        self.explosion_index = 0
        self.explosion_timer = 0
        self.explosion_delay = 4  # controls how slow explosion animates

        self.frame_index = 0
        self.frame_timer = 0
        self.animation_speed = 5  # controls how fast enemy animates

        

    def draw(self, screen, position):
        
        frame = pygame.transform.scale(self.enemy_frames[0], (40, 40))
        screen.blit(frame, position)
        

    async def move(self):
        while self.alive:
            player_x, player_y = self.player.get_position()
            direction = pygame.Vector2(player_x - self.rect.x, player_y - self.rect.y)
            if direction.length() != 0:
                direction.normalize_ip()
            self.rect.move_ip(direction * self.speed)
            await asyncio.sleep(0)
        
       

    def trigger_explosion(self):
        self.alive = False
        self.exploding = True

    def is_done(self):
        return self.explosion_index >= len(self.explosion_frames)

    def get_position(self):
        return (self.rect.x, self.rect.y)