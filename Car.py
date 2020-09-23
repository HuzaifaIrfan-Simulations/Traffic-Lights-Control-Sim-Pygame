



import pygame

import time







pygame.font.init()


STAT_FONT = pygame.font.SysFont("comicsans", 30)

carsize = 40




movements=[
    [
        [0,0],
        [-1,1],
        [0,1],
        [1,1]

    ],

    [
        [1,-1],
        [0,0],
        [1,1],
        [1,0]
    ],

    [
        [0,-1],
        [-1,-1],
        [0,0],
        [1,-1]
    ],

    [
        [-1,-1],
        [-1,0],
        [-1,1],
        [0,0]
    ]

]



def setvelocity(movefrom,moveto):



    vel=2
    
    vx=0

    vy=0


    # if posfrom[0]==posto[0]:
    #     vx=0

    #     if(posfrom[1]>posto[1]):
    #         vy=-1*vel
    #     else:
    #         vy=1*vel

    # elif posfrom[1]==posto[1]:

    #     vy=0

    #     if(posfrom[0]>posto[0]):
    #         vx=-1*vel
    #     else:
    #         vx=1*vel


    
    movement=movements[movefrom][moveto]

    vx = movement[0]*vel
    vy = movement[1]*vel


    
    return vx,vy







def setacceleration(movefrom,moveto):


    ax=0

    ay=0

    acc=1



    movement=movements[movefrom][moveto]

    ax=movement[0]*acc
    ay=movement[1]*acc


    # if posfrom[0]==posto[0]:
    #     ax=0

    #     if(posfrom[1]>posto[1]):
    #         ay=-1
    #     else:
    #         ay=1

    # elif posfrom[1]==posto[1]:

    #     ay=0

    #     if(posfrom[0]>posto[0]):
    #         ax=-1
    #     else:
    #         ax=1






    
    return ax,ay


class Car:

    def __init__(self, movefrom, moveto,posfrom,posto):
        self.movefrom=movefrom
        self.moveto=moveto

        self.posfrom=posfrom
        self.posto=posto

        self.ax=0
        self.ay=0

        # self.ax, self.ay= setacceleration(self.movefrom,self.moveto)


        

        self.x = posfrom[0]
        self.y = posfrom[1]

        self.vx=0
        self.vy=0

        self.vx, self.vy=setvelocity(self.movefrom,self.moveto)


        # self.animatetime=0
        # print(self)



    def draw(self, win):

        pygame.draw.rect(win, (200,200,200), (self.x ,self.y, carsize,carsize))

    def move(self):



        self.x+=self.vx
        self.y+=self.vy

        self.vx+=self.ax
        self.vy+=self.ay



        


    def __str__(self):
        msg=str(self.movefrom)+" to "+ str(self.moveto)
        return msg





