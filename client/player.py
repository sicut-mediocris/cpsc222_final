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


    x_change = 0
    alive = True

    def die(self):
        self.alive = False

    def update(screen, alive, positionRect, change, direction):
        frame_index = 0
        shoot_frame_timer = 0
        direction = "right"
        is_moving = False
        
        
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


   
        if alive and current_animation:
            if len(current_animation) > 0:
                frame_index = frame_index % len(current_animation)
                frame = current_animation[frame_index]
                screen.blit(frame, positionRect)

    