f = open("input.txt", "r")
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

fuel = 0
for pos in horizPositions:
    fuel += abs(target - pos)

print(fuel)
