import re

def inclusiveRange(start, stopIncl):
    if start < stopIncl:
        return range(start, stopIncl + 1, 1)
    return range(start, stopIncl - 1, -1)

f = open("input.txt", "r")
vents = {}
for line in f.readlines():
    strippedLine = line.strip()
    #  print(strippedLine)
    res = re.search("(\d*),(\d*) -> (\d*),(\d*)", strippedLine)
    x1 = int(res.group(1))
    y1 = int(res.group(2))
    x2 = int(res.group(3))
    y2 = int(res.group(4))
    #  if x1 != x2 and y1 != y2:
        #  continue
    xRange = inclusiveRange(x1, x2)
    yRange = inclusiveRange(y1, y2)
    if len(xRange) == len(yRange):
        # diag
        for i in range(len(xRange)):
            x = xRange[i]
            y = yRange[i]
            if x not in vents.keys():
                vents[x] = {}
            if y not in vents[x].keys():
                vents[x][y] = 1
            else:
                vents[x][y] += 1
    else:
        for x in xRange:
            for y in yRange:
                if x not in vents.keys():
                    vents[x] = {}
                if y not in vents[x].keys():
                    vents[x][y] = 1
                else:
                    vents[x][y] += 1

#  print(vents)
#  print(len(vents))

dangerVents = 0
for x, row in vents.items():
    for y, vent in row.items():
        if vent > 1:
            dangerVents += 1

print(dangerVents)
