def readData(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def roundScore(selections):
    if selections[1] == 'X':
        score = 1
        if selections[0] == 'A':
            score += 3
        elif selections[0] == 'B':
            score += 0
        else:
            score += 6
    elif selections[1] == 'Y':
        score = 2
        if selections[0] == 'A':
            score += 6
        elif selections[0] == 'B':
            score +=3
        else:
            score += 0
    else:
        score = 3
        if selections[0] == 'A':
            score +=0
        elif selections[0] == 'B':
            score +=6
        else:
            score +=3
    return score

def finalScore(fileName):
    totalScore = 0
    strategyGuide = readData(fileName)
    for line in strategyGuide:
        splitLine = line.split()
        totalScore +=roundScore(splitLine)
    print("The total score is " + str(totalScore))

finalScore("day2.txt")