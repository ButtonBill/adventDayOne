def read_data(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines

def trees_matrix(lines):
    matrix = [ [ 0 for i in range(len(lines)) ] for j in range(len(lines[0])) ]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            matrix[i][j] = int(lines[i][j])

    return matrix


def is_visible(treeMatrix,row, column,height):
    if row == 0 or column == 0 or row == len(treeMatrix)-1 or column == len(treeMatrix[0])-1:
        return 1

    #Check to the left
    left = 1
    for i in range(column-1,-1,-1):
        if treeMatrix[row][i] >= height:
            left = 0

    #Check to the right
    right = 1
    for i in range(column+1,len(treeMatrix[row])):
        if treeMatrix[row][i] >= height:
            right = 0

    #Check up
    up = 1
    for i in range(row-1,-1,-1):
        if treeMatrix[i][column] >= height:
            up = 0

    #Check down
    down = 1
    for i in range(row+1,len(treeMatrix)):
        if treeMatrix[i][column] >= height:
            down = 0

    return max(left,right,up,down)

def count_visible(fileName):
    lines = read_data(fileName)
    treeMatrix = trees_matrix(lines)
    visCount = 0
    for i in range(len(treeMatrix)):
        for j in range(len(treeMatrix[i])):
            visCount += is_visible(treeMatrix, i, j, treeMatrix[i][j])

    print("There are " + str(visCount) + " visible trees")

def scenic_score(treeMatrix,row, column,height):
    # Check to the left
    left = 0
    for i in range(column - 1, -1, -1):
        left += 1
        if treeMatrix[row][i] >= height:
            break

    # Check to the right
    right = 0
    for i in range(column + 1, len(treeMatrix[row])):
        right += 1
        if treeMatrix[row][i] >= height:
            break

    # Check up
    up = 0
    for i in range(row - 1, -1, -1):
        up += 1
        if treeMatrix[i][column] >= height:
            break

    # Check down
    down = 0
    for i in range(row + 1, len(treeMatrix)):
        down += 1
        if treeMatrix[i][column] >= height:
            break


    print(str(row) + " " + str(column))
    print(left)
    print(right)
    print(up)
    print(down)
    print("")

    return left*right*up*down


def max_scenic_score(fileName):
    lines = read_data(fileName)
    treeMatrix = trees_matrix(lines)
    highScore = 0
    for i in range(len(treeMatrix)):
        for j in range(len(treeMatrix[i])):
            highScore = max(highScore,scenic_score(treeMatrix,i,j,treeMatrix[i][j]))

    print("The best possible scenic score is " + str(highScore))


max_scenic_score("day8.txt")
