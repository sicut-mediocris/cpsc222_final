
import pygame
import random
pygame.init()

# Set up the drawing window

screen = pygame.display.set_mode((800,600))

# Title and icon
pygame.display.set_caption("Monkeys and Watermelons")
icon = pygame.image.load('monkey1.jpg')
pygame.display.set_icon(icon)

# Adding background image
background = pygame.image.load('background.jpeg')
background = pygame.transform.scale(background, (800, 600))

# Player
sprite_sheet = pygame.image.load('Soldier-Idle.png')
sprite_sheet = pygame.transform.scale(sprite_sheet, (sprite_sheet.get_width() * 3, sprite_sheet.get_height() * 3))  # Scale the sprite sheet

frame_width = 64*3
frame_height = 64*3


# Trying to just work with 1 frame for now

def extract_single_frame(sheet, frame_width, frame_height, row=0, col=0):
    frame = sheet.subsurface((col * frame_width, row * frame_height, frame_width, frame_height))
    return frame

# Extract the first frame

player_frame = extract_single_frame(sprite_sheet, frame_width, frame_height)


playerX = 270
playerY = 280 
playerX_change = 0
playerY_change = 0


def player(x,y):
    screen.blit(player_frame , (x, y))




# Getting the image for the enemy

enemy1 = pygame.image.load('akshay.png')
enemy1 = pygame.transform.scale(enemy1, (frame_width, frame_height))  # Scale the enemy image
enemyx = random.randint(20,700)
enemyy = 100
enemyx_change = 4

def enemy(x,y):
    screen.blit(enemy1,(enemyx,y))




# Adding the arrow

arrow = pygame.image.load('arrow.png')
arrow = pygame.transform.scale(arrow, (arrow.get_width() * 2, arrow.get_height() * 2))  # Scale the arrow image
arrow = pygame.transform.rotate(arrow, 90)
arrowx = 0
arrowy = 280
arrowx_change = 0
arrowy_change = 20
arrow_state = "ready"

def fire_arrow(x,y):
    global arrow_state
    arrow_state = "fire"
    screen.blit(arrow,(x, y ))



running = True
clock = pygame.time.Clock()
while running:
    screen.fill((222, 200, 180))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            if event.key == pygame.K_SPACE:
            
                arrowx = playerX+100
                arrowy = playerY+100
                arrow_state = "fire"
                    
               
            if event.key == pygame.K_UP:
                playerY_change = -10
            if event.key == pygame.K_DOWN:
                playerY_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
              
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0


    # Bullet movement

    if arrow_state == "fire":
        fire_arrow(arrowx,arrowy) 
        arrowy -= arrowy_change
    if arrowy <= 0:
        arrowy = playerY
        arrow_state = "ready"
    
        
        # Checking for boundaries for the enemy


    enemyx += enemyx_change

    if enemyx <= 0:
        enemyx_change = 4
    elif enemyx >= 600:
        enemyx_change = -4

    


    
    playerX += playerX_change
    playerY += playerY_change

    # Checkign for boundaries for the player 
    if playerX <= 0:
        playerX = 0
    elif playerX >= 760:
        playerX = 760
    if playerY <= 0:
        playerY = 0
    elif playerY >= 555:
        playerY = 555




    #frame_index = (frame_index+1 ) % len(idle_frames)
    player(playerX,playerY)
    enemy(enemyx,enemyy)
    pygame.display.update()
    clock.tick(10)
pygame.quit()

