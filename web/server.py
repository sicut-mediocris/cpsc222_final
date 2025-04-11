import socket
import threading
import time
import pygame
from player import Player
from arrowVector import *
import pickle

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
    while running:
        try:
            move = connect.recv(1024)
            move = move.decode()
        except Exception as e:
            print(e)
            break

        changeX = '0'
        if move.split(" ")[0] == 'move':
            split = move.split(" ")
            changeX = split[1]

        colide = thisPlayer.hitBox.collidelist([a.rect for a in attackers])
        if colide != -1 and thisPlayer.alive:
            print("Player hit!")
            player.die()
        
        # Player movement
        if changeX == "left":
            thisPlayer.x_change = -4
        elif changeX == "right":
            thisPlayer.x_change = 4
        else:
            thisPlayer.x_change = 0

        thisPlayer.update()
        
        for arrow in arrows[:]:
            arrow.update()
            if arrow.is_off_screen(800, 600):
                arrows.remove(arrow)

        player[playerID] = thisPlayer.getState()
        connect.send(pickle.dumps(player))
    
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