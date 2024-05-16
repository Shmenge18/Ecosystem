#Custom functions for you to use!!!!
from Functions import squarestouching,getdistance,getangle, getclosest
from MainLoop import main, check

#Other imports
from random import randint

#What class you are using
from Bee_Class import Bee

#Possible types - Bee, Sheep, Wolf, Caveman  (Make sure to spell properly starting with a capital letter)
yourtype = "Bee"

class randombee(Bee):
    def __init__(self,x,y,randombee):
        Bee.__init__(self,x,y,randombee)
    def act(self):
        self.direction = 0
        self.speed = 10
        self.move()
#Spawns your animals
def spawnyourcreatures(x,y):
    #All yall none bees just change the name here
    #Adam(x,y)

    #If you are a bee just return your class name like this NO BRACKETS
    return randombee



#Settings for Simulation
hungeron = True

# Spawn the animals randomly, or in quadrants
RandomSpawn = False

# Total tiles: 196
grasses = 100
trees = 35
bushes = 20

#THESE ARE NOT YOUR ANIMALS
sheeps = 10
bees = 10
wolfs = 10
cavemans = 10

if check:
    main()



















































"""#Custom functions for you to use!!!!
from Functions import squarestouching,getdistance,getangle, getclosest
from MainLoop import main, check

#Other imports
from random import randint

#What class you are using
from Bee_Class import Bee

#Possible types - Bee, Sheep, Wolf, Caveman  (Make sure to spell properly starting with a capital letter)
yourtype = "Bee"

class yournamehere(Bee):
    def __init__(self,x,y,yournamerhere):
        Bee.__init__(self,x,y,yournamerhere)
    def act(self):
        print("hie")
        self.speed = .18
        self.direction = 0#randint(0, 360)
        self.move()

#Spawns your animals
def spawnyourcreatures(x,y):
    #Just change the name Here
    #yournamehere(x,y)

    #If you are a bee just return your class name like this NO BRACKETS
    return yournamehere



#Settings for Simulation
hungeron = True

# Spawn the animals randomly, or in quadrants
RandomSpawn = False

# Total tiles: 196
grasses = 150
trees = 35
bushes = 15

#THESE ARE NOT YOUR ANIMALS
sheeps = 10
bees = 10
wolfs = 10
cavemans = 10

if check:
    main()"""