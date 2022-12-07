def read_data(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines


def get_arrangement(lines):
    initial_arrangement = []
    line = lines[0]
    count = 0
    while line[1] != '1':
        initial_arrangement.append(line)
        count += 1
        line = lines[count]
    return initial_arrangement


from collections import deque

def transpose(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result


def create_stacks(arrangement):
    full_arrangement = []
    for line in arrangement:
        spot = 1
        list = []
        count = 0
        while spot < len(line) -4:
            spot = 1 + 4 * count
            list.append(line[spot])
            count += 1
        while count < 9:
            list.append(' ')
            count +=1
        full_arrangement.append(list)
    # Full arrangement has blanks where they should be.
    stackList = []
    stack = deque()
    full_arrangement = transpose(full_arrangement)
    for i in range(len(full_arrangement)): #for each row of the arrangement
        for j in range(len(full_arrangement[0])): #for each column
            if full_arrangement[i][j] != ' ':
                stack.append(full_arrangement[i][j])
        stackList.append(stack)
        stack = deque()
    return stackList


# create_stacks now gets full arrangement with blanks where should be.

def handleMovesOne(lines, stackList):
    moveList = []
    for line in lines:
        if line[0] == 'm':
            moveList.append(line)
    for move in moveList:
        splitMove = move.split()
        numberMoved = int(splitMove[1])
        startpoint = int(splitMove[3])-1
        destination = int(splitMove[5])-1
        for i in range(numberMoved):
            stackList[destination].appendleft(stackList[startpoint].popleft())
    return stackList

def handleMovesTwo(lines, stackList):
    moveList = []
    for line in lines:
        if line[0] == 'm':
            moveList.append(line)
    movedBlocks = []
    for move in moveList:
        splitMove = move.split()
        numberMoved = int(splitMove[1])
        startpoint = int(splitMove[3])-1
        destination = int(splitMove[5])-1
        for i in range(numberMoved): #Put the blocks in a list
            movedBlocks.append(stackList[startpoint].popleft())
        for block in reversed(movedBlocks):
            stackList[destination].appendleft(block)
        movedBlocks = []
    return stackList


def get_tops_one(fileName):
    lines = read_data(fileName)
    stackList = create_stacks(get_arrangement(lines))
    newStacks = handleMovesOne(lines, stackList)
    tops = ""
    for i in range(len(newStacks)):
        tops= tops + newStacks[i].popleft()
    print("Part 1: The tops are " + tops)

def get_tops_two(fileName):
    lines = read_data(fileName)
    stackList = create_stacks(get_arrangement(lines))
    newStacks = handleMovesTwo(lines, stackList)
    tops = ""
    for i in range(len(newStacks)):
        tops= tops + newStacks[i].popleft()
    print("Part 2: The tops are " + tops)


get_tops_one("day5.txt")
get_tops_two("day5.txt")

