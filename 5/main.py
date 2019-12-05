#!/usr/bin/env python3
import sys
import time
import math

def readInput():
    file = open("input", "r")
    lines = file.readlines()
    return lines

def partTwo( codes ):
    partOne(codes, 5)

def computeOpCode( number ):
    return [number % 100, int(number/100)%10, int(number/1000)%10, int(number/10000)%10]

def partOne(codes, systemID):
    instructionPointer = 0
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
            codes[operandA] = systemID
            instructionPointer += 2
        elif( opCode[0] == 4 ):
            operandA = codes[ instructionPointer + 1 ]
            medium = codes [ operandA ] if not opCode[1] else operandA
            print(medium)
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

def main():
    lines = readInput()
    codes = list( map( lambda x: int(x), lines[0].split(',') ) )
    copyOfCodes = list(codes)
    partOne( codes , 1)
    codes = copyOfCodes
    partTwo( codes )


if __name__ == "__main__":
    main()
