import pygame
from assets import *
class Player:
    
    
    
    def setAssets(frames):
        global assets
        assets = frames
        global animations
        animations = {
            "run_left": assets["archer_run_left"],
            "run_right": assets["archer_run_right"],
            "stand_left": assets["archer_stand_left"],
            "stand_right": assets["archer_stand_right"],
            "shoot_left": assets["archer_shoot_left"],
            "shoot_right": assets["archer_shoot_right"]
        }
        global current_animation
        current_animation = animations["stand_right"]

    direction = "right"
    is_moving = False
    is_shooting = False
    shoot_frame_timer = 0
    shoot_duration = 10

    
    
    frame_timer = 0
    animation_speed = 5

    # sample_frame = animations["stand_right"]
    # width = sample_frame.get_width()
    # height = sample_frame.get_height()

    # hitBox = pygame.Rect(270, 0, width, height)
    # hitBox.bottom = 500

    x_change = 0
    alive = True

    def die(self):
        self.alive = False

    def update(screen, alive, positionRect, change, direction):
        frame_index = 0
        shoot_frame_timer = 0
        direction = "right"
        is_moving = False
        # if shoot:
        #     shoot_frame_timer += 1
        #     if shoot_frame_timer > global shoot_duration:
        #         self.is_shooting = False

        # previous_animation = self.current_animation

        # if self.is_shooting:
        #     self.current_animation = self.animations[f"shoot_{self.direction}"]
        
        if change == "left":
            direction = "left"
            is_moving = True
            current_animation = animations["run_left"]
        elif change == "right":
            direction = "right"
            is_moving = True
            current_animation = animations["run_right"]
        else:
            is_moving = False
            current_animation = animations[f"stand_{direction}"]

        # if self.current_animation != previous_animation:
        #     self.frame_index = 0
        #     self.frame_timer = 0

        # self.frame_timer += 1
        # if self.frame_timer >= self.animation_speed:
        #     self.frame_timer = 0
        #     self.frame_index = (self.frame_index + 1) % max(len(self.current_animation), 1)

   
        if alive and current_animation:
            if len(current_animation) > 0:
                frame_index = frame_index % len(current_animation)
                frame = current_animation[frame_index]
                screen.blit(frame, positionRect)

    