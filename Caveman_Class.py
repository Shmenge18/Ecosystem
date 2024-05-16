from Player_Class import Player, Caveman_List, firelist
from Functions import squarestouching, getdistance
from random import randint
import pygame
class fire:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 500
        self.type = "fire"

    def spawn(self, firelist):
        firewidth = 10
        fireheight = 10
        firecolour = "red"
        build = True
        if len(firelist) > 1:
            q = 0
            for i in range (len(firelist)):
                distance = getdistance(self, firelist[q])
                if distance <= 20:
                    build = False
                    break
                else:
                    build = True
                q = q + 1

        if build == True:
            #pygame.draw.rect(screen, firecolour, pygame.Rect(self.x - firewidth // 2, self.y - fireheight // 2, firewidth, fireheight))
            firelist.append(self)
            self.sticks -= 1
            print("sticks", self.sticks)


    def burnout(self):
        firelist.remove(self)

    def grow(self):
        self.timer = self.timer + 20
        self.x = self.x + 1
        self.y = self.y + 1
class Caveman(Player):
    def __init__(self,x,y):
        Player.__init__(self,x,y)
        self.color = "grey"
        self.type = "caveman"
        self.strength = 2
        self.sticks = 1
        Caveman_List.append(self)

    def act(self):
        pass

    def createfire(self):
        if self.action_allowed:
            if self.sticks >=0:
                newfire = fire(self.x, self.y)
                newfire.spawn(firelist)
                self.sticks = self.sticks - 1

    def addsticks(self):
        if self.action_allowed:
            if self.sticks >= 1:
                if squarestouching(self, self.target) and self.target.type == "fire":
                    fire = self.target
                    fire.grow()
                    self.sticks = self.sticks - 1


    def time(self):
        pass





    def attack(self):
        if self.action_allowed:
            self.action_allowed = False
            try:
                if squarestouching(self,self.target):
                    if self.target.type == "sheep" and self.stamina >= 25:
                        self.stamina -= 25
                        if not self.target.defend(self.strength):
                            self.target.kill()
                            self.target = None
                            self.age -= randint(500, 1000)
                            self.score += 3
                        else:
                            self.stunned = True
                            self.stunnedtime = 0
                    elif self.target.type == "hive" and self.stamina >= 5:
                        self.stamina = max(0,self.stamina-10)
                        self.target.kill()
                        self.age -= (400, 600)
                        self.score += 1
                        self.target = None
                    elif self.target.type == "wolf" and self.stamina >= 25:
                        self.stamina -= 25
                        if not self.target.defend(self.strength):
                            self.target.kill()
                            self.target = None
                            self.age -= (600, 1100)
                            self.score += 5
                        else:
                            self.stunned = True
                            self.stunnedtime = 0
            except:
                pass
    def kill(self):
        Caveman_List.pop(Caveman_List.index(self))
    def defend(self,oppattackstrength):
        return randint(0+self.strength,10+self.strength) > randint(0 + oppattackstrength, 10 + oppattackstrength)
    def upgrade_char(self, next_Upgrade):
        if next_Upgrade == "MS":
            self.max_Speed += .3
        elif next_Upgrade == "VR":
            self.viewrange += 10
        elif next_Upgrade == "S":
            self.strength += 10
        elif next_Upgrade == "VR":
            self.viewrange += 10