import math

input = open("input.txt", "r").readlines()

coordinates = []
intersections = []

for i in [0,1]:
    coordinates.append({})
    line = input[i]
    wire = line.split(',')
    currentX = 0
    currentY = 0
    steps = 0
    for move in wire:
        direction = move[0]
        spaces = int(move[1:])
        for j in range(spaces):
            if direction == 'R':
                currentX += 1
            if direction == 'L':
                currentX -= 1
            if direction == 'U':
                currentY += 1
            if direction == 'D':
                currentY -= 1
            steps += 1
            key = str(currentX) + "," + str(currentY)
            coordinates[i][key] = steps
            if i == 1:
                if key in coordinates[0]:
                    intersections.append(steps + coordinates[0][key])

smallestDistance = None
for intersection in intersections:
    currentDistance = intersection  # abs(intersection[0]) + abs(intersection[1])

    if smallestDistance is None:
        smallestDistance = currentDistance

    if currentDistance < smallestDistance:
        smallestDistance = currentDistance

print(smallestDistance)
        