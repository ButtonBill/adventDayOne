def readData(fileName):
    calorieDict = {}
    currentElf = 1
    currentCalories = 0
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readlines()

        for line in lines:
            if line.strip() == "":
                calorieDict[currentElf]=currentCalories
                currentElf+=1
                currentCalories=0
            else:
                currentCalories+=int(line)

    return calorieDict

def mostCalories(fileName):
    calorieDict = readData(fileName)
    highestCalories = max(calorieDict.values())
    mostCaloriesElf = max(calorieDict, key=calorieDict.get)

    print("The elf carrying the most calories is Elf number " + str(mostCaloriesElf) + " carrying " + str(highestCalories))

mostCalories("input.txt")

