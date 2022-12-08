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



count_visible("day8.txt")
