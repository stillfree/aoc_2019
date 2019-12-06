#!/usr/bin/env python3
import sys
import time
import collections as cl

def readInput():
    file = open("input", "r")
    lines = file.readlines()
    return lines

def partOne(Tree, currentElement, currentCounter):
    if currentElement in Tree:
        sum = currentCounter
        for element in Tree[currentElement]:
            sum += partOne(Tree, element, currentCounter + 1)
        return sum
    else:
        return currentCounter

def partTwo(Tree):
    jumps = []
    element = "YOU"
    while( element != "COM" ):
        element = Tree[element][0]
        jumps.append(element)
    element = "SAN"
    firstElement = Tree[element][0]
    while( element != "COM" ):
        element = Tree[element][0]
        if(element in jumps):
            del jumps[jumps.index(element)+1:jumps.index(firstElement)+1]
            break
        jumps.append(element)
    return(len(jumps))

def main():
    lines = list( map( lambda x: x.rstrip().split(')'), readInput()) )
    Tree = {}
    revertTree = {}
    for element in lines:
        if element[0] in Tree:
            Tree[element[0]].append(element[1])
        else:
            Tree[element[0]] = [element[1]]
        if element[1] in revertTree:
            revertTree[element[1]].append(element[0])
        else:
            revertTree[element[1]] = [element[0]]
    print("PartOne: " + str(partOne(Tree, "COM", 0)))
    print("PartTwo: " + str(partTwo(revertTree)))

if __name__ == "__main__":
    main()

