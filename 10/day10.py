import math

fileInput = open("input.txt", "r").readlines()

def getAllViewableAstroids(startingAstroid, astroidLocations):
    currentSetOfAngles = {}
    for j, endingAstroid in enumerate(astroidLocations):
        if startingAstroid == endingAstroid:
            continue

        dy = endingAstroid[1] - startingAstroid[1]
        dx = endingAstroid[0] - startingAstroid[0]

        tempAngle = math.atan2(dy, dx)

        angle = (math.degrees(tempAngle) - 270) % 360
        #print(angle)
        #if endingAstroid[0] == 8:
            #print(angle)

        distance = math.sqrt( ((startingAstroid[0]-endingAstroid[0])**2)+((startingAstroid[1] - endingAstroid[1])**2) )

        if angle not in currentSetOfAngles.keys():
            currentSetOfAngles[angle] = [j, distance, endingAstroid[0], endingAstroid[1]]
        else:
            if distance < currentSetOfAngles[angle][1]:
                currentSetOfAngles[angle] = [j, distance, endingAstroid[0], endingAstroid[1]]

    return currentSetOfAngles

def getAstroidsBetweenAngles(astroids, startingAngle, endingAngle):
    result = {}
    for astroid in astroids:
        if astroid >= startingAngle and astroid <= endingAngle:
            result[astroid] = astroids[astroid]
    
    return result

astroidLocations = []
for y, line in enumerate(fileInput):
    line = line.replace("\n","")
    for x, value in enumerate(line):
        if value == "#":
            astroidLocations.append((x,y))

angleOfOtherAstroids = []

for index, startingAstroid in enumerate(astroidLocations):
    viewableAstroids = getAllViewableAstroids(startingAstroid, astroidLocations)
    angleOfOtherAstroids.append(viewableAstroids)

maximum = 0
maxIndex = None
for i, angle in enumerate(angleOfOtherAstroids):
    if len(angle) > maximum:
        maximum = len(angle)
        maxIndex = i

print(maximum)
#print(astroidLocations[maxIndex])

myAstroid = astroidLocations[maxIndex]
count = 0
while len(astroidLocations) > 1:
    allViwable = getAllViewableAstroids(myAstroid, astroidLocations)
    angles = allViwable.keys()
    angles = sorted(angles)

    for angle in angles:
        if angle == 0:
            count+=1
            if count == 200:
                x = allViwable[angle][2]
                y = allViwable[angle][3]
                print(x * 100 + y)
            astroidLocations.remove((allViwable[angle][2], allViwable[angle][3]))
            angles.remove(angle)

    for angle in angles:
        count+=1
        if count == 200:
            x = allViwable[angle][2]
            y = allViwable[angle][3]
            print(x * 100 + y)
            print(allViwable[angle])
        astroidLocations.remove((allViwable[angle][2], allViwable[angle][3]))
    #print(len(astroidLocations))
