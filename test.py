print("Hello World")
 
import pygame
pygame.init()

# Set up the drawing window

screen = pygame.display.set_mode((800,600))

# Title and icon
pygame.display.set_caption("Monkeys and Watermelons")
icon = pygame.image.load('monkey1.jpg')
pygame.display.set_icon(icon)

# Player
sprite_sheet = pygame.image.load('Soldier-Idle.png')
sprite_sheet = pygame.transform.scale(sprite_sheet, (sprite_sheet.get_width() * 2, sprite_sheet.get_height() * 2))  # Scale the sprite sheet

frame_width = 64*2
frame_height = 64*2
num_frames = 4

def extract_frames(sheet,num_frames,row=0):
    frames = []
    for i in range(num_frames):
        frame = sheet.subsurface((i*frame_width,row*frame_height,frame_width,frame_height))
        frames.append(frame)
    return frames

idle_frames = extract_frames(sprite_sheet,num_frames)



playerX = 270
playerY = 280 
playerX_change = 0
playerY_change = 0
frame_index = 0
current_animation = idle_frames

def player(x,y):
    screen.blit(current_animation[frame_index], (x, y))

running = True
clock = pygame.time.Clock()
while running:
    screen.fill((222, 200, 180))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -8
            if event.key == pygame.K_RIGHT:
                playerX_change = 8
               
            if event.key == pygame.K_UP:
                playerY_change = -8
            if event.key == pygame.K_DOWN:
                playerY_change = 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
              
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    
    playerX += playerX_change
    playerY += playerY_change
    #print(str(playerX) + ", " + str(playerY))


    #frame_index = (frame_index+1 ) % len(idle_frames)
    player(playerX,playerY)
    pygame.display.update()
    clock.tick(10)
pygame.quit()

