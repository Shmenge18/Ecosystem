#Functions
from math import sqrt, atan, degrees, sin ,pi, cos
def squarestouching(object1,object2):
    if type(object2) == type(None):
        return False
    else:
        return(abs(object1.x-object2.x) < (object1.width/2+object2.width/2) and abs(object1.y-object2.y) < (object1.height/2+object2.height/2))
#Gets the distance between two objects
def getdistance(object1, object2):
    if type(object2) == type(None):
        return 0
    else:
        return sqrt((object2.x-object1.x)**2+(object2.y-object1.y)**2)

#Optimze this someone please its horrible it gets angle supposed too its so bad
def getangle(start,target):
    #Gets the related acute angle
    if type(target) == type(None) or target.y-start.y == target.x-start.x == 0:
        return 0
    if target.y-start.y == 0:
        return 45
    if target.x-start.x == 0:
        return 90 + abs(target.y-start.y)/(target.y-start.y)*90
    else:
        #Gets the dirrections of the x and y
        xsign = abs(target.x-start.x)/(target.x-start.x)
        ysign = abs(target.y-start.y)/(target.y-start.y)

        return (xsign*ysign*-((90+(ysign*90))-degrees(atan(abs((target.x-start.x)/(target.y-start.y))))))
def getclosest(object,ListofObjects):
    closest = None
    distance = 100000
    for x in ListofObjects:
        newdistance = getdistance(object,x)
        if newdistance < distance:
            distance = newdistance
            closest = x
    return closest

