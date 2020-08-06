import math

fileInput = open("input.txt", "r").read().split(",")

def fixLength(newLength, fileInput):
    while len(fileInput) <= newLength:
        fileInput.append("0")
    return fileInput

index = 0
relativeBase = 0
while index < len(fileInput):
    if fileInput[index] == "99":
        break

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

        userInput = input("enter user Input:")
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
        
        print(int(fileInput[index1]))
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