#!/usr/bin/env python3
import sys
import time
import math

def readInput():
    file = open("input", "r")
    lines = file.readlines()
    return lines

# [0-9]{amount = 0-4} [doubleBiggerThenFirstNum]{1}[numberBiggerThenDouble]{4 - amount}

def partOne(min, max):
    #bruteForce
    counter = 0
    for i in range(min, max + 1):
        happy = True
        double = False
        tripple = False
        for j in range(1, 6):
            if( str(i)[j-1] > str(i)[j]):
                happy = False
            elif(str(i)[j-1] == str(i)[j]):
                double = True
                if(str(i).count(str(i)[j]) == 2):
                    tripple = True

        if(happy and double and tripple):
            counter += 1
            #print(i)
    #print(counter)

def main():
    min = 234208
    max = 765869
    partOne(min, max)


if __name__ == "__main__":
    main()
