from os import linesep
from collections import defaultdict
from typing import List, Tuple, DefaultDict

inputFile = "9_Smoke_Basin_input.txt"
testInputFile = "9_Smoke_Basin_test_input.txt"

def GetAdjacentCoordinates(ventMap : List[List[int]], coord: Tuple[int,int]) -> List[Tuple[int,int]]:
    output = []
    x = coord[0]
    y = coord[1]
    mapWidth = len(ventMap)
    mapHeight = len(ventMap[0])
    if (x > 0):
        output.append((x - 1, y))
    if (x < mapWidth - 1):
        output.append((x + 1, y))
    if (x > 0):
        output.append((x - 1, y))
    if (y > 0):
        output.append((x, y - 1))
    if (y < mapHeight - 1):
        output.append((x, y + 1))
    return output

def FindBasins(ventMap: List[List[int]], lowPoints: List[Tuple[int,int]]) -> List[List[Tuple[int,int]]]:
    output = []
    exploredCoords = set()
    for coord in lowPoints:
        currentBasin = []
        coordsToExplore = [coord]
        
        # Iterate over items in boundary
        while len(coordsToExplore) > 0:
            currentCoord = coordsToExplore.pop(0)

            if currentCoord not in exploredCoords and ventMap[currentCoord[0]][currentCoord[1]] < 9:
                currentBasin.append(currentCoord)
                exploredCoords.add(currentCoord)

                for adjacentCoord in GetAdjacentCoordinates(ventMap, currentCoord):
                    coordsToExplore.append(adjacentCoord)

        output.append(currentBasin)

    return output

def FindLowPoints(ventMap: List[List[int]]) -> List[Tuple[int,int]]:
    output = []
    for i in range(0,len(ventMap)):
        for j in range(0,len(ventMap[0])):
            currentCell = ventMap[i][j]
            isLow = True
            for point in GetAdjacentCoordinates(ventMap, (i,j)):
                isLow &= (ventMap[point[0]][point[1]] > currentCell)
            if isLow:
                output.append((i,j))

    return output

def ParseInput(filename : str) -> List[List[int]]:    
    lines = open(filename).readlines()
    output = []
    for line in lines:
        numLine = []
        for char in line.strip():
            numLine.append(int(char))
        output.append(numLine)

    return output   

def Main() -> None :

    ventMap = ParseInput(inputFile)
    
    # Part 1
    lowPoints = FindLowPoints(ventMap)
    riskLevelTotal = 0
    for point in lowPoints:
        riskLevelTotal += ventMap[point[0]][point[1]] + 1
    print(riskLevelTotal)

    # Part 2    
    basins = FindBasins(ventMap, lowPoints)
    basinSizes = list(map(len, basins))
    basinSizes.sort(reverse = True)
    largestBasinsProduct = basinSizes[0] * basinSizes[1] * basinSizes[2]
    print(largestBasinsProduct)
            
Main()