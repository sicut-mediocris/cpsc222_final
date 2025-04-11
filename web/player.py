import pygame

class Player:
    def __init__(self, x, ID):
        
        self.ID = ID
        self.direction = "right"
        self.is_moving = False
        self.is_shooting = False
        self.shoot_frame_timer = 0
        self.shoot_duration = 10


        

        self.hitBox = pygame.Rect(x, 0, 50, 50)
        self.hitBox.bottom = 500

        self.x_change = 0
        self.alive = True
        self.direction = "left"

    def die(self):
        self.alive = False

    def update(self):
        self.hitBox.x += self.x_change
        self.hitBox.x = max(0, min(self.hitBox.x, 800 - 50))
        if self.x_change < 0:
            self.direction = "left"
        if self.x_change > 0:
            self.x_change = "right"

        


    def getState(self):
        return [self.alive, self.hitBox, self.x_change, self.direction]