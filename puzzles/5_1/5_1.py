import re

def inclusiveRange(start, stopIncl):
    if start < stopIncl:
        return range(start, stopIncl + 1, 1)
    return range(start, stopIncl - 1, -1)

f = open("input.txt", "r")
#  f = open("testInput.txt", "r")
vents = {}
for line in f.readlines():
    strippedLine = line.strip()
    #  print(strippedLine)
    res = re.search("(\d*),(\d*) -> (\d*),(\d*)", strippedLine)
    x1 = int(res.group(1))
    y1 = int(res.group(2))
    x2 = int(res.group(3))
    y2 = int(res.group(4))
    if x1 != x2 and y1 != y2:
        continue
    for x in inclusiveRange(x1, x2):
        for y in inclusiveRange(y1, y2):
            if x not in vents.keys():
                vents[x] = {}
            if y not in vents[x].keys():
                vents[x][y] = 1
            else:
                vents[x][y] += 1

#  print(vents)
#  print(len(vents))

dangerVents = 0
#  nonDangerVents = 0
for x, row in vents.items():
    for y, vent in row.items():
        if vent > 1:
            dangerVents += 1
        #  else:
            #  nonDangerVents += 1

#  for x in range(9):
    #  line = ""
    #  for y in range(9):
        #  if x in vents.keys() and y in vents[x].keys():
            #  line += str(vents[x][y]) + " "
        #  else:
            #  line += "0 "
    #  print(line)

#  print(nonDangerVents)
print(dangerVents)
