import re

class Board:
    def __init__(self):
        self.layout = []
        self.marked = [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
                ]

    def Call(self, calledNum):
        #  print(self.layout)
        for x in range(len(self.layout)):
            row = self.layout[x]
            for y in range(len(row)):
                boardNum = row[y]
                if calledNum == boardNum:
                    #  print(self.marked)
                    #  print(x)
                    #  print(y)
                    self.marked[x][y] = 1
                    return self.CheckWinner(x, y)
        return False

    def CheckWinner(self, x, y):
        rowCount = 0
        colCount = 0
        for check in range(5):
            rowCount += self.marked[x][check]
            colCount += self.marked[check][y]
        return rowCount >= 5 or colCount >= 5

    def CalcScore(self, num):
        unMarkedSum = 0
        for x in range(5):
            for y in range(5):
                if self.marked[x][y] == 0:
                    unMarkedSum += self.layout[x][y]
        return unMarkedSum * num

f = open("input.txt", "r")
#  f = open("testInput.txt", "r")
nums = []
curBoardId = -1
boards = []
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    if len(nums) == 0:
        for num in strippedLine.split(','):
            nums.append(int(num))
        continue
    if len(strippedLine) == 0:
        print("skip")
        curBoardId += 1
        continue
    if curBoardId not in boards:
        board = Board()
        boards.append(board)
    print(curBoardId)
    board = boards[curBoardId]
    line = []
    res = re.search("(\d*) *(\d*) *(\d*) *(\d*) *(\d*)", strippedLine)
    for groupId in range(1, 6):
        line.append(int(res.group(groupId)))
    #  print(line)
    board.layout.append(line)

#  print(len(boards))
#  print(boards)
for num in nums:
    for board in boards:
        if board.Call(num):
            print(num)
            print(board)
            print(board.layout)
            print(board.marked)
            print(board.CalcScore(num))
            exit()
