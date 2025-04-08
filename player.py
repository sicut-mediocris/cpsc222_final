import pygame

class Player:
    def __init__(self, x, assets):
        self.assets = assets

        self.animations = {
            "run_left": assets["archer_run_left"],
            "run_right": assets["archer_run_right"],
            "stand_left": assets["archer_stand_left"],
            "stand_right": assets["archer_stand_right"],
            "shoot_left": assets["archer_shoot_left"],
            "shoot_right": assets["archer_shoot_right"]
        }

        self.direction = "right"
        self.is_moving = False
        self.is_shooting = False
        self.shoot_frame_timer = 0
        self.shoot_duration = 10

        self.current_animation = self.animations["stand_right"]
        self.frame_index = 0
        self.frame_timer = 0
        self.animation_speed = 5

        sample_frame = self.current_animation[0]
        self.width = sample_frame.get_width()
        self.height = sample_frame.get_height()

        self.hitBox = pygame.Rect(x, 0, self.width, self.height)
        self.hitBox.bottom = 500

        self.x_change = 0
        self.alive = True

    def die(self):
        self.alive = False

    def update(self):
        self.hitBox.x += self.x_change
        self.hitBox.x = max(0, min(self.hitBox.x, 800 - self.width))

        if self.is_shooting:
            self.shoot_frame_timer += 1
            if self.shoot_frame_timer > self.shoot_duration:
                self.is_shooting = False

        previous_animation = self.current_animation

        if self.is_shooting:
            self.current_animation = self.animations[f"shoot_{self.direction}"]
        elif self.x_change < 0:
            self.direction = "left"
            self.is_moving = True
            self.current_animation = self.animations["run_left"]
        elif self.x_change > 0:
            self.direction = "right"
            self.is_moving = True
            self.current_animation = self.animations["run_right"]
        else:
            self.is_moving = False
            self.current_animation = self.animations[f"stand_{self.direction}"]

        if self.current_animation != previous_animation:
            self.frame_index = 0
            self.frame_timer = 0

        self.frame_timer += 1
        if self.frame_timer >= self.animation_speed:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % max(len(self.current_animation), 1)

    def draw(self, screen):
        if self.alive and self.current_animation:
            if len(self.current_animation) > 0:
                frame_index = self.frame_index % len(self.current_animation)
                frame = self.current_animation[frame_index]
                screen.blit(frame, self.hitBox)

    def get_position(self):
        return (self.hitBox.x, self.hitBox.y)