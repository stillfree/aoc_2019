#!/usr/bin/env python3
import sys
import time
import math

def readInput():
    file = open("input", "r")
    lines = file.readlines()
    return lines

def partTwo( codes ):
    memoryCopy = codes
    for i in range(100):
        for j in range(100):
            codes = list( memoryCopy )
            codes[1] = i
            codes[2] = j
            partOne(codes)
            if( codes[0] == 19690720):
                print(i , j)
                return


def partOne(codes):
    instructionPointer = 0
    while(codes[ instructionPointer ] != 99):
        opCode = codes[ instructionPointer ]
        if( opCode == 1 ):
            pointerA = codes[ instructionPointer + 1 ]
            pointerB = codes[ instructionPointer + 2 ]
            pointerResult = codes[ instructionPointer + 3 ]
            valueA = codes[ pointerA ]
            valueB = codes[ pointerB ]
            result = valueA + valueB
            instructionPointer += 4
            codes[ pointerResult ] = result
        elif( opCode == 2 ):
            pointerA = codes[ instructionPointer + 1 ]
            pointerB = codes[ instructionPointer + 2 ]
            pointerResult = codes[ instructionPointer + 3 ]
            valueA = codes[ pointerA ]
            valueB = codes[ pointerB ]
            result = valueA * valueB
            instructionPointer += 4
            codes[ pointerResult ] = result

def main():
    lines = readInput()
    codes = list( map( lambda x: int(x), lines[0].split(',') ) )
    partTwo( codes )


if __name__ == "__main__":
    main()
