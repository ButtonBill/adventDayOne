def read_data(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def remove_directory(currentDirectory):
    if len(currentDirectory) == 1:
        return ""
    return "-".join(currentDirectory.split("-")[:-1])

def update_sizes(directoryDict,currentDirectory,size):
    while len(currentDirectory) > 0:
        directoryDict[currentDirectory] +=size
        currentDirectory = remove_directory(currentDirectory)
    return directoryDict

def command_handler(lines):
    directoryDict = {}
    currentDirectory = ""
    for i in range(len(lines)):
        # If changing directories, update size and reset.
        if lines[i][0:4] == "$ cd":
            splitLine = lines[i].split()
            # If going to the root, current directory is the root
            if splitLine[2] == '/':
                currentDirectory = "/"
                if not currentDirectory in directoryDict:
                    directoryDict[currentDirectory] = 0
            # If going up a level, remove the last directory in the list.
            elif splitLine[2] == "..":
                currentDirectory = remove_directory(currentDirectory)
            # Otherwise, add the new directory to the current one, and dictionary.
            else:
                currentDirectory = currentDirectory + '-' + splitLine[2]
                if not currentDirectory in directoryDict:
                    directoryDict[currentDirectory] = 0
        # If listing directory, or directories inside, do nothing. Otherwise, get size and update.
        elif lines[i][0:4] != "$ ls" and lines[i][0:3] != "dir":
            splitLine = lines[i].split()
            directoryDict = update_sizes(directoryDict,currentDirectory, int(splitLine[0]))
    return directoryDict

MAX_SIZE = 100000
def sum_directory_sizes(fileName):
    lines = read_data(fileName)
    directoryDictionary = command_handler(lines)
    sum = 0
    for size in directoryDictionary.values():
        if size <= MAX_SIZE:
            sum += size
    print("The sum of the sizes of directories with size under " + str(MAX_SIZE) + " is " + str(sum))

sum_directory_sizes("day7.txt")