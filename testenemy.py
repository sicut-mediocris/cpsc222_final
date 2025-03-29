import pygame
import random
import math
import threading
import time

class TestEnemy:

    def __init__(self, player, screen):
        self.rect = pygame.Rect(50, 50, 50, 50)
        self.x = 100
        self.y = 100
        self.colour = (255, 0, 0)
        self.player = player
        self.speed = (1,1)
        self.screen = screen
        self.draw(self.screen)
        self.x = threading.Thread(target = self.move, daemon=True)
        self.x.start()

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
        
        pygame.draw.rect(screen, self.colour, self.rect)

    def move(self):
        while True:
            playerPosition = self.player.get_position()
            v = pygame.Vector2(playerPosition[0] - self.rect.x, playerPosition[1]  - self.rect.y)
            if (v[0] != 0 or v[1] != 0):
                v.normalize_ip()
            #print(v)
            self.rect.move_ip(v + self.speed)
            #self.draw(self.screen)
            
            time.sleep(0.10)

    def get_position(self):
        return (self.x, self.y)