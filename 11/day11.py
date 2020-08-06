import math
import sys

def fixLength(newLength, fileInput):
    while len(fileInput) <= newLength:
        fileInput.append("0")
    return fileInput

def day9(fileInput, index, relativeBase, colorInput):
    takenInput = False
    outputs = []
    while index < len(fileInput):
        if fileInput[index] == "99":
            return fileInput, -1, relativeBase, outputs

        instruction = '%s' % fileInput[index]

        while len(instruction) < 5:
            instruction = "0" + instruction
        opcode = instruction[len(instruction)-2:]
        
        if opcode == "1" or opcode == "01":
            if instruction[2] == "0":
                index1 = int(fileInput[index+1])
            elif instruction[2] == "1":
                index1 = index+1
            elif instruction[2] == "2":
                index1 = int(fileInput[index+1]) + relativeBase
            if instruction[1] == "0":
                index2 = int(fileInput[index+2])
            elif instruction[1] == "1":
                index2 = index+2
            elif instruction[1] == "2":
                index2 = int(fileInput[index+2]) + relativeBase
            if instruction[0] == "0":
                index3 = int(fileInput[index+3])
            elif instruction[0] == "1":
                index3 = index+3
            elif instruction[0] == "2":
                index3 = int(fileInput[index+3]) + relativeBase

            if index1 >= len(fileInput):
                fileInput = fixLength(index1, fileInput)
            if index2 >= len(fileInput):
                fileInput = fixLength(index2, fileInput)
            if index3 >= len(fileInput):
                fileInput = fixLength(index3, fileInput)

            values = [int(fileInput[index1]), int(fileInput[index2])]
            result = values[0] + values[1]
            fileInput[index3] = str(result)
            index += 4
        elif opcode == "2" or opcode == "02":
            if instruction[2] == "0":
                index1 = int(fileInput[index+1])
            elif instruction[2] == "1":
                index1 = index+1
            elif instruction[2] == "2":
                index1 = int(fileInput[index+1]) + relativeBase
            if instruction[1] == "0":
                index2 = int(fileInput[index+2])
            elif instruction[1] == "1":
                index2 = index+2
            elif instruction[1] == "2":
                index2 = int(fileInput[index+2]) + relativeBase
            if instruction[0] == "0":
                index3 = int(fileInput[index+3])
            elif instruction[0] == "1":
                index3 = index+3
            elif instruction[0] == "2":
                index3 = int(fileInput[index+3]) + relativeBase

            if index1 >= len(fileInput):
                fileInput = fixLength(index1, fileInput)
            if index2 >= len(fileInput):
                fileInput = fixLength(index2, fileInput)
            if index3 >= len(fileInput):
                fileInput = fixLength(index3, fileInput)

            values = [int(fileInput[index1]), int(fileInput[index2])]
            result = values[0] * values[1]
            fileInput[index3] = str(result)
            index += 4
        elif opcode == "3" or opcode == "03":
            if instruction[2] == "0":
                index1 = int(fileInput[index+1])
            elif instruction[2] == "1":
                index1 = index+1
            elif instruction[2] == "2":
                index1 = int(fileInput[index+1]) + relativeBase

            if index1 >= len(fileInput):
                fileInput = fixLength(index1, fileInput)

            #userInput = input("enter user Input:")
            if takenInput:
                return fileInput, index, relativeBase, outputs

            takenInput = True
            userInput = str(colorInput)
            fileInput[index1] = userInput
            index += 2
        elif opcode == "4" or opcode == "04":
            if instruction[2] == "0":
                index1 = int(fileInput[index+1])
            elif instruction[2] == "1":
                index1 = index+1
            elif instruction[2] == "2":
                index1 = int(fileInput[index+1]) + relativeBase

            if index1 >= len(fileInput):
                fileInput = fixLength(index1, fileInput)
            
            #print(int(fileInput[index1]))
            outputs.append(int(fileInput[index1]))
            index += 2
        elif opcode == "5" or opcode == "05":
            if instruction[2] == "0":
                index1 = int(fileInput[index+1])
            elif instruction[2] == "1":
                index1 = index+1
            elif instruction[2] == "2":
                index1 = int(fileInput[index+1]) + relativeBase
            if instruction[1] == "0":
                index2 = int(fileInput[index+2])
            elif instruction[1] == "1":
                index2 = index+2
            elif instruction[1] == "2":
                index2 = int(fileInput[index+2]) + relativeBase

            if index1 >= len(fileInput):
                fileInput = fixLength(index1, fileInput)
            if index2 >= len(fileInput):
                fileInput = fixLength(index2, fileInput)
            
            if fileInput[index1] != "0":
                index = int(fileInput[index2])
            else:
                index += 3
        elif opcode == "6" or opcode == "06":
            if instruction[2] == "0":
                index1 = int(fileInput[index+1])
            elif instruction[2] == "1":
                index1 = index+1
            elif instruction[2] == "2":
                index1 = int(fileInput[index+1]) + relativeBase
            if instruction[1] == "0":
                index2 = int(fileInput[index+2])
            elif instruction[1] == "1":
                index2 = index+2
            elif instruction[1] == "2":
                index2 = int(fileInput[index+2]) + relativeBase

            if index1 >= len(fileInput):
                fileInput = fixLength(index1, fileInput)
            if index2 >= len(fileInput):
                fileInput = fixLength(index2, fileInput)
            
            if fileInput[index1] == "0":
                index = int(fileInput[index2])
            else:
                index += 3
        elif opcode == "7" or opcode == "07":
            if instruction[2] == "0":
                index1 = int(fileInput[index+1])
            elif instruction[2] == "1":
                index1 = index+1
            elif instruction[2] == "2":
                index1 = int(fileInput[index+1]) + relativeBase
            if instruction[1] == "0":
                index2 = int(fileInput[index+2])
            elif instruction[1] == "1":
                index2 = index+2
            elif instruction[1] == "2":
                index2 = int(fileInput[index+2]) + relativeBase
            if instruction[0] == "0":
                index3 = int(fileInput[index+3])
            elif instruction[0] == "1":
                index3 = index+3
            elif instruction[0] == "2":
                index3 = int(fileInput[index+3]) + relativeBase

            if index1 >= len(fileInput):
                fileInput = fixLength(index1, fileInput)
            if index2 >= len(fileInput):
                fileInput = fixLength(index2, fileInput)
            if index3 >= len(fileInput):
                fileInput = fixLength(index3, fileInput)

            if int(fileInput[index1]) < int(fileInput[index2]):
                fileInput[int(index3)] = "1"
            else:
                fileInput[int(index3)] = "0"
            index += 4
        elif opcode == "8" or opcode == "08":
            if instruction[2] == "0":
                index1 = int(fileInput[index+1])
            elif instruction[2] == "1":
                index1 = index+1
            elif instruction[2] == "2":
                index1 = int(fileInput[index+1]) + relativeBase
            if instruction[1] == "0":
                index2 = int(fileInput[index+2])
            elif instruction[1] == "1":
                index2 = index+2
            elif instruction[1] == "2":
                index2 = int(fileInput[index+2]) + relativeBase
            if instruction[0] == "0":
                index3 = int(fileInput[index+3])
            elif instruction[0] == "1":
                index3 = index+3
            elif instruction[0] == "2":
                index3 = int(fileInput[index+3]) + relativeBase

            if index1 >= len(fileInput):
                fileInput = fixLength(index1, fileInput)
            if index2 >= len(fileInput):
                fileInput = fixLength(index2, fileInput)
            if index3 >= len(fileInput):
                fileInput = fixLength(index3, fileInput)

            if int(fileInput[index1]) == int(fileInput[index2]):
                fileInput[int(index3)] = "1"
            else:
                fileInput[int(index3)] = "0"
            index += 4
        elif opcode == "9" or opcode == "09":
            if instruction[2] == "0":
                index1 = int(fileInput[index+1])
            elif instruction[2] == "1":
                index1 = index+1
            elif instruction[2] == "2":
                index1 = int(fileInput[index+1]) + relativeBase

            if index1 >= len(fileInput):
                fileInput = fixLength(index1, fileInput)
            
            relativeBase += int(fileInput[index1])
            index += 2

#up, right, down, left --- 0, 1, 2, 3
def getNewDirection(currentDirection, turnValue):
    if turnValue == 0:
        currentDirection = (currentDirection - 1) % 4
    else:
        currentDirection = (currentDirection + 1) % 4
    return currentDirection

def moveOneSpace(currentPosition, currentDirection):
    if currentDirection == 0:
        currentPosition = (currentPosition[0], currentPosition[1] + 1)
    if currentDirection == 1:
        currentPosition = (currentPosition[0] + 1, currentPosition[1])
    if currentDirection == 2:
        currentPosition  = (currentPosition[0], currentPosition[1] - 1)
    if currentDirection == 3:
        currentPosition = (currentPosition[0] - 1, currentPosition[1])
    return currentPosition

currentState = open("input.txt", "r").read().split(",")
index = 0
relativeBase = 0

currentPosition = (0,0)
currentDirection = 0
mapPositionToColor = {}

mapPositionToColor[currentPosition] = 1

while index != -1:
    if currentPosition in mapPositionToColor:
        colorInput = mapPositionToColor[currentPosition]
    else:
        colorInput = 0
    currentState, index, relativeBase, results = day9(currentState, index, relativeBase, colorInput)

    if index == -1:
        break

    mapPositionToColor[currentPosition] = int(results[0])

    currentDirection = getNewDirection(currentDirection, results[1])
    currentPosition = moveOneSpace(currentPosition, currentDirection)

minX = None
minY = None
maxX = None
maxY = None

for position in mapPositionToColor.keys():
    if minX is None or position[0] < minX:
        minX = position[0]
    if maxX is None or position[0] > maxX:
        maxX = position[0]
    if minY is None or position[1] < minY:
        minY = position[1]
    if maxY is None or position[1] > maxY:
        maxY = position[1]
# print(minX)
# print(minY)
# print(maxX)
# print(maxY)

x = minX
y = maxY
while y >= minY:
    x = minX
    while x <= maxX:
        value = "."
        if (x,y) in mapPositionToColor:
            if mapPositionToColor[(x,y)] == 1:
                value = "#"
        sys.stdout.write(value)
        x += 1
    sys.stdout.write("\n")
    y -= 1