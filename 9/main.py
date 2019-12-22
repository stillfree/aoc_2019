#!/usr/bin/env python3
import sys
import time
import math
import itertools
from amplifier import Amplifier

def readInput():
    file = open("input", "r")
    lines = file.readlines()
    return lines

def partTwo( codes ):
    maxValue = 0
    print("PartTwo: ", maxValue)

def partOne( codes ):
    maxValue = 0
    amplifier = Amplifier(2 , codes, 0)
    result = amplifier.compute()
    #print("PartOne: ", concatOutput)#, amplifier._state)

def generateVariants(copyLeft, copyCurrent, counter, resultList):
    laenge = len(copyLeft)
    if laenge != 0:
        for i in range(0, laenge):
            left = copyLeft.copy()
            current = copyCurrent.copy()
            output = left[i]
            left.pop(i)
            current.append(output)
            #print(left, copyLeft, output, current, counter)
            generateVariants( left, current, counter + 1, resultList)
    else:
        resultList.append(list(copyCurrent))
    return resultList

def foo(array, num):
    yield from itertools.product(*([array] * num))

def computeOpCode( number ):
    return [number % 100, int(number/100)%10, int(number/1000)%10, int(number/10000)%10]

def main():
    lines = readInput()
    codes = list( map( lambda x: int(x), lines[0].split(',') ) )
    for i in range(4000):
        codes.append(0)
    partOne(codes)
    return
    partTwo(codes)

if __name__ == "__main__":
    main()
