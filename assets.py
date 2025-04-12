import pygame

def load_animation(folder, count):
    return [
        pygame.image.load(f"{folder}/frame ({i}).png").convert_alpha()
        for i in range(1, count + 1)
    ]

def load_assets():
    # Background
    background = pygame.image.load('assets/background.jpeg')
    background = pygame.transform.scale(background, (800, 600))

  
    archer_run_left = load_animation('assets/archer_sprites/Running_Towards_Left', 5)
    archer_run_right = load_animation('assets/archer_sprites/Running_Towards_Right', 5)
    archer_shoot_left = load_animation('assets/archer_sprites/ShootingArrow_Towards_Left', 4)
    archer_shoot_right = load_animation('assets/archer_sprites/ShootingArrow_Towards_Right', 4)
    archer_stand_left = load_animation('assets/archer_sprites/Standing_Facing_Left', 3)
    archer_stand_right = load_animation('assets/archer_sprites/Standing_Facing_Right', 3)

    enemy_frames = load_animation('assets/enemy_frames', 8)
    enemy_explosions = load_animation('assets/enemy_after_shot', 3)


    arrow = pygame.image.load('assets/arrow.png').convert_alpha()
    arrow = pygame.transform.scale(arrow, (arrow.get_width(), arrow.get_height()))

    arrow_sound = pygame.mixer.Sound('assets/arrow_swish.mp3')
    impact_sound = pygame.mixer.Sound('assets/arrow_impact.mp3')
    arrow_sound.set_volume(0.3)
    impact_sound.set_volume(0.3)

    return {
        "background": background,
        "archer_run_left": archer_run_left,
        "archer_run_right": archer_run_right,
        "archer_shoot_left": archer_shoot_left,
        "archer_shoot_right": archer_shoot_right,
        "archer_stand_left": archer_stand_left,
        "archer_stand_right": archer_stand_right,
        "enemy_frames": enemy_frames,
        "enemy_explosions": enemy_explosions,
        "arrow": arrow,
        "arrow_sound": arrow_sound,
        "impact_sound": impact_sound,
    }