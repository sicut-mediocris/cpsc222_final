import pygame
import threading
import time

class TestEnemy:
    def __init__(self, player, screen, spawnx, spawny, enemy_frames, explosion_frames):
        self.rect = pygame.Rect(spawnx, spawny, 40, 50)
        self.player = player
        self.speed = 5
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

        self.thread = threading.Thread(target=self.move, daemon=True)
        self.thread.start()

    def draw(self, screen):
        if self.exploding:
            if self.explosion_index < len(self.explosion_frames):
                frame = pygame.transform.scale(self.explosion_frames[self.explosion_index], (40, 40))
                screen.blit(frame, self.rect)
                self.explosion_timer += 1
                if self.explosion_timer >= self.explosion_delay:
                    self.explosion_timer = 0
                    self.explosion_index += 1
        elif self.alive:
            frame = pygame.transform.scale(self.enemy_frames[self.frame_index], (40, 40))
            screen.blit(frame, self.rect)
            self.frame_timer += 1
            if self.frame_timer >= self.animation_speed:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.enemy_frames)

    def move(self):
        while self.alive:
            player_x, player_y = self.player.get_position()
            direction = pygame.Vector2(player_x - self.rect.x, player_y - self.rect.y)
            if direction.length() != 0:
                direction.normalize_ip()
            self.rect.move_ip(direction * self.speed)
            time.sleep(0.10)

    def trigger_explosion(self):
        self.alive = False
        self.exploding = True

    def is_done(self):
        return self.explosion_index >= len(self.explosion_frames)

    def get_position(self):
        return (self.rect.x, self.rect.y)