import pygame

import time


pygame.font.init()


STAT_FONT = pygame.font.SysFont("comicsans", 30)



size = 20

gaps=50

shift=0

position={
    "north":(shift+gaps,shift+0),
    "west":(shift+0,shift+gaps),
    "south":(shift+gaps,shift+(gaps*2)),
    "east":(shift+(gaps*2),shift+gaps)
    }


class Light_Single:

    def __init__(self,direction,jun_x,jun_y):

        self.x = position[direction][0]+jun_x
        self.y = position[direction][1]+jun_y
        self.direction=direction


        # on 0 1
        self.on = 0

   
    
    def draw(self, win):
        global size


        # text = STAT_FONT.render(
        #     self.direction, 1, (100, 100, 100))

        # win.blit(text, (self.x+size+20, self.y))



        if self.on == 0:
            #red
            light_color = (255, 0, 0)

        elif self.on == 1:
            #green
            light_color = (0, 255, 0)


        pygame.draw.ellipse(win, light_color, (self.x, self.y, size, size))


    # def running(self):

    #     if self.greencount == 0:
    #         self.setgreen = False

    #     elif self.setgreen == True:
    #         newtime = int(time.time())
    #         diff = newtime-self.prevtime

    #         # print(self.runninglightchangecount)

    #         if self.runninglightchangecount > 0:
    #             self.on = 1
    #             self.runninglightchangecount -= diff
    #             self.totalrunningtime -= diff

    #         if self.runninglightchangecount < 0:

    #             self.totalrunningtime += (2 *
    #                                       (self.lightchangecount) + self.greencount)

    #             self.runninglightchangecount = self.lightchangecount

    #         if self.runninggreencount > 0:
    #             self.on = 2
    #             self.runninggreencount -= diff
    #             self.totalrunningtime -= diff

    #         if self.runninglightchangecount == 0 and self.runninggreencount < 0:
    #             self.runninggreencount = self.greencount

    #         if self.runninggreencount == 0 and self.runninglightchangecount == 0:

    #             if self.on == 2:
    #                 self.runninglightchangecount = self.lightchangecount

    #             elif self.on == 1:
    #                 self.runninglightchangecount = -1

    #                 self.runninggreencount = -1

    #                 self.setgreen = False

    #                 self.on = 0

    #     self.prevtime = int(time.time())

    # def checkcars(self):
