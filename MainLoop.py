import pygame
screen = pygame.display.set_mode([700, 700])
check = True
def main():
    global check
    check = False
    #Pygame import
    import pygame

    #Project Files
    from Player_Class import (Dirt_List,Grass_List,Bush_List, Bee_List,Wolf_List,Sheep_List,Tree_List, Hive_List, Point_List, Caveman_List, Twig_List, firelist)
    from Plants_Classes import Grass, Tree
    from RandomAnimals import randomSheep, randomBee, randomWolf, randomCaveman
    from PlantGrid import CreatePlantGrid
    from Bee_Class import Hive
    from pointclass import point
    from CodeHere import hungeron, grasses, trees, bushes, sheeps, bees, wolfs,cavemans, RandomSpawn, yourtype, spawnyourcreatures

    #Other imports
    from random import randint

    #Pygame and fonts
    pygame.font.init()
    pygame.font.get_init()
    funfont = pygame.font.SysFont("New Roman", 30)

    #Screen dimensions
    screenwidth = 700
    screenheight = 700

    #Innitializes pygame
    # pygame.display.init()
    pygame.display.set_caption('Ecosystem')

    # Set up the drawing window
    screen = pygame.display.set_mode([700, 700])

    plantamounts = {"grass": grasses, "tree": trees, "bush": bushes}
    CreatePlantGrid(50, 50, screen, plantamounts, False)


    if yourtype == "Sheep":
        def randomSheep(x,y):
            spawnyourcreatures(x,y)
    elif yourtype in ["Caveman","Cavemen"]:
        def randomCaveman(x,y):
            spawnyourcreatures(x,y)
    elif yourtype in ["Wolves","Wolf"]:
        def randomWolf(x,y):
            spawnyourcreatures(x,y)





    if RandomSpawn:
        for x in range(0, sheeps):
            randomSheep(randint(10, 690), randint(10, 690))
        for x in range(0, wolfs):
            randomWolf(randint(10, 690), randint(10, 690))
        for x in range(0, cavemans):
            randomCaveman(randint(10, 690), randint(10, 690))
    else:
        for x in range(0,sheeps):
            randomSheep(randint(500,700),randint(500,700))
        for x in range(0,wolfs):
            randomWolf(randint(0,250),randint(0,250))
        for x in range(0,cavemans):
            randomCaveman(randint(0,250),randint(550,700))


    #Main Loop
    running = True
    point(500,500,0)
    while running:
        #Checks if the user closed the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        y = 0

        #Runs for all charcteres as x
        for x in Dirt_List+Grass_List+Tree_List+Bush_List+Twig_List+Sheep_List+Wolf_List+Caveman_List+Bee_List+Hive_List:

            #Varibles that change for all charcters (stunned or not)
            x.stamina = min(x.stamina+x.staminaregen,x.maxstamina)

            if x.stunned:
                if x.stunnedtime >= 15:
                    x.stunned = False
                    x.stunnedtime = 0
                else:
                    x.stunnedtime += 1
                    x.direction = randint(0,360)
                    x.speed = x.max_Speed / 10
                    x.action_allowed = True
                    x.move()
            else:
                    #Lets the charcter act
                x.action_allowed = True
                if x.type == "hive":
                    x.act()
                else:
                    try:
                        x.act()
                    except Exception as e:
                        pass

                    # print(e)
                    # print("YOU SUCK AT PROGRAMMING")
                #Removes the information given by the scan
                x.clearinfo()
            #Displays the charcter
            pygame.draw.rect(screen, x.color, pygame.Rect(x.x-x.width//2, x.y-x.height//2, x.width, x.height))

            # If the grade 11s added their own picture then displays said picture
            if type(x.image) != type(None):
                screen.blit(x.image, pygame.Rect(x.x-x.width//2, x.y-x.height//2, x.width, x.height))
            if x.target not in Dirt_List+Bush_List+Grass_List+Tree_List+Twig_List+Sheep_List+Wolf_List+Caveman_List+Bee_List+Hive_List:
                x.target = None
            if x.age >= 200 and hungeron and x not in Grass_List+Tree_List+Bush_List+Twig_List+Hive_List+Dirt_List:
                x.kill()

            x.tick()
        y = 0
        for x in firelist:

            x.timer = x.timer - 1
            if x.timer == 0:
                x.burnout()
            firewidth = 10
            fireheight = 10
            firecolour = "red"
            pygame.draw.rect(screen, firecolour, pygame.Rect(x.x - firewidth // 2, x.y - fireheight // 2, firewidth, fireheight))
            y = y + 1
        for x in Point_List:
            x.act()
            pygame.draw.rect(screen, (200,255,200), pygame.Rect(x.x - x.width // 2, x.y - x.height // 2, x.width, x.height))
        # print(len(Grass_List) + len(Dirt_List) + len(Tree_List) + len(Bush_List))
        # print(len(Twig_List))
        pygame.time.Clock().tick(30)
        pygame.display.flip()

