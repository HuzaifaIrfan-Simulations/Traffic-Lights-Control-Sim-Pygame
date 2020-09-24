
from app_settings import defaultyellowlighttime, defaultgreenlighttime, useautocar, carcountsettings
import pygame

import time


pygame.font.init()


STAT_FONT = pygame.font.SysFont("comicsans", 30)

size = 20


class Light:

    def __init__(self, loc, direction):

        self.x = loc[0]
        self.y = loc[1]

        self.direction = direction

        self.waitingtime = 0

        self.cars = []

        self.numberofcars = 0

        # on 0 1 2
        self.on = 0

        self.totalrunningtime = 0

        self.lightchangecount = 2
        self.lightchangecount = defaultyellowlighttime

        self.runninglightchangecount = -1

        self.greencount = 5
        self.greencount = defaultgreenlighttime

        self.runninggreencount = -1

        self.prevtime = int(time.time())

        self.setgreen = False

    def draw(self, win):
        global size
        # pygame.draw.rect(win,(255,255,255),(0,0,60,20))
        pygame.draw.rect(win, (100, 100, 100), (self.x, self.y, size*3, size))

        text = STAT_FONT.render("rg = "+str(self.runninggreencount) +
                                ", ry = "+str(self.runninglightchangecount), 1, (100, 100, 100))

        win.blit(text, (self.x-20, self.y+size+10))

        text = STAT_FONT.render("sg = "+str(self.greencount) +
                                ", sy = "+str(self.lightchangecount), 1, (100, 100, 100))

        win.blit(text, (self.x-20, self.y+size+30))

        text = STAT_FONT.render(
            "Cars = "+str(len(self.cars)), 1, (100, 100, 100))

        win.blit(text, (self.x-20, self.y+size+50))

        text = STAT_FONT.render(
            "Waiting = "+str(self.waitingtime), 1, (100, 100, 100))

        win.blit(text, (self.x-20, self.y+size+70))

        text = STAT_FONT.render(
            "Total running time = "+str(self.totalrunningtime), 1, (100, 100, 100))

        win.blit(text, (self.x-20, self.y+size+90))

        red = (100, 0, 0)
        yellow = (100, 100, 10)
        green = (0, 100, 0)

        if self.on == 0:
            red = (255, 0, 0)

        elif self.on == 1:
            yellow = (255, 255, 25)

        elif self.on == 2:
            green = (0, 255, 0)

        # red Light
        # pygame.draw.ellipse(win,(255,0,0),(0,0,20,20))
        pygame.draw.ellipse(win, red, (self.x, self.y, size, size))

        # yellow Light
        # pygame.draw.ellipse(win,(255,255,25),(20,0,20,20))
        pygame.draw.ellipse(win, yellow, (self.x+size, self.y, size, size))

        # green Light
        # pygame.draw.ellipse(win,(0,255,0),(40,0,20,20))
        pygame.draw.ellipse(win, green, (self.x+size*2, self.y, size, size))

    def running(self):

        if self.greencount == 0:
            self.setgreen = False

        elif self.setgreen == True:
            newtime = int(time.time())
            diff = newtime-self.prevtime

            # print(self.runninglightchangecount)

            if self.runninglightchangecount > 0:
                self.on = 1
                self.runninglightchangecount -= diff
                self.totalrunningtime -= diff

            if self.runninglightchangecount < 0:

                self.totalrunningtime += (2 *
                                          (self.lightchangecount) + self.greencount)

                self.runninglightchangecount = self.lightchangecount

            if self.runninggreencount > 0:
                self.on = 2
                self.runninggreencount -= diff
                self.totalrunningtime -= diff

            if self.runninglightchangecount == 0 and self.runninggreencount < 0:
                self.runninggreencount = self.greencount

            if self.runninggreencount == 0 and self.runninglightchangecount == 0:

                if self.on == 2:
                    self.runninglightchangecount = self.lightchangecount

                elif self.on == 1:
                    self.runninglightchangecount = -1

                    self.runninggreencount = -1

                    self.setgreen = False

                    self.on = 0

        self.prevtime = int(time.time())

    def checkcars(self):

        if useautocar:

            for lightsetting in carcountsettings:
                if self.numberofcars >= lightsetting["mincars"]:
                    self.greencount = lightsetting["green"]
                    self.lightchangecount = lightsetting["yellow"]

                    break

            # if len(self.cars) > 20:
            #     self.greencount = 20
            #     self.lightchangecount = 5

            # elif len(self.cars) > 10:
            #     self.greencount = 10
            #     self.lightchangecount = 2

            # elif len(self.cars) > 5:
            #     self.greencount = 10
            #     self.lightchangecount = 2

            # elif len(self.cars) > 0:
            #     self.greencount = 5
            #     self.lightchangecount = 2

            # elif len(self.cars) <= 0:
            #     self.greencount = 5
            #     self.lightchangecount = 2
