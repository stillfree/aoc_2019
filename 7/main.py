#!/usr/bin/env python3
import sys
import time
import math
import itertools

def readInput():
    file = open("input4", "r")
    lines = file.readlines()
    return lines

class Amplifier():
    def __init__(self, ID):
        self._state = ID
        self._counterHit = False
        self._instructionPointer = 0
        self._output = ""

    def input(self):
        pass

    def compute(self):
        codes = list(copy)
        while(codes[ instructionPointer ] != 99):
            opCode = computeOpCode( codes[ instructionPointer ] )
            if( opCode[0] == 1 ):
                operandA = codes[ instructionPointer + 1 ]
                operandB = codes[ instructionPointer + 2 ]
                pointerResult = codes[ instructionPointer + 3 ]
                valueA = codes[ operandA ] if not opCode[1] else operandA
                valueB = codes[ operandB ] if not opCode[2] else operandB
                result = valueA + valueB
                instructionPointer += 4
                codes[ pointerResult ] = result
            elif( opCode[0] == 2 ):
                operandA = codes[ instructionPointer + 1 ]
                operandB = codes[ instructionPointer + 2 ]
                valueA = codes[ operandA ] if not opCode[1] else operandA
                valueB = codes[ operandB ] if not opCode[2] else operandB
                pointerResult = codes[ instructionPointer + 3 ]
                result = valueA * valueB
                instructionPointer += 4
                codes[ pointerResult ] = result
            elif( opCode[0] == 3 ):
                operandA = codes[ instructionPointer + 1 ]
                codes[operandA] = systemID[systemIDPointer]
                systemIDPointer += 1
                instructionPointer += 2
            elif( opCode[0] == 4 ):
                operandA = codes[ instructionPointer + 1 ]
                medium = codes [ operandA ] if not opCode[1] else operandA
                output += str(medium)
                instructionPointer += 2
            elif( opCode[0] == 5 ):
                operandA = codes[ instructionPointer + 1 ]
                operandB = codes[ instructionPointer + 2 ]
                valueA = operandA if opCode[1] else codes[ operandA ]
                if valueA:
                    instructionPointer = operandB if opCode[2] else codes[ operandB ]
                else:
                    instructionPointer += 3
            elif( opCode[0] == 6 ):
                operandA = codes[ instructionPointer + 1 ]
                operandB = codes[ instructionPointer + 2 ]
                valueA = operandA if opCode[1] else codes[ operandA ]
                if valueA == 0:
                    instructionPointer = operandB if opCode[2] else codes[ operandB ]
                else:
                    instructionPointer += 3
            elif( opCode[0] == 7 ):
                operandA = codes[ instructionPointer + 1 ]
                operandB = codes[ instructionPointer + 2 ]
                operandC = codes[ instructionPointer + 3 ]
                valueA = operandA if opCode[1] else codes[ operandA ]
                valueB = operandB if opCode[2] else codes[ operandB ]
                codes[ operandC ] = 1 if valueA < valueB else 0
                instructionPointer += 4
            elif( opCode[0] == 8 ):
                operandA = codes[ instructionPointer + 1 ]
                operandB = codes[ instructionPointer + 2 ]
                operandC = codes[ instructionPointer + 3 ]
                valueA = operandA if opCode[1] else codes[ operandA ]
                valueB = operandB if opCode[2] else codes[ operandB ]
                codes[ operandC ] = 1 if valueA == valueB else 0
                instructionPointer += 4
        return int(output)


def partTwo( codes ):
    partOne(codes, 5)


def generateVariants(copyLeft, copyCurrent, counter, liste):
    laenge = len(copyLeft)
    if laenge != 0:
        for i in range(0, laenge):
            left = copyLeft.copy()
            current = copyCurrent.copy()
            output = left[i]
            left.pop(i)
            current.append(output)
            #print(left, copyLeft, output, current, counter)
            generateVariants( left, current, counter + 1, liste)
    else:
        liste.append(list(copyCurrent))

def foo(array, num):
    yield from itertools.product(*([array] * num))

def computeOpCode( number ):
    return [number % 100, int(number/100)%10, int(number/1000)%10, int(number/10000)%10]

def partOne(copy, systemID):
    instructionPointer = 0
    systemIDPointer = 0
    output = ""
    codes = list(copy)
    while(codes[ instructionPointer ] != 99):
        opCode = computeOpCode( codes[ instructionPointer ] )
        if( opCode[0] == 1 ):
            operandA = codes[ instructionPointer + 1 ]
            operandB = codes[ instructionPointer + 2 ]
            pointerResult = codes[ instructionPointer + 3 ]
            valueA = codes[ operandA ] if not opCode[1] else operandA
            valueB = codes[ operandB ] if not opCode[2] else operandB
            result = valueA + valueB
            instructionPointer += 4
            codes[ pointerResult ] = result
        elif( opCode[0] == 2 ):
            operandA = codes[ instructionPointer + 1 ]
            operandB = codes[ instructionPointer + 2 ]
            valueA = codes[ operandA ] if not opCode[1] else operandA
            valueB = codes[ operandB ] if not opCode[2] else operandB
            pointerResult = codes[ instructionPointer + 3 ]
            result = valueA * valueB
            instructionPointer += 4
            codes[ pointerResult ] = result
        elif( opCode[0] == 3 ):
            operandA = codes[ instructionPointer + 1 ]
            codes[operandA] = systemID[systemIDPointer]
            systemIDPointer += 1
            instructionPointer += 2
        elif( opCode[0] == 4 ):
            operandA = codes[ instructionPointer + 1 ]
            medium = codes [ operandA ] if not opCode[1] else operandA
            output += str(medium)
            instructionPointer += 2
        elif( opCode[0] == 5 ):
            operandA = codes[ instructionPointer + 1 ]
            operandB = codes[ instructionPointer + 2 ]
            valueA = operandA if opCode[1] else codes[ operandA ]
            if valueA:
                instructionPointer = operandB if opCode[2] else codes[ operandB ]
            else:
                instructionPointer += 3
        elif( opCode[0] == 6 ):
            operandA = codes[ instructionPointer + 1 ]
            operandB = codes[ instructionPointer + 2 ]
            valueA = operandA if opCode[1] else codes[ operandA ]
            if valueA == 0:
                instructionPointer = operandB if opCode[2] else codes[ operandB ]
            else:
                instructionPointer += 3
        elif( opCode[0] == 7 ):
            operandA = codes[ instructionPointer + 1 ]
            operandB = codes[ instructionPointer + 2 ]
            operandC = codes[ instructionPointer + 3 ]
            valueA = operandA if opCode[1] else codes[ operandA ]
            valueB = operandB if opCode[2] else codes[ operandB ]
            codes[ operandC ] = 1 if valueA < valueB else 0
            instructionPointer += 4
        elif( opCode[0] == 8 ):
            operandA = codes[ instructionPointer + 1 ]
            operandB = codes[ instructionPointer + 2 ]
            operandC = codes[ instructionPointer + 3 ]
            valueA = operandA if opCode[1] else codes[ operandA ]
            valueB = operandB if opCode[2] else codes[ operandB ]
            codes[ operandC ] = 1 if valueA == valueB else 0
            instructionPointer += 4
    return int(output)

def main():
    lines = readInput()
    codes = list( map( lambda x: int(x), lines[0].split(',') ) )
    copyOfCodes = list(codes)
    maxValue = 0
    #tem = [0,1,2,3,4]
    #variants = []
    #generateVariants( tem, [], 0, variants)
    #for variant in variants:
        #value = 0
        #for i in range(0,5):
            #value = partOne( codes , [variant[i], value])
        #if value > maxValue:
            #maxValue = value
    #print(maxValue)
    tem2 = [5,6,7,8,9]
    variants = []
    generateVariants( tem2, [], 0, variants)
    maxValue = 0
    codeList = []
    for i in range(0,5):
        codeList.append(codes.copy())
    print(len(codeList))
    for variant in variants:
        value = 0
        for j in range(0, 100):
            for i in range(0, 5):
                value = partOne( codeList[i] , [variant[i], value])
            if value > maxValue:
                maxValue = value

if __name__ == "__main__":
    main()
