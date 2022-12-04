def readData(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def prioritiesSum(fileName):
    rucksacks = readData(fileName)
    prioritySum = 0
    for rucksack in rucksacks:
        compartment1, compartment2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        commonType = list(set(compartment1) & set(compartment2))
        if ord(commonType[0]) in range(65,91):
            priority = ord(commonType[0]) - 38
        else:
            priority = ord(commonType[0]) - 96
        prioritySum +=priority
    print ("The sum of the prorities of the shared item types is " + str(prioritySum))

prioritiesSum("day3.txt")