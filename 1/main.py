#!/usr/bin/env python3
import sys
import time
import math

def readInput():
    file = open("input", "r")
    lines = file.readlines()
    return lines

def calcFuel( amount ):
    return int(amount / 3) - 2

def partOne( lines ):
    sum = 0
    for line in lines:
        sum += calcFuel( int( line ) )
    return sum

def partTwo( lines ):
    sum = 0
    for line in lines:
        num = calcFuel( int( line ) )
        sum += num
        while(num > 0):
            num = calcFuel( int( num ) )
            if( num > 0 ):
                sum += num
    return sum

def main():
    lines = readInput()
    print( "Part one: " + str( partOne( lines ) ) )
    print( "Part two: " + str( partTwo( lines ) ) )

if __name__ == "__main__":
    main()
