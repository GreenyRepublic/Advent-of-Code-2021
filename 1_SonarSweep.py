import sys
import io
from typing import List

def CountDepthIncreases(depths: List[int]) -> int:
    increases = 0
    previous = 0
    for depth in depths:
        if depth > previous and previous != 0:
            increases += 1
        previous = depth
        
    return increases

def CountDepthIncreasesWithWindows(depths: List[int]) -> int:
    buckets = [0] * (len(depths) - 2)
    for i in range(0,len(buckets)):
        for j in range (0,3):
            sample = depths[i + j]
            buckets[i] += sample

    return CountDepthIncreases(buckets)
        

def Main() -> None:

    input = open("1_SonarSweep_input.txt")
    data = input.readlines()
    dataAsInts = list(map(int, data))

    # Part 1
    partOneAnswer = CountDepthIncreases(dataAsInts)
    print(partOneAnswer)

    # Part 2
    partTwoAnswer = CountDepthIncreasesWithWindows(dataAsInts)
    print(partTwoAnswer)

Main()