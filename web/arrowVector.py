import pygame
import math

class Arrow:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.arrow = pygame.Rect(x, y, 5, 5)
        self.dx = dx
        self.dy = dy
        self.speed = 10
        

    def calculate_angle(self):
        angle_rad = math.atan2(-self.dy, self.dx)
        return math.degrees(angle_rad)

    def update(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        self.arrow.move_ip((self.dx * self.speed, self.dy * self.speed))


    def is_off_screen(self, screen_width, screen_height):
        return self.x < 0 or self.x > screen_width or self.y < 0 or self.y > screen_height

    def get_position(self):
        return (self.x, self.y, self.dx, self.dy)