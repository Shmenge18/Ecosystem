#Pygame import
import pygame

#Other imports
from math import cos,sin,pi
from copy import deepcopy
from random import randint

#Project Imports
from Functions import squarestouching, getdistance

#Varibles
global globalreproducecountdown
globalreproducecountdown = 100 #every 100 ticks

#List of all the differnt types of classes!!!!!
#If you are adding a new type of class be sure to add your list here
Wolf_List = []
Sheep_List = []
Bee_List = []
Obstruction_List = []
Caveman_List = []
Hive_List = []

# PLANTS
Grass_List = []
Tree_List = []
Dirt_List = []
Bush_List = []
Twig_List = []



#Here we go
class Player:
    #Innit function all the differnt varibles are catergorized below
    def __init__(self,x,y):
        #Grade 12s assign...
        #Doesn't change by Inherintance
        self.x = x
        self.y = y
        self.level = 0
        self.action_allowed = True
        self.score = 0
        self.stunned = False
        self.stunnedtime = 0
        self.age = 0
        self.strength = 0
        #Objects in area (Already Sorted by type-Through Scan Function)
        self.sheeplist = []
        self.beelist = []
        self.wolflist = []
        self.grasslist = []
        self.treelist = []
        self.dirtlist = []
        self.bushlist = []
        self.hivelist = []
        self.twiglist = []
        #Can Change by inheritance
        self.width = 10
        self.height = 10
        self.max_Speed = 5
        self.color = "blue"
        self.viewrange = 100
        self.health = 100
        self.strength = 100
        self.stamina = 100
        self.maxstamina = 100
        self.staminaregen = 1
        self.type = "player"
        self.reproducecountdown = globalreproducecountdown

        #Grade 11s can use and change
        self.image = None
        self.direction = 0
        self.speed = 10
        self.target = None
        obj = self
    def clearinfo(self):
        self.sheeplist = []
        self.beelist = []
        self.wolflist = []
        self.grasslist = []
        self.treelist = []
        self.dirtlist = []
        self.bushlist = []
        self.twiglist = []

    #Scan function can stay the same for all other classes
    def scan(self):
        if self.action_allowed:
            self.action_allowed = False
            listtype1 = [Sheep_List, Bee_List, Wolf_List, Grass_List, Tree_List, Dirt_List, Bush_List, Twig_List]
            listtype2 = [self.sheeplist, self.beelist, self.wolflist, self.grasslist, self.treelist, self.dirtlist,
                         self.bushlist, self.twiglist]
            for y in range(0, len(listtype1)):
                for x in listtype1[y]:
                    if getdistance(self, x) <= self.viewrange and x != self:
                        listtype2[y].append(x)
    #Move function does not need to change for other classes
    #Direction is in degrees 0-360; North=0,East=90,South=180,West=270
    def move(self):
        #THis check is because charcter is only allowed to do one action per tick
        if self.action_allowed:
            self.action_allowed = False

            #Makes sure the speed doesn't pass max speed
            self.speed = min(self.max_Speed,self.speed,self.stamina)

            #Moves the charcter porportionally to the speed and direction
            self.y += -cos(self.direction / 180 * pi) * self.speed
            self.x += -sin(self.direction / 180 * pi) * self.speed

            #This is a ridicously somewhat less sillly way then before to make sure that any obsticles is detected
            for x in Tree_List:
                if squarestouching(x,self):
                    self.y -= -cos(self.direction / 180 * pi) * self.speed
                    self.x -= -sin(self.direction / 180 * pi) * self.speed
                    self.stamina = max(0,self.stamina-5)
                    return None

            #Will lower stamina by the speed
            self.stamina -= self.speed


            #The math on how I decided what percentage of the speed is changing the y and what changes the x


    #Default reproduce condition Change this for new classees (This is not at all what it would look like)
    def reproducecondition(self):
        return self.reproducecountdown <= 0
    #Upgrade condition
    def upgradecondition(self):
        return self.score >= [5,10,15,20,25,50][self.level]
    #Step1 of the upgrade system (Doesn't change in inherntence)
    def upgrade(self,code):
        if self.action_allowed:
            self.action_allowed = False
            if self.upgradecondition():

                #Runs the function that actually upgrades the charcter
                self.upgrade_char(code)

                self.level += 1
    #This does change because differnt classes will upgrade differnt things
    def upgrade_char(self,next_Upgrade):
        if next_Upgrade == "MS":
            self.max_Speed += .1
        if next_Upgrade == "W":
            self.width += 1
        if next_Upgrade == "H":
            self.height += 1
        if next_Upgrade == "S":
            self.stamina += 1
    #Changed through inherentence
    def attack(self):
        pass
    #This does not change from most classes (maybe some exceptinos) however its not finished coded yet
    def reproduce(self):

        if self.action_allowed:
            self.action_allowed = False
            if self.type == self.target.type and self.target.target == self and self.reproducecondition():
                child = deepcopy(self)
                child.__init__(self.x,self.y)

                self.target.reproducecountdown = 100
                self.reproducecountdown = 100
                self.target.target = None
                self.target = None

    def tick(self):
        self.reproducecountdown = max(0,self.reproducecountdown-1)
        self.age += 1
    #Just in case the grade 11s don't add act function. THis will avoid an error
    def act(self):
        pass