# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:42:16 2021

@author: Eduard.Krutitsky
"""
import numpy as np

x="""1,1,1,2,1,1,2,1,1,1,5,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,4,1
,1,1,1,3,1,1,3,1,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,1,1,5,5,2,5,
1,1,2,1,1,1,1,3,4,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,4,1,1,1,
1,1,5,1,2,4,1,1,1,1,1,3,3,2,1,1,4,1,1,5,5,1,1,1,1,1,2,5,1,4,1,
1,1,1,1,1,2,1,1,5,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,4,3,1,1,3,1,3,1,4,1,5,4,1,1,2,1,1,5,1,1,1,1,1,5,1,
1,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,1,1,5,4,1,2,1,1,1,1,1,1,1,1,
1,1,1,3,1,1,1,1,1,1,1,1,1,1,4,1,1,1,2,1,4,1,1,1,1,1,1,1,1,1,4,
2,1,2,1,1,4,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,3,2,1,4,1,5,1,1,1,4,
5,1,1,1,1,1,1,5,1,1,5,1,2,1,1,2,4,1,1,2,1,5,5,3"""


fl = np.array(x.split(","))


def initFishGroups(fl):
    x = np.zeros(9,int)
    for f in fl:
        x[int(f)] += 1
    return x

x = initFishGroups(fl)

#Using np.int64 to have large enough numbers to prevent overflow
def updateFishGroups(fg):
    newArr = np.zeros(9,np.int64)
    for i in range(0, len(newArr)):
        if i == 0:
            newArr[8] += fg[i]
            newArr[6] += fg[i]
            
        else:
            newArr[i-1] += fg[i]
    return newArr


#Perform the iterations
for i in range(256):
    x = updateFishGroups(x)

print(sum(x))
    
