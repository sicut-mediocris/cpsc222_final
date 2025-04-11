import pygame
import threading
import time
import asyncio
import math
class TestEnemy:
    def __init__(self, player, spawnx, spawny):
        self.rect = pygame.Rect(spawnx, spawny, 30, 30)
        self.player = player
        self.speed = 2
        

        

        self.alive = True
        

        self.thread = threading.Thread(target=self.move, daemon=True)
        self.thread.start()

    

    def move(self):
        while self.alive:
            closest = 2000
            x = 0
            y = 0
            for key, val in self.player.items():
                check = abs(math.hypot(val[1].x - self.rect.x, val[1].y - self.rect.y))
                if  check < closest:
                    target = self.player[key]
                    x = target[1].x
                    y = target[1].y
                    closest = check
            direction = pygame.Vector2(x - self.rect.x, y - self.rect.y)
            if direction.length() != 0:
                direction.normalize_ip()
            self.rect.move_ip(direction * self.speed)
            time.sleep(0.025)
        
        #self.thread.cancel()

    def trigger_explosion(self):
        self.alive = False
       

    

    def get_position(self):
        return (self.rect)