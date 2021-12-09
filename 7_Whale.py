from os import linesep
import sys
import io
from collections import defaultdict
from typing import List
from typing import DefaultDict

inputFile = "7_Whale_input.txt"

def NaturalSequenceSum(size : int) -> int:
    return (1 + size)* (size/2)

def GetTotalFuelCost(crabPositions : DefaultDict, candidatePosition: int, linearBurn : bool = True) -> int:
    cost = 0
    for position, count in crabPositions.items():
        if (linearBurn):
            cost += abs(position - candidatePosition) * count
        else:
            cost += NaturalSequenceSum(abs(position - candidatePosition)) * count
    return cost

def FindCheapestPosition(inPositions : List[int], linearBurn : bool = True) -> int:
    positionDict = defaultdict(int)
    for pos in inPositions:
        positionDict[pos] += 1

    smallestPos = min(inPositions)
    largestPos = max(inPositions)
    smallestCost = 2147483647
    for i in range(smallestPos, largestPos):
        cost = GetTotalFuelCost(positionDict, i, linearBurn)
        if (cost < smallestCost):
            smallestCost = cost

    return smallestCost

def ParseInput(filename : str) -> List[int]:
    
    lines = open(filename).readlines()
    outNums = list(map(int, lines[0].split(',')))
    return outNums    


def Main() -> None :

    crabPositions = ParseInput(inputFile)
    
    # Part 1
    print(FindCheapestPosition(crabPositions, True))

    # Part 2    
    print(FindCheapestPosition(crabPositions, False))
            
Main()