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

    calorieDict.pop(mostCaloriesElf)
    secondHighestCalories = max(calorieDict.values())
    secondMostCaloriesElf = max(calorieDict, key=calorieDict.get)

    calorieDict.pop(secondMostCaloriesElf)
    thirdHighestCalories = max(calorieDict.values())
    thirdMostCaloriesElf = max(calorieDict, key=calorieDict.get)



    print("The elf carrying the most calories is Elf number " + str(mostCaloriesElf) + " carrying " + str(highestCalories))
    print("The elf carrying the second most calories is Elf number " + str(secondMostCaloriesElf) + " carrying " + str(secondHighestCalories))
    print("The elf carrying the third most calories is Elf number " + str(thirdMostCaloriesElf) + " carrying " + str(thirdHighestCalories))
    print("The total number of calories they're carrying is "+ str(highestCalories+secondHighestCalories+thirdHighestCalories))

mostCalories("input.txt")

