def readData(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def roundScore(selections):
    #Need to lose
    if selections[1] == 'X':
        if selections[0] == 'A':
            score = 3
        elif selections[0] == 'B':
            score = 1
        else:
            score = 2
    #Need to Draw
    elif selections[1] == 'Y':
        if selections[0] == 'A':
            score = 4
        elif selections[0] == 'B':
            score = 5
        else:
            score = 6
    #Need to Win
    else:
        if selections[0] == 'A':
            score = 8
        elif selections[0] == 'B':
            score = 9
        else:
            score = 7
    return score



def finalScore(fileName):
    totalScore = 0
    strategyGuide = readData(fileName)
    for line in strategyGuide:
        splitLine = line.split()
        totalScore +=roundScore(splitLine)
    print("The total score is " + str(totalScore))

finalScore("day2.txt")