from os import linesep
from typing import Deque, List, Tuple

inputFile = "11_Octopus_input.txt"
inputTestFile = "11_Octopus_test_input.txt"

GRID_SIZE = 10

def GetAdjacentCoordinates(inmap : List[List[int]], coord: Tuple[int,int]) -> List[Tuple[int,int]]:
    output = []
    x = coord[0]
    y = coord[1]
    mapWidth = len(inmap)
    mapHeight = len(inmap[0])

    leftBoundary = x > 0
    rightBoundary = x < mapWidth - 1
    topBoundary = y > 0
    bottomBoundary = y < mapHeight - 1

    if leftBoundary:
        output.append((x - 1, y))
    if rightBoundary:
        output.append((x + 1, y))
    if topBoundary:
        output.append((x, y - 1))
    if bottomBoundary:
        output.append((x, y + 1))
    if leftBoundary and topBoundary:
        output.append((x - 1, y - 1))
    if leftBoundary and bottomBoundary:
        output.append((x - 1, y + 1))
    if rightBoundary and topBoundary:
        output.append((x + 1, y - 1))
    if rightBoundary and bottomBoundary:
        output.append((x + 1, y + 1))

    return output

def RunGridStep(octopusGrid : List[List[int]]) -> int:
    hasFlashed = set()
    flashingOcts = Deque()

    for i in range(0, GRID_SIZE):
        for j in range(0, GRID_SIZE):
            octopusGrid[i][j] += 1
            if octopusGrid[i][j] == 10:
                flashingOcts.append((i,j))
    
    while len(flashingOcts) > 0:
        currentOct = flashingOcts.pop()
        if currentOct not in hasFlashed:
            hasFlashed.add(currentOct)
            octopusGrid[currentOct[0]][currentOct[1]] = 0
            for adjacent in GetAdjacentCoordinates(octopusGrid, currentOct):
                if adjacent not in hasFlashed:
                    octopusGrid[adjacent[0]][adjacent[1]] += 1
                    if octopusGrid[adjacent[0]][adjacent[1]] == 10:
                        flashingOcts.append(adjacent)

    return len(hasFlashed)

def RunOctopusSequence(octopusGrid : List[List[int]], repetitions : int) -> Tuple[int, int]:
    total = 0
    firstSync = 0
    for i in range(0,repetitions):
        flashes = RunGridStep(octopusGrid)
        total += flashes
        if flashes == (GRID_SIZE * GRID_SIZE) and firstSync == 0:
            firstSync = i + 1

    return total, firstSync

def ParseInput(filename : str) -> List[List[int]]:    

    file = open(filename)
    output = []
    for line in file.readlines():
        nums = []
        for char in line.strip():
            nums.append(int(char))
        output.append(nums)
    return output

def Main() -> None :

    octopusGrid = ParseInput(inputFile)
    
    # Part 1
    flashCount, firstSync = RunOctopusSequence(octopusGrid, 500)
    print(flashCount)

    # Part 2
    print(firstSync)
    
Main()