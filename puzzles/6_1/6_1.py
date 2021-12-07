f = open("input.txt", "r")
timers = [0,0,0,0,0,0,0,0,0] # 8 is max
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    for val in strippedLine.split(','):
        timers[int(val)] += 1

print(timers)

for day in range(80):
    spawners = timers.pop(0)
    timers.append(spawners)
    timers[6] += spawners
    print(timers)

print(sum(timers))
