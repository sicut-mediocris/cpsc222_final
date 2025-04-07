import pygame

def load_assets():
    frame_width = 64 * 3
    frame_height = 64 * 3

    background = pygame.image.load('assets/background.jpeg')
    background = pygame.transform.scale(background, (800, 600))

    sprite_sheet = pygame.image.load('assets/Soldier-Idle.png').convert_alpha()
    sprite_sheet = pygame.transform.scale(sprite_sheet, (sprite_sheet.get_width() * 3, sprite_sheet.get_height() * 3))

    duck_enemy = pygame.image.load('assets/duck_man_og.png')
    duck_enemy = pygame.transform.scale(duck_enemy, (frame_width, frame_height))

    hit_sprite_sheet = pygame.image.load('assets/duck_man_sprite.png')
    hit_sprite_sheet = pygame.transform.scale(hit_sprite_sheet, (hit_sprite_sheet.get_width()*2, hit_sprite_sheet.get_height()*2))

    arrow = pygame.image.load('assets/arrow.png')
    arrow = pygame.transform.scale(arrow, (arrow.get_width() * 2, arrow.get_height() * 2))
    arrow = pygame.transform.rotate(arrow, 90)

    arrow_sound = pygame.mixer.Sound('assets/arrow_swish.mp3')
    impact_sound = pygame.mixer.Sound('assets/arrow_impact.mp3')

    return {
        "background": background,
        "sprite_sheet": sprite_sheet,
        "duck_enemy": duck_enemy,
        "arrow": arrow,
        "hit_sprite_sheet": hit_sprite_sheet,
        "arrow_sound": arrow_sound,
        "impact_sound": impact_sound,
        "frame_width": frame_width,
        "frame_height": frame_height,
        "hit_frame_width": 200,
        "hit_frame_height": 200
    }