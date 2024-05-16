import time

from Player_Class import Player, Sheep_List
from Functions import squarestouching, getangle, getclosest
from random import randint
class Sheep(Player):
    def __init__(self,x,y):
        Player.__init__(self,x,y)
        Sheep_List.append(self)
        self.type = "sheep"
        self.wait = 0

    def act(self):
        if self.wait > 0:
            self.wait -= 1
            return
        #Speed and direction varibles must be changed before moving (max speed is 10 so sheep doesn't go 1000000)
        self.speed = 0
        self.direction = randint(0, 360)
        if randint(0,1) == 1:
            self.direction = getangle(self,self.target)
            self.speed = 10
            self.move()
        else:
            self.scan()
            self.target = getclosest(self,self.grasslist)
            if self.stamina <= 3:
                self.wait = 30
        if squarestouching(self, self.target):
            self.target.kill()
            self.target = None
            self.age -= randint(50, 200)
            self.score += 2

    def attack(self):
        if self.action_allowed:
            self.action_allowed = False
            try:
                if self.target.planttype.type == "grass" and squarestouching(self, self.target):
                    self.target.kill()
                    self.target = None
                    self.score += 2
            except:
                pass
    def kill(self):
        Sheep_List.pop(Sheep_List.index(self))
    def defend(self,oppattackstrength):
        self.action_allowed = True
        self.scan()
        sheep = self.sheeplist
        self.clearinfo()
        return len(sheep)//5 + self.stamina//25 + self.strength > randint(0+oppattackstrength,10+oppattackstrength)

    def upgrade_char(self, next_Upgrade):
        if next_Upgrade == "MS":
            self.max_Speed += 1
        elif next_Upgrade == "STR":
            self.strength += 1
        elif next_Upgrade == "STA":
            self.maxstamina += 1
            self.stamina = self.maxstamina
        elif next_Upgrade == "REG":
            self.staminaregen += .5
            self.stamina = self.maxstamina