#!/usr/bin/env python3
import sys
import time
import math

combinations = []
overproduction = []

class Combination():
    def __init__(self, value, name):
        self._number = value
        self._name = name
        self._recipe = []

    def addRecipt(self, recipe):
        self._recipe.append(recipe)

def readInput():
    file = open("testinput1", "r")
    lines = file.readlines()
    return lines

def getCombination( name ):
    global combinations
    for combination in combinations:
        if combination._name == name:
            return combination
    return 0


def createCombinations( lines ):
    global combinations
    for line in lines:
        line.rstrip()
        result = line.split("=>")
        value, name = result[1].split(' ')[:2]
        currentComb = Combination(value, name)
        recipes = result[0].split(',')
        for recipe in recipes:
            value, name = recipe.split(' ')[:2]
            currentComb.addRecipt(Combination( value, name ))

    for comb in combinations:
        print(" ")


def replaceCombinations():
    global combinations
    pass

def partOne():
    currentString = ""
    replaceCombinations()

def main():
    lines = readInput()
    createCombinations( lines )
    partOne()


if __name__ == "__main__":
    main()
