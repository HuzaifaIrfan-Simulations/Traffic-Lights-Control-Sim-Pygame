

from Light import Light

import pygame


from random import randint


WIN_WIDTH=800
WIN_HEIGHT=800

shift=50

directions=["north","east","south","west"]

locations=[(shift+250,shift+0),(shift+0,shift+250),(shift+250,shift+500),(shift+500,shift+250)]

lights=[Light(locations[0]),Light(locations[1]),Light(locations[2]),Light(locations[3])]



cars=[[],[],[],[]]

for i in range(0,4):
    num=randint(0,25)
    for n in range(0,num):
        cars[i].append(0)


def getnewcars(i):
    global cars

    newcars=[]
    num=randint(0,25)
    for n in range(0,num):
        newcars.append(0)

    cars[i]=newcars



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


run=True
while(run):
    clock.tick(60)

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


    for n, light in enumerate(lights):

        light.cars=len(cars[n])
        light.checkcars()
        
        light.running()
        
        light.draw(win)

    
    countremainingtime()




    pygame.display.update()

