import random, pygame

from Player_Class import Player, Grass_List, Tree_List, Obstruction_List, Twig_List, Hive_List
from PlantGrid import PlantCell
from Bee_Class import Hive

class Dirt(PlantCell):
    def __init__(self):
        self.image = "dirt1.png"
        self.type = "dirt"
        # print("new dirt made")


class Grass(PlantCell):
    def __init__(self):
        self.image = "grass1.png"
        self.type = "grass"

        # print("new grass made")



class Tree(PlantCell):
    def __init__(self, x, y):
        Player.__init__(self, x, y)
        self.x = x
        self.y = y
        self.image = "tree1.png"
        self.type = "tree"
        # print("new tree made")

    def AddHive(self,classname):
        Hive(self.x, self.y, classname)


    def FallOver(self):
        # put tree falling over stuff here
        pass

    def DropTwigs(self):
        Twig_List.append(Twig(self.x, self.y))
        # drop sticks
        pass


class Bush(PlantCell):
    def __init__(self):
        self.image = "bush1.png"
        self.type = "bush"

    def AddBerries(self):

        self.image = "bush2.png"

    def RemoveBerries(self):
        self.image = "bush1.png"


class Twig(Player):
    def __init__(self, x, y):
        Player.__init__(self, x, y)
        self.type = "twig"
        self.image = pygame.transform.scale(pygame.image.load("twig.png"), (20, 20))
        self.width = 0
        self.height = 0

    def act(self):
        if self.age > 1000:
            Twig_List.remove(self)
