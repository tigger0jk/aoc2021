f = open("input.txt", "r")
depths = []
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    newDepth = int(strippedLine)
    depths.append(newDepth)

count = 0
for index in range(len(depths)):
    if index - 1 <= 0:
        continue

    prevWindow = sum(depths[index-1:index-4:-1])
    print(prevWindow)

    curWindow = sum(depths[index:index-3:-1])
    print(curWindow)

    if curWindow > prevWindow:
        count += 1

print(count)
