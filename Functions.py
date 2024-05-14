#Functions
from math import sqrt, atan, degrees, sin ,pi, cos
def squarestouching(object1,object2):
    if type(object2) == type(None):
        return False
    else:
        return(abs(object1.x-object2.x) < (object1.width/2+object2.width/2) and abs(object1.y-object2.y) < (object1.height/2+object2.height/2))
#Gets the distance between two objects
def getdistance(start, target):
    if type(start) != type((0,0)):
        Sx,Sy = start.x, start.y
    else:
        Sx,Sy = start[0], start[1]
    if type(target) != type((0,0)):
        Tx,Ty = target.x, target.y
    else:
        Tx,Ty = target[0], target[1]

    if type(target) == type(None):
        return 0
    else:
        return sqrt((Tx-Sx)**2+(Ty-Sy)**2)

#Optimze this someone please its horrible it gets angle supposed too its so bad
def getangle(start,target):
    if type(start) != type((0,0)):
        Sx,Sy = start.x, start.y
    else:
        Sx,Sy = start[0], start[1]
    if type(target) != type((0,0)):
        Tx,Ty = target.x, target.y
    else:
        Tx,Ty = target[0], target[1]
    #Gets the related acute angle
    if type(target) == type(None) or Ty-Sy == Tx-Sx == 0:
        return 0
    if Ty-Sy == 0:
        return 45
    if Tx-Sx == 0:
        return 90 + abs(Ty-Sy)/(Ty-Sy)*90
    else:
        #Gets the dirrections of the x and y
        xsign = abs(Tx-Sx)/(Tx-Sx)
        ysign = abs(Ty-Sy)/(Ty-Sy)

        return (xsign*ysign*-((90+(ysign*90))-degrees(atan(abs((Tx-Sx)/(Ty-Sy))))))

def getclosest(object,ListofObjects):
    closest = None
    distance = 100000
    for x in ListofObjects:
        newdistance = getdistance(object,x)
        if newdistance < distance:
            distance = newdistance
            closest = x
    return closest
