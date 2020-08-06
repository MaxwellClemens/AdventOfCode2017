import math

input = open("input.txt", "r").readlines()

def calcFuelRequered(mass):
    return math.floor(int(mass) / 3) - 2

sum = 0
for mass in input:
    value = calcFuelRequered(mass)

    while value > 0:
        sum += value
        value = calcFuelRequered(value)

print(sum)