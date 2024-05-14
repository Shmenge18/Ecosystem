import Plants_Classes as PTypes
import pygame
import random
import time
from Player_Class import Player, Grass_List, Dirt_List, Bush_List, Tree_List, Twig_List
testgrid = []
allplants = []


class PlantCell(Player):
    def __init__(self, topleft, bottomright, tcenter, planttype):
        Player.__init__(self, topleft[0], topleft[1])
        if planttype.type == "tree":
            planttype.x = tcenter[0]
            planttype.y = tcenter[1]
        self.topleft = topleft
        self.bottomright = bottomright
        self.tcenter = tcenter

        self.width = 0
        self.height = 0

        # Dirt
        self.regrowcycle = 0

        # Grass
        self.pollencount = 0
        self.MaxPollen = 0
        self.pollencycle = 0

        # Trees
        self.hashive = False
        self.twigcycle = 0

        # Berry Bushes
        self.berrycycle = 0
        self.HasBerries = 0
        self.MaxBerries = 0

        self.planttype = None
        self.ChangePlant(planttype)
        self.image = pygame.transform.scale(pygame.image.load(self.planttype.image), (50, 50))
        # print(f"I AM A PLANT SQUARE WITH THE CENTER OF {tcenter}, I AM NUMBER {len(allplants) + 1}")

    def ChangePlant(self, plant):
        if self.planttype:
            if self.planttype.type == "dirt":
                Dirt_List.remove(self)
            elif self.planttype.type == "grass":
                Grass_List.remove(self)
            elif self.planttype.type == "bush":
                Bush_List.remove(self)
            elif self.planttype.type == "tree":
                Tree_List.remove(self)

        self.planttype = plant
        if plant.type == "dirt":
            Dirt_List.append(self)

        elif plant.type == "grass":
            self.MaxPollen = 3
            self.pollencount = self.MaxPollen
            Grass_List.append(self)

        elif plant.type == "bush":
            if random.randint(0, 1) == 0:
                self.planttype.AddBerries()
                self.MaxBerries = 1
                self.HasBerries = self.MaxBerries
            Bush_List.append(self)
            
        elif plant.type == "tree":
            Tree_List.append(self)

    def kill(self):
        if self.planttype.type == "grass":
            self.ChangePlant(PTypes.Dirt())
            self.image = pygame.transform.scale(pygame.image.load(self.planttype.image), (50, 50))
        elif self.planttype.type == "bush":
            if self.HasBerries > 0:
                self.HasBerries -= 1
            elif self.HasBerries <= 0:
                self.planttype.RemoveBerries()
                self.image = pygame.transform.scale(pygame.image.load(self.planttype.image), (50, 50))
            else:
                self.berrycycle = 0

    def regrow(self):
        self.ChangePlant(PTypes.Grass())
        self.image = pygame.transform.scale(pygame.image.load(self.planttype.image), (50, 50))

    def pollinate(self):
        if self.pollencount > 0 and self.planttype.type == "grass":
            self.pollencount -= 1
            return True
        else:
            return False

    def act(self):
        if self.planttype.type == "dirt":
            if self.regrowcycle >= 200 and random.randint(1, 80) == 1:
                self.regrowcycle = 0
                self.regrow()
            else:
                self.regrowcycle += 1
        elif self.planttype.type == "grass":
            pass
            if self.pollencycle >= 250:
                if self.pollencount < self.MaxPollen:
                    self.pollencount += 1
                self.pollencycle = 0
            else:
                self.pollencycle += 1
            # self.pollencount = self.planttype.pollencount

        elif self.planttype.type == "tree":
            if self.twigcycle >= 200 and len(Twig_List) < 60:
                if random.randint(1, 100) < 60:
                    self.planttype.DropTwigs()
                self.twigcycle = 0
            else:
                self.twigcycle += random.randint(1, 3)

        elif self.planttype.type == "bush":
            if self.berrycycle >= 150:
                if random.randint(1, 100) < 60:
                    if self.HasBerries < self.MaxBerries:
                        self.HasBerries += 1
                    self.planttype.AddBerries()
                    self.image = pygame.transform.scale(pygame.image.load(self.planttype.image), (50, 50))
                self.berrycycle = 0
            else:
                self.berrycycle += 1


def CreatePlantGrid(cellX, cellY, screen, plantgen, visualize):
    def VisualizeGrid(cellX, cellY, screen):

        # Draws the vertical grid lines
        for i in range(screen.get_width() // cellX + 1):
            start = (i * cellX, 0)
            end = (i * cellX, screen.get_height())
            pygame.draw.line(screen, (100, 160, 60), start, end)
            # Draws dots on each vertex of the grid
            for b in range((screen.get_height() // cellY) + 1):
                testgrid.append((i * cellX, b * cellY))
                pygame.draw.circle(screen, (200, 50, 50), testgrid[-1], 3)
        # Draws the horizontal grid lines
        for i in range(screen.get_height() // cellY):
            start = (0, i * cellY)
            end = (screen.get_width(), i * cellY)
            pygame.draw.line(screen, (100, 160, 60), start, end)
    if visualize:
        VisualizeGrid(cellX, cellY, screen)

    perplant = []
    totalplants = 0
    totaltrees = plantgen["tree"]
    for v in plantgen.values():
        totalplants += v
    for p in range(totalplants):
        if plantgen["grass"] > 0:
            perplant.append(PTypes.Grass())
            plantgen["grass"] -= 1
        elif plantgen["tree"] > 0:
            perplant.append(PTypes.Tree(0, 0))
            plantgen["tree"] -= 1
        elif plantgen["bush"] > 0:
            perplant.append(PTypes.Bush())
            plantgen["bush"] -= 1
    for n in range((screen.get_width() // cellX) * (screen.get_height() // cellY) - totalplants):
        perplant.append(PTypes.Dirt())
    random.shuffle(perplant)
    for a in range((screen.get_width() // cellX) * (screen.get_height() // cellY)):
        topleft = (a * cellX % (screen.get_width()), a // 14 * cellY % (screen.get_height()))
        bottomright = ((a * cellX) % (screen.get_width()) + 50, (a // 14 * cellY + 50) % (screen.get_height() + 50))
        cellcenter = ((topleft[0] + bottomright[0]) / 2, (topleft[1] + bottomright[1]) / 2)
        allplants.append(PlantCell(topleft, bottomright, cellcenter, perplant[a]))
    hivechance = 1
    for p in allplants:
        if p.planttype.type == "tree":
            if random.randint(hivechance, totaltrees) == totaltrees:
                p.planttype.AddHive()
                break
            else:
                hivechance += 1

    return allplants
