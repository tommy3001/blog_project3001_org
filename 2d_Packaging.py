__author__ = 'T.Severin'
"""
P = [[1200,1100],[1000,750],[500,0]]
#P = []

L = 1300
x_0=L
D_X = [] #maximal free space, which has to be calculated
print(L)
for x in range(L)[::-1] :
    for indx,item in enumerate(P):
        if x == item[0]:
            D_X.append( x_0 - item[0])
        if x == item[1]:
            x_0 = min(x_0, D_X[indx] + x)

print(D_X)
for indx, item in enumerate(P):
    item[0] = item[0] + D_X[indx]
    item[1] = item[1] + D_X[indx]
print(P)
"""

#for x in range(1200):
#    bin.append([0])
#    for y in range(800):
#       bin[x].append(0)

#print(bin)
from pandas import  *
import numpy as np
EPs = np.array([])
Yx = 0
Yz = 1
Xy = 2
Xz = 3
Zx = 4
Zy = 5
X = 0
Y = 1
Z = 2

items = []



class newBox():
    def __init__(s,size = [0,0,0],pos = [0,0,0]):
        s.size = size
        s.pos = pos

def newPosCheck(Items, newItem, newPos):
    for item in Items:
        if not (newPos[X] > item.pos[X]
                and newPos[X]< (item.pos[X] + item.size[X])
                and newPos[Y] > item.pos[Y]
                and newPos[Y]< (item.pos[Y] + item.size[Y])
                and newPos[Z] > item.pos[Z]
                and newPos[Z]< (item.pos[Z] + item.size[Z])) :
            #position is free

            #check for overlapping
            return True


    return False

def areaCheck(Items, newItem, newPos):
    print("Position OK: ",newPosCheck(Items, newItem, newPos))
    if newPosCheck(Items, newItem, newPos):
        print("newPos ",newPos )
        print("size ",newItem.size)
        for item in Items:
            if not ((newPos[X] <= item.pos[X] + item.size[X]) and (newPos[X] + newItem.size[X] >= item.pos[X])
                and (newPos[Y] <= item.pos[Y] + item.size[Y]) and (newPos[Y] + newItem.size[Y] >= item.pos[Y])
                and (newPos[Z] <= item.pos[Z] + item.size[Z]) and (newPos[Z] + newItem.size[Z] >= item.pos[Z])):
                newItem.pos = newPos
                items.append(newItem)

                return True
        return False
    return False

items.append(newBox(size = [100,150,120], pos = [0,0,0]))
items.append(newBox(size = [100,400,120], pos = [100,0,0]))
test = areaCheck(items,newBox(size = [100,300,120], pos = [0,0,0]), newPos= [100,0,100] )

print(test)