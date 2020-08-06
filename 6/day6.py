import math

fileInput = open("input.txt", "r").readlines()

orbits = {}
for line in fileInput:
    parts = line.replace("\n", "").split(")")
    orbits[parts[1]] = parts[0]

# count = 0
# for key in orbits.keys():
#     currentKey = key
#     while currentKey in orbits:
#         currentKey = orbits[currentKey]
#         count += 1

# print(count)

youList = []
youKey = "YOU"
while youKey in orbits:
    youKey = orbits[youKey]
    youList.append(youKey)

sanList = []
sanKey = "SAN"
while sanKey in orbits:
    sanKey = orbits[sanKey]
    sanList.append(sanKey)

for i in range(len(youList)):
    for j in range(len(sanList)):
        if youList[i] == sanList[j]:
            print(i + j)
