#!/usr/bin/env python3
import sys
import math
import numpy as np

def readInput():
    file = open("input", "r")
    lines = file.readlines()
    return lines

def turnToList( lines ):
    asteroidList = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if(lines[y][x] == "#"):
                asteroidList.append([x,y])
    return asteroidList

def normalize( asteroidA ):
    product = distance( [0,0], asteroidA)
    return [round(asteroidA[0] / product, 3) , round(asteroidA[1] / product,3)]

def distance( asteroidA, asteroidB ):
    return math.sqrt( pow(asteroidA[0] - asteroidB[0], 2) + pow(asteroidA[1] - asteroidB[1], 2) )

def distanceToMiddle(asteroidB):
    asteroidA = [0, 0]
    return math.sqrt( pow(asteroidA[0] - asteroidB[0], 2) + pow(asteroidA[1] - asteroidB[1], 2) )

def shiftCoordinates(center, asteroidList):
    newastroidList = []
    for asteroid in asteroidList:
        new = [ asteroid[0] - center[0], asteroid[1] - center[1]]
        newastroidList.append(new)
    return newastroidList

def getAngle( startVector, asteroid):
    dot = startVector[0] * asteroid[0] + startVector[1] * asteroid[1]
    det = asteroid[1] * startVector[0] - asteroid[0] * startVector[1]
    return math.degrees(math.atan2(det, dot))

def getNext( vector, asteroidList ):
    minimumAngle =  400
    minimumAsteroid = [0, 0]
    for asteroid in asteroidList:
        angle = getAngle(vector, asteroid)
        if(angle < 0):
            angle = 360 -(angle * -1)
        if angle < minimumAngle and (angle != 0 or vector == [0,-1000]):
            minimumAngle = angle
            minimumAsteroid = asteroid
        elif angle == minimumAngle:
            distanceA = distanceToMiddle(asteroid)
            distanceB = distanceToMiddle(minimumAsteroid)
            if(distanceA < distanceB):
                minimumAsteroid = asteroid
    return minimumAsteroid

def partOne( asteroidList ):
    maxValue = 0
    maxAsteroid = []
    hitList = []
    for asteroid in asteroidList:
        asteroidsLeft = asteroidList.copy()
        asteroidsLeft.remove(asteroid)
        asteroidsLeft = shiftCoordinates( asteroid, asteroidsLeft )
        asteroidsAlreadyHit = []
        for asteroidL in asteroidsLeft:
            normAsteroid = normalize(asteroidL)
            if normAsteroid not in asteroidsAlreadyHit:
                asteroidsAlreadyHit.append(normAsteroid)
        if len(asteroidsAlreadyHit) > maxValue:
            maxValue = len(asteroidsAlreadyHit)
            maxAsteroid = asteroid

    print("PartOne: ", maxValue, maxAsteroid)
    return maxAsteroid

def partTwo( asteroidList, center):
    asteroidList.remove(center)
    asteroidList = shiftCoordinates( center, asteroidList )
    hitCounter = 0
    currentVector = [0, -1000]
    while(hitCounter < 200):
        currentVector = getNext(currentVector, asteroidList)
        asteroidList.remove(currentVector)
        hitCounter += 1
    print("PartTwo: ", (currentVector[0]+ center[0])*100 + (currentVector[1] + center[1]))

def main():
    lines = readInput()
    asteroidList = turnToList( lines )
    center = partOne( asteroidList )
    partTwo( asteroidList, center)

if __name__ == "__main__":
    main()
