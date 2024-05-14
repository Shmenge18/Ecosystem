from Player_Class import Player, Caveman_List
from Functions import squarestouching
from random import randint

class Caveman(Player):
    def __init__(self,x,y):
        Player.__init__(self,x,y)
        self.color = "grey"
        self.type = "caveman"
        self.strength = 2
        Caveman_List.append(self)

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
                            self.score += 3
                        else:
                            self.stunned = True
                            self.stunnedtime = 0
                    elif self.target.type == "hive" and self.stamina >= 5:
                        self.stamina = max(0,self.stamina-10)
                        self.target.kill()
                        self.score += 1
                        self.target = None
                    elif self.target.type == "wolf" and self.stamina >= 25:
                        self.stamina -= 25
                        if not self.target.defend(self.strength):
                            self.target.kill()
                            self.target = None
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