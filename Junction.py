

from mq_settings import host, port

from app_settings import directions, locations
from Light import Light

# from Car import Car

import pygame

# import asyncio

from random import randint

import random

import time
import json


from app_settings import useautocar

# from app_settings import carmovepersecond,mincargen,maxcargen


# import socketio

# # standard Python
# sio = socketio.Client()

# try:
#     sio.connect('http://localhost:3005/app')
#     print("connected to server")

# except:
#     print("cannot connect to server")


# @sio.event
# def connect():
#     print("I'm connected!")


# @sio.event
# def disconnect():
#     print("I'm disconnected!")


import socketio

sio = socketio.Client()


serveraddress = f'http://{host}:{port}/'

####################
# Connecting to SocketIO Server
####################

try:
    sio.connect(serveraddress)
    print(f"connected to server at {serveraddress}")

except:
    print(f"Cannot Connect to Server at {serveraddress}")


@sio.event
def connect():
    print(sio.sid)
    print(f'Connection established at {serveraddress}')


@sio.event
def returnnumcars(numcarsobj):
    print(numcarsobj)

    direction = numcarsobj["direction"]
    numofcars = int(numcarsobj["numofcars"])

    for light in lights:
        if light.direction == direction:
            light.numberofcars = numofcars
            light.checkcars()


@sio.event
def message(msg):
    print(msg)


####################
# Disconnected from The Server
####################

@sio.event
def disconnect():
    print('Disconnected from server')


WIN_WIDTH = 800
WIN_HEIGHT = 800


pygame.font.init()


STAT_FONT = pygame.font.SysFont("comicsans", 30)


# cars=[[],[],[],[]]

# movingcars=[]


# lights=[Light(locations[directions[0]]),Light(locations[directions[1]]),Light(locations[directions[2]]),Light(locations[directions[3]])]
lights = []

for i, direction in enumerate(directions):
    lights.append(Light(locations[directions[i]], directions[i]))


# for i in range(0,4):
#     num=randint(mincargen,maxcargen)
#     for n in range(0,num):
#         cars[i].append(i)


# def getnewcars(i):
#     global cars

#     # newcars=[]
#     num=randint(mincargen,maxcargen)
#     for n in range(0,num):
#         cars[i].append(i)


# prevlights=[[3,2,1],[0,3,2],[1,0,3],[2,1,0]]
# prevlights=[[3,2,1],[0,3,2],[1,0,3],[2,1,0]]

prevlights = []

for n in range(0, len(directions)):

    lst = []

    nnow = n-1

    if nnow < 0:
        nnow = len(directions)-1

    for i in range(0, len(directions)-1):

        # if nnow=n:
        #     nnow=len(directions)-1

        lst.append(nnow)

        nnow -= 1

        if nnow < 0:
            nnow = len(directions)-1

    prevlights.append(lst)


def countremainingtime():
    global prevlights

    global lights

    for n, prevlight in enumerate(prevlights):

        remtime = 0

        if lights[n].setgreen == True:
            lights[n].waitingtime = 0
        else:
            for i in prevlight:
                if lights[i].setgreen == True:
                    remtime += lights[i].totalrunningtime
                    break
                else:

                    remtime += lights[i].greencount
                    remtime += 2*(lights[i].lightchangecount)

            lights[n].waitingtime = remtime


win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()


lightnow = 0
greenon = False


# carmovingtime=[0,0,0,0]

# # prevtime = int(time.time())

# def movecars():
#     global carmovingtime


#     for n in range(0,4):
#         if lights[n].on==2:


#             newtime = int(time.time())
#             diff=newtime-carmovingtime[n]

#             diff=diff*carmovepersecond

#             for i in range(0,diff):
#                 if(len(cars[n])>0):
#                     cars[n].remove(n)

#                      moveto=n

# if len(prevlights)>0:
#     if len(prevlights[n])>0:

#         moveto=random.choice(prevlights[n])


#                     movingcars.append(Car(n,moveto,locations[n],locations[moveto]))


#         carmovingtime[n] = int(time.time())


# def carpassed(n):

#     fromto=movingcars.pop(n)
#     # print("passed",fromto)


run = True
while(run):
    clock.tick(60)

    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    # Running Lights

    if greenon == False:

        lights[lightnow].setgreen = True
        greenon = True

        if useautocar:

            getcarobj = {'readytogreen': str(lights[lightnow].direction)}

            print(getcarobj)

            sio.emit('sendmecarsfrompygame', getcarobj)

        # if lightnow==0:
        #     getnewcars(3)
        # else:
        #     getnewcars(lightnow-1)

        # 3
        # get number of cars from camera detection module

        if useautocar:
            pass

    if greenon == True:
        if lights[lightnow].setgreen == False:
            lightnow += 1

            if lightnow > len(directions)-1:
                lightnow = 0

            greenon = False

    # for n,car in enumerate(movingcars):

    #     car.move()
    #     car.draw(win)

    #     if car.x<0 or car.x >WIN_WIDTH:
    #         carpassed(n)

    #     if car.y<0 or car.y >WIN_HEIGHT:
    #         carpassed(n)

    for n, light in enumerate(lights):

        # light.checkcars()

        light.running()

        # light.cars=cars[n]

        light.draw(win)

    # movecars()

    # text = STAT_FONT.render(
    #     "flask values "+str(a), 1, (100, 100, 100))

    # win.blit(text, (10, 10))

    countremainingtime()

    pygame.display.update()


# ####################
# # sio Wait LOOP
# ####################
sio.wait()
