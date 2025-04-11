import pygame
import math

class Arrow:
    def __init__(self, image):
        
       
        self.speed = 10
        self.image = image

    def calculate_angle(self, dx, dy):
        angle_rad = math.atan2(-dy, dx)
        return math.degrees(angle_rad)



    def draw(self, screen, x, y, dx, dy):
        angle = self.calculate_angle(dx, dy)
        rotated = pygame.transform.rotate(self.image, angle)
        rect = rotated.get_rect(center=(x, y))
        screen.blit(rotated, rect.topleft)

 

    def get_position(self):
        return (self.x, self.y)