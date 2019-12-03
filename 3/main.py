#!/usr/bin/env python3
import sys
import time
import numpy as np
closestDistance = 1000000
freespot = 0
collisionCounter = 0
closestPoint = [ 0, 0 ]
gridSize = 25000
steps = 0
intersections = []
grid = np.zeros((gridSize, gridSize, 2), dtype=np.int32)
print("init grid")

middle = []

def readInput():
    file = open("input", "r")
    lines = file.readlines()
    return lines

def manhattenDistance(A , B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

def placeLine(start, instruction, lineNumber):
    global closestDistance, closestPoint, middle, grid, steps
    X = 0
    Y = 0
    if(instruction[0] == "U"):
        x = start[0]
        X = x
        for y in range(start[1], start[1] + instruction[1] + 1):
            currentValue = grid[x][y][0]
            newValue = check(currentValue, lineNumber)
            if newValue == 98:
                saveIntersection(x, y)
                distance = manhattenDistance(middle, [x, y])
                if ( closestDistance > distance ):
                    closestDistance = distance
                    closestPoint = [ x, y ]
            grid[x][y][0] = newValue
            grid[x][y][1] = steps
            Y = y
            steps += 1
    elif(instruction[0] == "D"):
        x = start[0]
        X = x
        for y in range(start[1], start[1] - instruction[1] -1, -1):
            currentValue = grid[x][y][0]
            newValue = check(currentValue, lineNumber)
            if newValue == 98:
                saveIntersection(x, y)
                distance = manhattenDistance(middle, [x, y])
                if ( closestDistance > distance ):
                    closestDistance = distance
                    closestPoint = [ x, y ]
            grid[x][y][0] = newValue
            grid[x][y][1] = steps
            Y = y
            steps += 1
    elif(instruction[0] == "R"):
        y = start[1]
        Y = y
        for x in range(start[0], start[0] + instruction[1]+1):
            currentValue = grid[x][y][0]
            newValue = check(currentValue, lineNumber)
            if newValue == 98:
                saveIntersection(x, y)
                distance = manhattenDistance(middle, [x, y])
                if ( closestDistance > distance ):
                    closestDistance = distance
                    closestPoint = [ x, y ]
            grid[x][y][0] = newValue
            grid[x][y][1] = steps
            steps += 1
            X = x
    elif(instruction[0] == "L"):
        y = start[1]
        Y = y
        for x in range(start[0], start[0] - instruction[1]-1, -1):
            currentValue = grid[x][y][0]
            newValue = check(currentValue, lineNumber)
            if newValue == 98:
                saveIntersection(x, y)
                distance = manhattenDistance(middle, [x, y])
                if ( closestDistance > distance ):
                    closestDistance = distance
                    closestPoint = [ x, y ]
            grid[x][y][0] = newValue
            grid[x][y][1] = steps
            X = x
            steps += 1
    return [X, Y]

def check(value, lineNumber):
    global freespot
    global collisionCounter
    if( value == lineNumber):
        return lineNumber
    elif(value == 99):
        #middle
        return 99
    elif(value == 0):
        #freespot
        freespot += 1
        return lineNumber
    elif(value != lineNumber):
        # Collision
        collisionCounter += 1
        return 98

def partOne(lines):
    global closestDistance, closestPoint, middle, grid, steps
    closestDistance = 1000000
    closestPoint = [ 0, 0 ]
    middle = [ int(gridSize/2), int(gridSize/2) ]
    grid[middle[0]][middle[1]][0] = 99
    grid[middle[0]][middle[1]][1] = 0
    lineNumber = 1
    counter = 0
    for line in lines:
        instructions = list( map( lambda x: [ x[0:1], int(x[1:]) ], line.split(',') ) )
        currentPointer = middle
        steps = 0
        for instruction in instructions:
            currentPointer = placeLine( currentPointer,
                                        instruction,
                                        lineNumber,
                                        )
            steps -= 1

        lineNumber += 1
    print("PartOne:" + str(closestDistance))

def saveIntersection(x, y):
    global intersections, steps, grid
    #print(steps, grid[x][y][1], grid[x][y][1] + steps, x, y)
    for intersection in intersections:
        if (intersection[1] == x and intersection[2] == y):
            return
    intersections.append([grid[x][y][1] + steps, x, y])

def partTwo():
    global intersections
    minimum = 10000
    sort = sorted(intersections, key=lambda x: x[0])
    print("PartTwo:" + str(sort[0][0]))

def main():
    lines = readInput()
    partOne(lines)
    partTwo()

if __name__ == "__main__":
    main()
