import math

fileInput = open("input.txt", "r").read().split(",")

index = 0
while index < len(fileInput):
    if fileInput[index] == "99":
        break

    instruction = fileInput[index]
    opcode = instruction[len(instruction)-2:]
    
    if opcode == "1" or opcode == "01":
        mode1 = len(instruction) > 2 and instruction[len(instruction)-3] == "1"
        mode2 = len(instruction) > 3 and instruction[len(instruction)-4] == "1"

        index1 = fileInput[index+1] if mode1 else fileInput[int(fileInput[index+1])]
        index2 = fileInput[index+2] if mode2 else fileInput[int(fileInput[index+2])]

        values = [int(index1), int(index2)]
        result = values[0] + values[1]
        fileInput[int(fileInput[index+3])] = str(result)
        index += 4
    elif opcode == "2" or opcode == "02":
        mode1 = len(instruction) > 2 and instruction[len(instruction)-3] == "1"
        mode2 = len(instruction) > 3 and instruction[len(instruction)-4] == "1"

        index1 = fileInput[index+1] if mode1 else fileInput[int(fileInput[index+1])]
        index2 = fileInput[index+2] if mode2 else fileInput[int(fileInput[index+2])]

        values = [int(index1), int(index2)]
        result = values[0] * values[1]
        fileInput[int(fileInput[index+3])] = str(result)
        index += 4
    elif opcode == "3" or opcode == "03":
        userInput = input("enter user Input:")
        fileInput[int(fileInput[index+1])] = userInput
        index += 2
    elif opcode == "4" or opcode == "04":
        mode1 = len(instruction) > 2 and instruction[len(instruction)-3] == "1"
        index1 = fileInput[index+1] if mode1 else fileInput[int(fileInput[index+1])]
        
        print(int(index1))
        index += 2
    elif opcode == "5" or opcode == "05":
        mode1 = len(instruction) > 2 and instruction[len(instruction)-3] == "1"
        mode2 = len(instruction) > 3 and instruction[len(instruction)-4] == "1"

        index1 = fileInput[index+1] if mode1 else fileInput[int(fileInput[index+1])]
        index2 = fileInput[index+2] if mode2 else fileInput[int(fileInput[index+2])]
        
        if index1 != "0":
            index = int(index2)
        else:
            index += 3
    elif opcode == "6" or opcode == "06":
        mode1 = len(instruction) > 2 and instruction[len(instruction)-3] == "1"
        mode2 = len(instruction) > 3 and instruction[len(instruction)-4] == "1"

        index1 = fileInput[index+1] if mode1 else fileInput[int(fileInput[index+1])]
        index2 = fileInput[index+2] if mode2 else fileInput[int(fileInput[index+2])]
        
        if index1 == "0":
            index = int(index2)
        else:
            index += 3
    elif opcode == "7" or opcode == "07":
        mode1 = len(instruction) > 2 and instruction[len(instruction)-3] == "1"
        mode2 = len(instruction) > 3 and instruction[len(instruction)-4] == "1"
        mode3 = len(instruction) > 4 and instruction[len(instruction)-5] == "1"

        index1 = fileInput[index+1] if mode1 else fileInput[int(fileInput[index+1])]
        index2 = fileInput[index+2] if mode2 else fileInput[int(fileInput[index+2])]
        index3 = index+3 if mode3 else fileInput[int(index+3)]

        if int(index1) < int(index2):
            fileInput[int(index3)] = "1"
        else:
            fileInput[int(index3)] = "0"
        index += 4
    elif opcode == "8" or opcode == "08":
        mode1 = len(instruction) > 2 and instruction[len(instruction)-3] == "1"
        mode2 = len(instruction) > 3 and instruction[len(instruction)-4] == "1"
        mode3 = len(instruction) > 4 and instruction[len(instruction)-5] == "1"

        index1 = fileInput[index+1] if mode1 else fileInput[int(fileInput[index+1])]
        index2 = fileInput[index+2] if mode2 else fileInput[int(fileInput[index+2])]
        index3 = index+3 if mode3 else fileInput[int(index+3)]

        if int(index1) == int(index2):
            fileInput[int(index3)] = "1"
        else:
            fileInput[int(index3)] = "0"
        index += 4