import pygame
import threading
import time

class TestEnemy:
    def __init__(self, player, screen, spawnx, spawny):
        self.rect = pygame.Rect(spawnx, spawny, 50, 50)  # use spawn coords
        self.colour = (255, 0, 0)
        self.player = player
        self.speed = 5
        self.screen = screen

        # Start enemy movement in a separate thread
        self.thread = threading.Thread(target=self.move, daemon=True)
        self.thread.start()

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)

    def move(self):
        while True:
            player_x, player_y = self.player.get_position()
            direction = pygame.Vector2(player_x - self.rect.x, player_y - self.rect.y)
            if direction.length() != 0:
                direction.normalize_ip()
            self.rect.move_ip(direction * self.speed)
            time.sleep(0.10)

    def get_position(self):
        return (self.rect.x, self.rect.y)
