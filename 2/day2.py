import math

def testValues(one, two):
    input = open("input.txt", "r").read().split(",")
    input[1] = str(one)
    input[2] = str(two)

    for index in range(0, len(input), 4):
        if input[index] == "99":
            break

        values = [int(input[int(input[index+1])]), int(input[int(input[index+2])])]

        result = 0
        if input[index] == "1":
            result = values[0] + values[1]
        if input[index] == "2":
            result = values[0] * values[1]

        input[int(input[index+3])] = str(result)

    return input[0] == "19690720"

for i in range(0, 99):
    for j in range(0, 99):
        if testValues(i, j) == True:
            print(i)
            print(j)