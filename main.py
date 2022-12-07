def read_data(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readline()
    return lines


def first_marker_one(fileName):
    datastreamBuffer = read_data(fileName)
    lastFour = [datastreamBuffer[0],datastreamBuffer[1],datastreamBuffer[2],datastreamBuffer[3]]
    marker = 4
    lastChanged = 0
    while not lastChanged == -1:
        lastFour[lastChanged] = datastreamBuffer[marker]
        set = {lastFour[0],lastFour[1],lastFour[2],lastFour[3]}
        if len(set) == 4:
            lastChanged = -1
        else:
            lastChanged = (lastChanged + 1) % 4
        marker += 1
    print("Part one: The marker is " + str(marker))


first_marker_one("day6.txt")
