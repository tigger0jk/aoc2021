f = open("input.txt", "r")
#  f = open("testInput.txt", "r")

def calcFuelForTarget(horizPositions, target):
    fuel = 0
    for pos in horizPositions:
        dist = abs(target - pos)
        fuel += (dist * (dist + 1)) / 2
    return int(fuel)

horizPositions = []
for line in f.readlines():
    strippedLine = line.strip()
    #  print(strippedLine)
    strings = strippedLine.split(',')
    for string in strings:
        horizPositions.append(int(string))

horizPositions.sort()
print(horizPositions)
midpoint = int(len(horizPositions)/2)
target = horizPositions[midpoint]

lowestFuel = float('inf')
for pos in range(horizPositions[-1]):
    target = pos
    fuel = calcFuelForTarget(horizPositions, target)
    #  print(fuel)
    if fuel < lowestFuel:
        lowestFuel = fuel
        lowestPos = target
        #  print(lowestPos)

print(lowestPos)
print(lowestFuel)
