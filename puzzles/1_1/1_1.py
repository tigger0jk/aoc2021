f = open("input.txt", "r")
depth = -1
count = 0
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    newDepth = int(strippedLine)
    if depth == -1:
        depth = newDepth
        continue
    if newDepth > depth:
        count += 1
    depth = newDepth

print(count)
