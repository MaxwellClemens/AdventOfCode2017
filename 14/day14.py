import math

def OreNeeded(fuelToProduce):
    neededValues = {"FUEL": fuelToProduce}
    wastedValues = {}
    while len(neededValues) > 1 or "ORE" not in neededValues:
        currentKeys = set(neededValues.keys())
        for resource in currentKeys:
            if resource == "ORE":
                continue
            numNeeded = neededValues[resource]
            toProduce = equations[resource]

            del neededValues[resource]

            subtractor = 0
            if resource in wastedValues:
                subtractor = wastedValues[resource]
                del wastedValues[resource]

            multiplier = 1
            while toProduce[0] * multiplier < numNeeded - subtractor:
                multiplier += 1
            wasted = 0
            if toProduce[0] * multiplier > numNeeded - subtractor:
                wasted = toProduce[0] * multiplier - (numNeeded - subtractor)
                if resource in wastedValues:
                    wastedValues[resource] += wasted
                else:
                    wastedValues[resource] = wasted
            
            num = 0
            val = None
            for i in range(1, len(toProduce)):
                if i % 2 == 1:
                    num = toProduce[i] * multiplier
                else:
                    val = toProduce[i]

                    if val in neededValues:
                        neededValues[val] += num
                    else:
                        neededValues[val] = num
    return neededValues["ORE"]

fileInput = open("input.txt", "r").readlines()

equations = {}
for line in fileInput:
    parts = line.split("=>")
    produces = parts[1].strip().replace("\n", "").split(" ")
    valueList = [int(produces[0])]

    needed = parts[0].split(",")

    for item in needed:
        pieces = item.strip().split(" ")
        valueList.append(int(pieces[0]))
        valueList.append(pieces[1])

    equations[produces[1]] = valueList

# print(OreNeeded(1))
# result = 0
# count = 2733973
# while result < 1000000000000:
#     result = OreNeeded(count)
#     print(result)
#     print(count)
#     count += 1000

neededValues = {"FUEL": 1}
wastedValues = {}
while len(neededValues) > 1 or "ORE" not in neededValues:
    currentKeys = set(neededValues.keys())
    for resource in currentKeys:
        if resource == "ORE":
            continue
        numNeeded = neededValues[resource]
        toProduce = equations[resource]

        del neededValues[resource]

        subtractor = 0
        if resource in wastedValues:
            subtractor = wastedValues[resource]
            del wastedValues[resource]

        multiplier = 1
        while toProduce[0] * multiplier < numNeeded - subtractor:
            multiplier += 1
        wasted = 0
        if toProduce[0] * multiplier > numNeeded - subtractor:
            wasted = toProduce[0] * multiplier - (numNeeded - subtractor)
            if resource in wastedValues:
                wastedValues[resource] += wasted
            else:
                wastedValues[resource] = wasted
        
        num = 0
        val = None
        for i in range(1, len(toProduce)):
            if i % 2 == 1:
                num = toProduce[i] * multiplier
            else:
                val = toProduce[i]

                if val in neededValues:
                    neededValues[val] += num
                else:
                    neededValues[val] = num
print(neededValues)
print(wastedValues)