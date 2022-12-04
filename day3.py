def readData(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def prioritiesSumPartOne(fileName):
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

def prioritiesSum(fileName):
    rucksacks = readData(fileName)
    groups = []
    prioritySum = 0


    currentList = []
    currentSack = 1
    for rucksack in rucksacks:
        currentList.append(rucksack)
        if currentSack == 3:
            groups.append(currentList)
            currentList = []
            currentSack = 0
        currentSack+=1
    for group in groups:
        sack1 = group[0].strip()
        sack2 = group[1].strip()
        sack3 = group[2].strip()
        commonFirstTwo = list(set(sack1) & set(sack2))
        for char in commonFirstTwo:
            if char in sack3:
                commonType = char
        if ord(commonType) in range(65,91):
            priority = ord(commonType) - 38
        else:
            priority = ord(commonType) - 96
        prioritySum +=priority
    print("The sum of the prorities of the shared item types is " + str(prioritySum))



prioritiesSum("day3.txt")