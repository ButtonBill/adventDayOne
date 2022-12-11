def read_data(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


class Head:
    def __init__(self, xCoordinate=0, yCoordinate=0):
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate

    def moveX(self, distance):
        self.xCoordinate += distance

    def moveY(self, distance):
        self.yCoordinate += distance

    def getX(self):
        return self.xCoordinate

    def getY(self):
        return self.yCoordinate

class Tail:
    def __init__(self, head = None, xCoordinate=0, yCoordinate=0,visitedLocations = []):
        self.head = head
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.visitedLocations = [(xCoordinate,yCoordinate)]

    def moveHeadX(self, distance):
        self.head.moveX(distance)

    def moveHeadY(self, distance):
        self.head.moveY(distance)

    def moveTailX(self):
        if self.head.getX() > self.xCoordinate:
            self.xCoordinate += 1
        else:
            self.xCoordinate -= 1

    def moveTailY(self):
        if self.head.getY() > self.yCoordinate:
            self.yCoordinate += 1
        else:
            self.yCoordinate -= 1

    def moveTail(self):
        currHeadX = self.head.getX()
        currHeadY = self.head.getY()
        #If the difference in x is more than 1
        if abs(currHeadX-self.xCoordinate) > 1:
            #If it's in the same row, move in the appropriate straight direction.
            if abs(currHeadY-self.yCoordinate) == 0:
                self.moveTailX()
            #if it's not in the same row, move in the correct diagonal direction
            else:
                self.moveTailY()
                self.moveTailX()
        #If the difference in y is more than 1, already in the correct column, so move up or down.
        if abs(currHeadY-self.yCoordinate) > 1:
            # If it's in the same column, move in the appropriate straight direction.
            if abs(currHeadX - self.xCoordinate) == 0:
                self.moveTailY()
            # If it's not in the same column, move in the correct diagonal direction
            else:
                self.moveTailX()
                self.moveTailY()
        #After moving the tail, update visited Locations.
        if not (self.xCoordinate, self.yCoordinate) in self.visitedLocations:
            self.visitedLocations.append((self.xCoordinate, self.yCoordinate))

    def numberVisitedLocations(self):
        print(self.visitedLocations)
        return len(self.visitedLocations)





def get_direction_list(lines):
    dirList = []
    for line in lines:
        splitLine = line.split()
        dirList.append(splitLine[0])
    return dirList


def get_distance_list(lines):
    distList = []
    for line in lines:
        splitLine = line.split()
        distList.append(int(splitLine[1]))
    return distList


def move_head(tail, direction, distance):
    if direction == 'U':
        while distance > 0:
            tail.moveHeadY(1)
            tail.moveTail()
            distance -= 1
    elif direction == 'D':
        while distance > 0:
            tail.moveHeadY(-1)
            tail.moveTail()
            distance -= 1
    elif direction == 'R':
        while distance > 0:
            tail.moveHeadX(1)
            tail.moveTail()
            distance -= 1
    else:
        while distance > 0:
            tail.moveHeadX(-1)
            tail.moveTail()
            distance -= 1
    return tail
def positions_tail_visited(fileName):
    lines = read_data(fileName)
    directionList = get_direction_list(lines)
    distanceList = get_distance_list(lines)
    tail = Tail(Head())
    for i in range(len(directionList)):
        tail = move_head(tail,directionList[i],distanceList[i])
    print ("There are " + str(tail.numberVisitedLocations()) + " locations that the tail has visited.")

positions_tail_visited("day9.txt")
