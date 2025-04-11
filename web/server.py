import socket
import threading
import time
import pygame
from player import Player
from arrowVector import *
from testenemy import *
import pickle
from random import randint

s = socket.socket()

PORT = 5555
HOST = socket.gethostname()
IP = socket.gethostbyname(HOST)

print(HOST)
print(IP)

#nia
#10.5.0.2

s.bind((HOST, PORT))
s.listen()



pygame.init()


clock = pygame.time.Clock()

REVIVE = pygame.USEREVENT + 1
CLEAR = pygame.USEREVENT + 2

arrows = []

attackers = []

direction_map = {
        pygame.K_q: (-1, -1),
        pygame.K_w: (0, -1),
        pygame.K_e: (1, -1),
    }

player = {}


def game(connect, playerID):
    thisPlayer = Player(270, playerID)
    player[playerID] = thisPlayer.getState()
    keys_held = {
        "left": False,
        "right": False
    }
    last_direction_key = None
    running = True
    score = 0
    while running:
        try:
            move = connect.recv(1024)
            move = move.decode()
        except Exception as e:
            print(e)
            break

        changeX = '0'
      
        vec = (0, 0)
        if move.split(" ")[0] == 'move':
            split = move.split(" ")
            changeX = split[1]
            if split[2] == "True":
                arrows.append(Arrow(thisPlayer.hitBox.x, thisPlayer.hitBox.y, int(split[3]), int(split[4])))

        if pygame.time.get_ticks() % 50 == 0 and thisPlayer.alive:
            test = TestEnemy(player, randint(0, 600), randint(0, 300))
            test_enemy_initialized = True
            attackers.append(test)
            
        for arrow in arrows[:]:
            colide = arrow.arrow.collideobjects(attackers, key=lambda x: x.rect)
            if colide !=None:
            
                colide.trigger_explosion()
                arrows.remove(arrow)
                attackers.remove(colide)
                score += 1
                print("Score:", score)

        colide = thisPlayer.hitBox.collidelist([a.rect for a in attackers])
        if colide != -1 and thisPlayer.alive:
            print("Player hit!")
            thisPlayer.die()
            pygame.time.set_timer(REVIVE, 5000)
            for a in attackers:
                a.trigger_explosion()
            attackers.clear()
        
        

        for event in pygame.event.get():
            if event.type == REVIVE:
                thisPlayer.alive = True

                
        
        # Player movement
        if changeX == "left":
            thisPlayer.x_change = -4
        elif changeX == "right":
            thisPlayer.x_change = 4
        else:
            thisPlayer.x_change = 0

        thisPlayer.update()
        arrowLoc = []
        for arrow in arrows[:]:
            arrow.update()

            if arrow.is_off_screen(800, 600):
                arrows.remove(arrow)
            else:
                arrowLoc.append(arrow.get_position())
        enemyLoc = []
        for a in attackers:
            enemyLoc.append(a.get_position())
        player[playerID] = thisPlayer.getState()
        connect.send(pickle.dumps((player, arrowLoc, enemyLoc)))
    
        time.sleep(0.001)
    del player[playerID]
    connect.close()

def connections():
    ID = 1
    while True:
        connect, addr = s.accept()
        connect.send(str(ID).encode())
        con = threading.Thread(target=game, args=(connect, ID))
        con.start()
        ID += 1

connections()