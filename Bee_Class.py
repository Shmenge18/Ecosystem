from Player_Class import Player, Bee_List, Hive_List
from copy import deepcopy
from math import pi,cos,sin
from Functions import squarestouching


class Hive(Player):
    def __init__(self,x,y,classname):
        Player.__init__(self,x,y)
        self.x = self.x + 5
        self.y = self.y + 3
        self.color = "white"
        self.type = "hive"
        self.count = 0
        self.countdowntime = 100
        self.countdown = self.countdowntime
        self.childclass = classname
        self.childlist = []
        Hive_List.append(self)

    def act(self):
        if self.countdown == 0:
            self.childlist.append(self.childclass(self.x,self.y,self.childclass))
            self.count += 1
            self.countdown = self.countdowntime
        self.countdown -= 1

    def kill(self):
        self.childlist = []
        child = self.childclass(self.x,self.y,self.childclass)
        child.queen = True
        Hive_List.pop(Hive_List.index(self))


class Bee(Player):
    def __init__(self,x,y):
        Player.__init__(self,x,y)
        Bee_List.append(self)

        # self.classname = classname
        self.age = 75

        # Change these to stats bees should have
        self.width = 5
        self.height = 5
        self.max_Speed = 7
        self.color = "yellow"
        self.viewrange = 100
        self.health = 100
        self.strength = 100
        self.stamina = 100

        self.home = None
        self.type = "bee"
        self.polin = 0
        self.maxpolin = 0
        self.queen = False

    def kill(self):
        Bee_List.pop(Bee_List.index(self))
    def nest(self):
        if self.action_allowed:
            self.action_allowed = False
            if self.target.type == "tree" and squarestouching(self,self.target) and self.queen:
                Hive(self.x,self.y,self.classname)
    def move(self):
        if self.action_allowed:
            self.action_allowed = False
            self.speed = min(self.max_Speed,self.speed)
            self.y += -cos(self.direction / 180 * pi) *self.speed
            self.x += -sin(self.direction / 180 * pi) *self.speed

    def polinate(self):
        if not self.queen and self.action_allowed:
            self.action_allowed = False
            if squarestouching(self,self.target):
                if self.target.type == "grass" and self.target.polincount < 10:
                    self.polin = min(self.polin+1,self.maxpolin)
                    self.target.polincount += 1
    def makehoney(self):
        try:
            if not self.queen and self.action_allowed:
                self.action_allowed = False
                if squarestouching(self,self.target) and self in self.target.childlist:
                    self.target.score += self.polin
                    self.polin = 0
        except:
            print("Honey Was not succesfully Made")
    def upgrade_char(self,next_Upgrade):
        if next_Upgrade == "MS":
            self.max_Speed += .3
        if next_Upgrade == "MP":
            self.maxpolin += 1
        if next_Upgrade == "STA":
            self.maxstamina += 1