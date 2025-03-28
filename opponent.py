import pygame
import random
import math
from test2 import *

class type1:

    def __init__(self, player):
        self.rect = pygame.Rect(50, 50, 50, 50)
        self.x = 100
        self.y = 100
        self.colour = (255, 0, 0)
        self.player = player

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
        playerPosition = self.player.get_positon()
        v = pygame.Vector2(playerPosition[0] - self.rect.x, playerPosition[1]  - self.rect.y)
        v.normalize()
        self.enemy.move_ip(v)

    def get_position(self):
        return (self.x, self.y)