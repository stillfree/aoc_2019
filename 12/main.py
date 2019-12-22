#!/usr/bin/env python3
import sys
import time
import math
import numpy as np
import matplotlib.pyplot as plt

moonList = []
combinations = []
comb = {}

class Moon():
    def __init__(self, position):
        self._velocity = [0, 0, 0]
        self._position = position

    def move(self):
        for i in range(3):
            self._position[i] += self._velocity[i]

    def gravity(self, otherMoon):
        for i in range(3):
            if self._position[i] > otherMoon._position[i]:
                self._velocity[i] -= 1
                otherMoon._velocity[i] += 1
            elif self._position[i] < otherMoon._position[i]:
                self._velocity[i] += 1
                otherMoon._velocity[i] -= 1

    def sum(self):
        summeX = 0
        summeY = 0
        for i in range(3):
            summeX += abs(self._position[i])
            summeY += abs(self._velocity[i])
        return summeX * summeY

def readInput():
    file = open("input", "r")
    lines = file.readlines()
    return lines

def calcCent():
    global moonList
    x = 0
    y = 0
    z = 0
    for i in range(3):
        x += moonList[i]._position[0]
        y += moonList[i]._position[1]
        z += moonList[i]._position[2]
    return [ x/4, y/4, z/4 ]

def createMoon( line ):
    global moonList
    moonList.append( Moon( [int(line[0]), int(line[1]), int(line[2]) ] ) )

def stepMoons():
    global moonList
    for combination in combinations:
        combination[0].gravity(combination[1])

    for moon in moonList:
        moon.move()

def createCombinations():
    global combinations
    combinations.append([moonList[0], moonList[1]])
    combinations.append([moonList[0], moonList[2]])
    combinations.append([moonList[0], moonList[3]])
    combinations.append([moonList[1], moonList[2]])
    combinations.append([moonList[1], moonList[3]])
    combinations.append([moonList[2], moonList[3]])

def saveCombination( steps ):
    global comb, moonList
    A = ""
    B = ""
    for i in range(3):
        for j in range(3):
            A += str(moonList[i]._velocity[j])
            B += str(moonList[i]._position[j])

    A = A.replace('-','Z')
    B = B.replace('-','Z')
    if A in comb and comb[A] == B:
        print("Steps: ", steps)
        print(A)
        print(B)
        print(comb[A])
        exit()
    else:
        comb[A] = B

def partOne( lines ):
    global moonList
    for line in lines:
        createMoon( line )
    #for moon in moonList:
        #print(moon._position, moon._velocity)
    createCombinations()
    i = 1
    while(1):
        stepMoons()
        saveCombination( i )
        #printMoons()
        time.sleep(0.5)
        i += 1
    sum = 0
    for moon in moonList:
        #print(moon._position, moon._velocity)
        sum += moon.sum()
    print("The overall Sum is: ", sum)

def printMoons():
    global moonList
    plt.axis([0, 10, 0, 1])

    for i in range(10):
        y = np.random.random()
        plt.scatter(i, y)
        plt.pause(0.05)

    plt.show()
    #min =

def main():
    lines = readInput()
    lines = list( map( lambda x: x.rstrip().rsplit(','), lines) )
    partOne( lines )
    return
    partTwo( lines )

if __name__ == "__main__":
    main()
