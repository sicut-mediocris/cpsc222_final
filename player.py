import pygame

class Player:
    def __init__(self, x, y, frame):
        self.hitBox = frame.get_rect()
        self.hitBox.topleft = (x, y)
        self.frame = frame
        self.x_change = 0
        self.y_change = 0
        self.alive = True

    def update(self):
        if(self.alive):
            self.hitBox.move_ip((self.x_change, self.y_change))
            self.hitBox.x = max(0, min(self.hitBox.x, 760))
            self.hitBox.y = max(0, min(self.hitBox.y, 555))

    def draw(self, screen):
        if(self.alive):
            screen.blit(self.frame, self.hitBox)

    def get_position(self):
        return (self.hitBox.x, self.hitBox.y)
    
    def die(self):
        self.alive = False