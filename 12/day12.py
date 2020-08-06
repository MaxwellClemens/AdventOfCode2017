import math

def calculateChangeToVelocities(currentPositions, allPositions, currentIndex):
    changeToVelocities = [0,0,0]
    for index, position in enumerate(allPositions):
        if index == currentIndex:
            continue
        for k in range(3):
            if currentPositions[k] < position[k]:
                changeToVelocities[k] += 1
            if currentPositions[k] > position[k]:
                changeToVelocities[k] -= 1
    return changeToVelocities

lines = open("input.txt", "r").readlines()#.split(",")

positions = []
velocities = []

previousStates=[{},{},{}]

for index, line in enumerate(lines):
    values = line.replace("\n","").split(",")
    position = (int(values[0]), int(values[1]), int(values[2]))
    positions.append(position)
    velocities.append((0,0,0))
    # previousStates[index][(position,(0,0,0))] = True

steps = 0
while True:
    lenx = len(previousStates[0])
    leny = len(previousStates[1])
    lenz = len(previousStates[2])
    for i in range(3):
        previousStates[i][((positions[0][i],positions[1][i],positions[2][i]),(velocities[0][i],velocities[1][i],velocities[2][i]))] = True

    if lenx == len(previousStates[0]) and leny == len(previousStates[1]) and lenz == len(previousStates[2]):
        break

    newPositions = []
    newVelocities = []
    for j in range(len(positions)):
        changeToVelocities = calculateChangeToVelocities(positions[j], positions, j)
        newVelocity = (velocities[j][0] + changeToVelocities[0], velocities[j][1] + changeToVelocities[1], velocities[j][2] + changeToVelocities[2])
        newPosition = (positions[j][0] + newVelocity[0], positions[j][1] + newVelocity[1], positions[j][2] + newVelocity[2])
        
        newPositions.append(newPosition)
        newVelocities.append(newVelocity)

    steps += 1
    # if steps % 1000000 == 0:
    #     print(steps)
    
    # isRepeted = [False, False, False, False]
    # for j in range(len(newPositions)):
    #     if (newPositions[j],newVelocities[j]) in previousStates[j]:
    #         isRepeted[j] = True
    #     previousStates[j][(newPositions[j],newVelocities[j])] = True
    # if(isRepeted[0] and isRepeted[1] and isRepeted[2] and isRepeted[3]):
    #     break


    positions = newPositions
    velocities = newVelocities

print(steps)
print(len(previousStates[0]))
print(len(previousStates[1]))
print(len(previousStates[2]))

# potentialEnergies = []
# kineticEnergies = []
# for position in positions:
#     energy = 0
#     for value in position:
#         energy += abs(value)
#     potentialEnergies.append(energy)
# for velocity in velocities:
#     energy = 0
#     for value in velocity:
#         energy += abs(value)
#     kineticEnergies.append(energy)

# totalEnergy = 0
# for i in range(len(potentialEnergies)):
#     totalEnergy += potentialEnergies[i] * kineticEnergies[i]
# print(potentialEnergies)
# print(kineticEnergies)
# print(totalEnergy)