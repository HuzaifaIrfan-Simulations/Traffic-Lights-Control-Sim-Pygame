

from Light import Light

from Car import Car

import pygame

# import asyncio

from random import randint

import random

import time
import json

# import socketio

# # standard Python
# sio = socketio.Client()

# try:
#     sio.connect('http://localhost:3008')
#     print("connected to server")

# except:
#     print("cannot connect to server")



# @sio.event
# def connect():
#     print("I'm connected!")

# @sio.event
# def connect_error():
#     print("The connection failed!")

# @sio.event
# def disconnect():
#     print("I'm disconnected!")






WIN_WIDTH=800
WIN_HEIGHT=800



pygame.font.init()


STAT_FONT = pygame.font.SysFont("comicsans", 30)

shift=50

directions=["north","east","south","west"]

locations=[(shift+250,shift+0),(shift+0,shift+250),(shift+250,shift+500),(shift+500,shift+250)]




cars=[[],[],[],[]]

movingcars=[]


lights=[Light(locations[0],cars[0]),Light(locations[1],cars[1]),Light(locations[2],cars[2]),Light(locations[3],cars[3])]


for i in range(0,4):
    num=randint(0,25)
    for n in range(0,num):
        cars[i].append(i)


def getnewcars(i):
    global cars

    # newcars=[]
    num=randint(0,25)
    for n in range(0,num):
        cars[i].append(i)

    



prevlights=[[3,2,1],[0,3,2],[1,0,3],[2,1,0]]

def countremainingtime():
    global prevlights

    global lights

    for n, prevlight in enumerate(prevlights):

        remtime=0

        if lights[n].setgreen==True:
            lights[n].waitingtime=0
        else:
            for i in prevlight:
                if lights[i].setgreen==True:
                    remtime += lights[i].totalrunningtime
                    break
                else:

                    remtime += lights[i].greencount
                    remtime +=  2*(lights[i].lightchangecount)



            lights[n].waitingtime=remtime







win= pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
clock=pygame.time.Clock()


lightnow=0
greenon=False


carmovingtime=[0,0,0,0]

# prevtime = int(time.time())

def movecars():
    global carmovingtime


    for n in range(0,4):
        if lights[n].on==2:
            


            newtime = int(time.time())
            diff=newtime-carmovingtime[n]

            for i in range(0,diff):
                if(len(cars[n])>0):
                    cars[n].remove(n)

                    moveto=random.choice(prevlights[n])


                    movingcars.append(Car(n,moveto,locations[n],locations[moveto]))




        carmovingtime[n] = int(time.time())



def carpassed(n):

    fromto=movingcars.pop(n)
    # print("passed",fromto)
    



run=True
while(run):
    clock.tick(60)

    # sio.emit('msg', {'lights': str(lights)})

    win.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
            quit()




    # Running Lights

    if greenon==False:

        lights[lightnow].setgreen=True
        greenon=True

        if lightnow==0:
            getnewcars(3)
        else:
            getnewcars(lightnow-1)

    if greenon==True:
        if lights[lightnow].setgreen==False:
            lightnow+=1

            if lightnow>3:
                lightnow=0

            greenon=False

    
    for n,car in enumerate(movingcars):

        car.move()
        car.draw(win)

        if car.x<0 or car.x >WIN_WIDTH:
            carpassed(n)

        if car.y<0 or car.y >WIN_HEIGHT:
            carpassed(n)



    for n, light in enumerate(lights):

        
        light.checkcars()
        
        light.running()

        light.cars=cars[n]
        
        light.draw(win)

    
    movecars()






    # text = STAT_FONT.render(
    #     "flask values "+str(a), 1, (100, 100, 100))

    # win.blit(text, (10, 10))

    
    countremainingtime()




    pygame.display.update()









