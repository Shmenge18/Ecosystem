from random import randint
from Sheep_Class import Sheep
from Wolf_Class import Wolf
from Bee_Class import Bee
from Caveman_Class import Caveman
import random
from Player_Class import firelist
from Functions import getclosest, getangle

class randomSheep(Sheep):
    def __init__(self,x,y):
        Sheep.__init__(self,x,y)
    def act(self):
       self.speed = 8
       self.direction = randint(0,360)
       self.move()


class randomBee(Bee):
    def __init__(self,x,y,randomBee):
        Bee.__init__(self,x,y,randomBee)
    def act(self):
       self.speed = 10
       self.direction = randint(0,360)
       self.move()

class randomCaveman(Caveman):
    def __init__(self,x,y):
        Caveman.__init__(self,x,y)
    def act(self):
        x = random.randint(1, 100)
        if len(firelist) <= 50:
            if x == 2:

                self.createfire()

            elif x == 4:

                self.addsticks()

        self.speed = 10
        self.direction = randint(0,360)
        self.move()

class randomWolf(Wolf):
    def __init__(self,x,y):
        Wolf.__init__(self,x,y)
    def act(self):
       self.speed = 10
       self.direction = randint(0,360)
       self.move()
