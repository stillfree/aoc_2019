#!/usr/bin/env python3
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import itertools
from amplifier import Amplifier

placesVisited = []
whiteTiles = []
position = (0, 0)
direction = 0

def readInput():
    file = open("input", "r")
    lines = file.readlines()
    return lines

def partTwo():
    global whiteTiles
    print(whiteTiles)
    print(max(whiteTiles))
    data = []
    for x in range(0,100):
        array = []
        for y in range(0,100):
            if( (x-50,y-50) in whiteTiles):
                array.append(1)
            else:
                array.append(0)
        data.append(array)

    plt.imshow(data, interpolation='nearest')
    plt.show()
    print(data)
    print(len(whiteTiles))

def react(touple):
    global whiteTiles, placesVisited, position, direction
    color = touple[0]
    directionChange = touple[1]

    if color == 1:
        if position not in whiteTiles:
            whiteTiles.append(position)
    elif color == 0:
        if position in whiteTiles:
            whiteTiles.remove(position)

    if directionChange == 0:
        direction -= 1
        if(direction < 0):
            direction = 3
    elif directionChange == 1:
        direction += 1
        direction = direction % 4

    newPosition()
    return 1 if position in whiteTiles else 0

def newPosition():
    global position, direction
    position = list(position)
    if(direction == 0):
        position[1] = position[1] + 1
    elif(direction == 1):
        position[0] = position[0] + 1
    elif(direction == 2):
        position[1] = position[1] - 1
    elif(direction == 3):
        position[0] = position[0] - 1
    position = tuple(position)

def partOne( codes ):
    global whiteTiles, placesVisited, position, direction
    amplifier = Amplifier(1 , codes, 0)
    touple = []
    result = (0, 0)
    counter = 0
    while(result[1] != 99):
        result = amplifier.compute()
        counter += 1
        if(result[1] == 4):
            touple.append(result[0])
            if(len(touple) >= 2):
                amplifier.input(react(touple))
                placesVisited.append(position)
                touple.clear()
    myList = set(placesVisited)
    print("PartOne: ", len(myList), len(placesVisited), counter)

def main():
    lines = readInput()
    codes = list( map( lambda x: int(x), lines[0].split(',') ) )
    for i in range(4000):
        codes.append(0)
    partOne(codes)
    partTwo()

if __name__ == "__main__":
    main()
