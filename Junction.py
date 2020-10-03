
from Light_Single import Light_Single




class Junction:


    def __init__(self,x,y):

        self.x = x
        self.y = y


        # on 0 1
        self.on = 0

        self.directions=["north","east","south","west"]

        self.lights=[]

        for direction in self.directions:
            self.lights.append(Light_Single(direction,self.x,self.y))



    
    def draw(self,win):

        for light in self.lights:
            light.draw(win)