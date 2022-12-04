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
        if int(firstElf[0]) <= int(secondElf[0]) and int(firstElf[1]) >= int(secondElf[1]):
            containedCount += 1
        elif int(secondElf[0]) <= int(firstElf[0]) and int(secondElf[1]) >= int(firstElf[1]):
            containedCount += 1
    print("There are " + str(containedCount) + " pairs where one's work fully contains another.")

containedPairs("day4.txt")

