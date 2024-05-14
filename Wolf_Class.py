from Player_Class import Player, Wolf_List
from Functions import squarestouching
from random import randint
class Wolf(Player):
    def __init__(self,x,y):
        Player.__init__(self,x,y)
        self.color = "pink"
        self.type = "wolf"
        Wolf_List.append(self)
    def defend(self,oppattackstrength):
        self.stamina = max(0,self.stamina-5)
        self.action_allowed = True
        self.scan()
        wolf = self.wolflist
        self.clearinfo()
        return len(wolf)//5 + self.stamina//25 < randint(0+oppattackstrength,10+oppattackstrength)
    def attack(self):
        if self.action_allowed:
            self.action_allowed = False
            try:
                if self.target.type == "sheep" and squarestouching(self,self.target) and self.stamina >= 50:
                    self.stamina -= 25
                    if not self.target.defend(self.strength):
                        self.target.kill()
                        self.target = None
                        self.score += 5
                    else:
                        self.target = None
                        self.stunned = True
                        self.stunnedtime = 0
            except:
                pass #ur mom
    def kill(self):
        Wolf_List.pop(Wolf_List.index(self))

    def upgrade_char(self, next_Upgrade):
        if next_Upgrade == "MS":
            self.max_Speed += .3
        if next_Upgrade == "VR":
            self.viewrange += 10
        if next_Upgrade == "STR":
            self.strength += 1
        if next_Upgrade == "STA":
            self.maxstamina += 25
            self.stamina = self.maxstamina
        if next_Upgrade == "REG":
            self.staminaregen += .5
            self.stamina = self.maxstamina