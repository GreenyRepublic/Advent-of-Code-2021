from numpy.core.defchararray import array, split, splitlines
from typing import List

inputFile = "6_Lanternfish_input.txt"

def LanternfishPopulationAfterDays(fishPopulation : List[int], days : int) -> int:
    fishDaysToBreed = [0] * 9
    
    # Populate days to breed list
    for fish in fishPopulation:
        fishDaysToBreed[fish] += 1

    # Simulate breeding for n days
    for i in range(0, days):
        newfish = fishDaysToBreed[0]
        for j in range(0,len(fishDaysToBreed) - 1):
            fishDaysToBreed[j] = fishDaysToBreed[j + 1]
        fishDaysToBreed[6] += newfish
        fishDaysToBreed[8] = newfish

    return sum(fishDaysToBreed)

def ParseInput(filename : str) -> List[int]:
    
    lines = open(filename).readlines()
    outNums = list(map(int, lines[0].split(',')))
    return outNums    


def Main() -> None :

    lanternfish = ParseInput(inputFile)
    
    # Part 1
    print(LanternfishPopulationAfterDays(lanternfish, 80))

    # Part 2    
    print(LanternfishPopulationAfterDays(lanternfish, 256))
            
Main()