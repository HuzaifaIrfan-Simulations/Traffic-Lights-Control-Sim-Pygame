

import pygame



from random import randint

import random

import time
import json



WIN_WIDTH = 800
WIN_HEIGHT = 800


pygame.font.init()


STAT_FONT = pygame.font.SysFont("comicsans", 30)

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

from Junction import Junction


junctions=[
Junction(0,0),Junction(0,200),Junction(200,0),Junction(200,200)

]


run = True
while(run):
    clock.tick(60)

    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    for junction in junctions:
        junction.draw(win)


    pygame.display.update()

