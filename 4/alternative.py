#!/usr/bin/env python3
import sys
import time
import math

min = 234208
max = 765869

def recursive(numberBefore, position, currentNumber, doubleFound):
    global min, max
    if(position > 5):
        if(doubleFound):
            return 1
        return 0

    if(position == 0):
        currentMin = int(str(min)[position])
        currentMax = int(str(max)[position])
        globalMin = currentMin
    else:
        globalMin = int(str(min)[position])
        globalMax = int(str(max)[position])

        currentMax = globalMax if int(currentNumber + "9") > int(str(max)[0:position + 1]) else 9

        currentMin = globalMin if int(currentNumber + str(numberBefore)) < int(str(min)[0:position + 1]) else numberBefore

    sum = 0
    #print( position, numberBefore, globalMin, currentMin, currentMax)
    for i in range( currentMin, currentMax + 1):
        if(i == numberBefore):
            sum += partOne(i, position + 1, currentNumber + str(i), True)
        else:
            sum += partOne(i, position + 1, currentNumber + str(i), doubleFound)
    return sum

def main():
    print(partOne(0, 0, "", False))

if __name__ == "__main__":
    main()
