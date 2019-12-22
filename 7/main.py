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
    variants = []
    generateVariants( [5,6,7,8,9], [], 0, variants)
    maxValue = 0
    for variant in variants:
        AmplifierList = []
        for i in range(0, 5):
            AmplifierList.append(Amplifier(variant[i], codes))
        result = [0, 0]
        last = False
        while(not last):
            for i in range(0, len(AmplifierList)):
                amplifier = AmplifierList[i]
                amplifier.input(result[0])
                result = amplifier.compute()
                if( i == 4):
                    if (result[1] == 99):
                        last = True
                    else:
                        if result[0] > maxValue:
                            maxValue = result[0]
    print("PartTwo: ", maxValue)

def partOne( codes ):
    variants = []
    generateVariants( [0,1,2,3,4], [], 0, variants)
    maxValue = 0
    for variant in variants:
        result = [0, 0]
        for i in range(0, 5):
            amplifier = Amplifier(variant[i], codes)
            amplifier.input(result[0])
            result = amplifier.compute()
        if(result[0] > maxValue):
            maxValue = result[0]
    print("PartOne: ", maxValue)

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
    partOne(codes)
    partTwo(codes)

if __name__ == "__main__":
    main()
