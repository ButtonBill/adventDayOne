def readData(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def containedPairs(fileName):
    pairs = readData(fileName)
    containedCount = 0
    for pair in pairs:
        stripPair= pair.strip('\n')
        assignments = stripPair.split(",")
        firstElf = assignments[0].split("-")
        secondElf = assignments[1].split("-")
        if max(int(firstElf[0]),int(secondElf[0])) <= min(int(firstElf[1]),int(secondElf[1])):
                containedCount += 1
    print("There are " + str(containedCount) + " pairs where the work overlaps")

containedPairs("day4.txt")

