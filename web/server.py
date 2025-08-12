import socket
import threading
import time
import pygame
from player import Player
from arrowVector import *
from testenemy import *
import pickle
from random import randint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 5555
HOST = '0.0.0.0'

print(HOST)

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

    try:
        keys_held = {"left": False, "right": False}
        last_direction_key = None
        running = True
        score = 0

        while running:
            try:
                move = connect.recv(1024)
                if not move:
                    break  # client closed
                move = move.decode()
            except Exception as e:
                print("recv error:", e)
                break

            changeX = '0'
            vec = (0, 0)

            if move.split(" ")[0] == 'move':
                split = move.split(" ")
                changeX = split[1]
                if split[2] == "True":
                    arrows.append(
                        Arrow(
                            thisPlayer.hitBox.x,
                            thisPlayer.hitBox.y,
                            int(split[3]),
                            int(split[4])
                        )
                    )

            # Enemy spawn
            if pygame.time.get_ticks() % 50 == 0 and thisPlayer.alive:
                test = TestEnemy(player, randint(0, 600), randint(0, 300))
                attackers.append(test)

            # Arrow-enemy collision
            for arrow in arrows[:]:
                colide = arrow.arrow.collideobjects(attackers, key=lambda x: x.rect)
                if colide is not None:
                    colide.trigger_explosion()
                    arrows.remove(arrow)
                    attackers.remove(colide)
                    score += 1

            # Player hit detection
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

            # Prepare positions
            arrowLoc = []
            for arrow in arrows[:]:
                arrow.update()
                if arrow.is_off_screen(800, 600):
                    arrows.remove(arrow)
                else:
                    arrowLoc.append(arrow.get_position())

            enemyLoc = [a.get_position() for a in attackers]

            player[playerID] = thisPlayer.getState()

            try:
                connect.send(pickle.dumps((player, arrowLoc, enemyLoc)))
            except Exception as e:
                print("send error:", e)
                break

            time.sleep(0.001)

    finally:
        # Always remove the player from dict and close socket
        if playerID in player:
            del player[playerID]
        try:
            connect.close()
        except:
            pass
        print(f"Cleaned up player {playerID}")


def connections():
    ID = 1
    while True:
        connect, addr = s.accept()
        connect.send(str(ID).encode())
        con = threading.Thread(target=game, args=(connect, ID))
        con.start()
        ID += 1


connections()
