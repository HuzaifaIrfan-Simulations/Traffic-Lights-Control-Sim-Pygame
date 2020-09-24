



import pygame

import time


from app_settings import carsize ,setcaracc,setcarvel,caracc,carvel


from app_settings import directions, locations


pygame.font.init()


STAT_FONT = pygame.font.SysFont("comicsans", 30)




movements={
    "north":{
        "north":[0,0],
        "west":[-1,1],
        "south":[0,1],
        "east":[1,1]

    },

    "west":{
        "north":[1,-1],
        "west":[0,0],
        "south":[1,1],
        "east":[1,0]
    },

    "south":{
        "north":[0,-1],
        "west":[-1,-1],
        "south":[0,0],
        "east":[1,-1]
    },

    "east":{
        "north":[-1,-1],
        "west":[-1,0],
        "south":[-1,1],
        "east":[0,0]
    }

}





def setvelocity(movefrom,moveto):



    vel=2

    vel=carvel
    
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


    
    movement=movements[directions[movefrom]][directions[moveto]]

    vx = movement[0]*vel
    vy = movement[1]*vel


    
    return vx,vy







def setacceleration(movefrom,moveto):


    ax=0

    ay=0

    acc=1


    acc=caracc



    movement=movements[directions[movefrom]][directions[moveto]]

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


        if setcaracc:
            self.ax, self.ay= setacceleration(self.movefrom,self.moveto)


        

        self.x = posfrom[0]
        self.y = posfrom[1]

        self.vx=0
        self.vy=0

        if setcarvel:
            self.vx, self.vy=setvelocity(self.movefrom,self.moveto)


        # self.animatetime=0
        print(self)



    def draw(self, win):

        pygame.draw.ellipse(win, (200,200,200), (self.x ,self.y, carsize,carsize))

    def move(self):



        self.x+=self.vx
        self.y+=self.vy

        self.vx+=self.ax
        self.vy+=self.ay



        


    def __str__(self):
        msg=str(directions[self.movefrom])+" to "+ str(directions[self.moveto])
        return msg





