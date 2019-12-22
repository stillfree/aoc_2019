#!/usr/bin/env python3
import sys
import time
import math

def readInput():
    file = open("input", "r")
    lines = file.readlines()
    return lines


def partOne(lines):
    temp = 25 * 6
    imageCounter = []
    image = []
    for i in range(0, 100):
        tempList = []
        for j in range(0, 3):
            tempList.append(0)
        imageCounter.append(tempList)
    for i in range(0, 6):
        tempList = []
        for j in range(0, 25):
            tempList.append(-1)
        image.append(tempList)

    counter = 0
    index = 0
    lineIndex = 0
    for number in lines[0].rstrip():
        number = int(number)
        tempIndex = counter % 25
        imageCounter[index][number] += 1
        currentPixel = image[lineIndex][tempIndex]
        if(currentPixel == -1 or currentPixel == 2):
            image[lineIndex][tempIndex] = number
        counter += 1
        index = int(counter/temp)
        lineIndex = int(counter/ 25) % 6
    minValue = 150
    minIndex = 0
    for i in range(0, len(imageCounter)):
        if( minValue > imageCounter[i][0]):
            minValue = imageCounter[i][0]
            minIndex = i
    print("Part one: ", imageCounter[minIndex][1]* imageCounter[minIndex][2])
    return image

def main():
    lines = readInput()
    image = partOne(lines)
    for line in image:
        print(line)


if __name__ == "__main__":
    main()
