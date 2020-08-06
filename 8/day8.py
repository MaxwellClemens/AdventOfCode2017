import math

fileInput = open("input.txt", "r").read()#.split(",")

currentWinner = [None,0,0]

layer = 25 * 6
numberOf0 = 0
numberOf1 = 0
numberOf2 = 0

image = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 
2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
print(image)
j = 0
k = 0
for index in range(len(fileInput)):
    i = fileInput[index]

    if i == '0' and image[k][j] == 2:
        image[k][j] = 0
    if i == '1' and image[k][j] == 2:
        image[k][j] = 1
    
    j += 1
    if j == 25:
        j = 0
        k += 1
    if k == 6:
        k = 0
    
for layer in image:
    print(layer)