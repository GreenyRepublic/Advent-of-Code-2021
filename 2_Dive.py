import sys
import io
from typing import List, Tuple

inputFile = "2_Dive_input.txt"

def GetPositionAfterDirections(directions: List[str]) -> Tuple[int,int]:
    counts = {'forward' : 0, 'up' : 0, 'down' : 0}
    for entry in directions:
        direction, distance = entry.split()
        counts[direction] += int(distance)
    return counts['forward'], (counts['down'] - counts['up'])

def GetPositionAfterDirectionsWithAiming(directions: List[str]) -> Tuple[int,int]:
    aiming = 0
    horizontalDistance = 0
    verticalDistance = 0
    for entry in directions:
        direction, distance = entry.split()
        distance = int(distance)
        if direction == "up":
            aiming -= distance
        elif direction == "down":
            aiming += distance
        elif direction == "forward":
            horizontalDistance += distance
            verticalDistance += distance * aiming

    return horizontalDistance, verticalDistance

def Main() -> None:

    input = open(inputFile)
    data = input.readlines()

    # Part 1
    distances = GetPositionAfterDirections(data)
    partOneAnswer = distances[0] * distances[1]
    print(partOneAnswer)

    # Part 2
    distances = GetPositionAfterDirectionsWithAiming(data)
    partTwoAnswer = distances[0] * distances[1]
    print(partTwoAnswer)
    

Main()