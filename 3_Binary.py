import sys
import io

inputFile = "3_Binary_input.txt"

def GetCommonBit(input : 'list[str]', position : int) -> int:
    commonBit = 0
    for item in input:
        if (item[position]) == '0':
            commonBit -= 1
        elif (item[position]) == '1':
            commonBit += 1

    return int(commonBit >= 0)
    

def GetGammaAndEpsilonRate(input : 'list[str]') -> 'tuple[int,int]':
    bitCount = len(input[0].strip())
    gamma = 0
    epsilon = 0
    for x in range(0, bitCount):
        commonBit = GetCommonBit(input, x)
        if commonBit == 1:
            gamma += pow(2, bitCount - x - 1)
        else:
            epsilon += pow(2, bitCount - x - 1)
    
    return gamma, epsilon

def GetLifeSupportRating(input: 'list[str]', oxygen : bool) -> int:
    bitCount = len(input[0].strip())

    candidates = input.copy()

    for x in range(0, bitCount):
        commonBit = GetCommonBit(candidates, x)
        newList = []
        for value in candidates:
            if (value[x] == str(commonBit) and oxygen) or (value[x] != str(commonBit) and not oxygen) :
                newList.append(value)

        candidates = newList
        if len(candidates) == 1:
            break
    
    return int(list(candidates)[0],2)


def Main():

    testIn = ["00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010"]

    input = open(inputFile)
    data = input.readlines()

    # Part 1
    gamma, epsilon = GetGammaAndEpsilonRate(data)
    print(gamma * epsilon)

    # Part 2
    oxygen = GetLifeSupportRating(data, True)
    co2 = GetLifeSupportRating(data, False)
    print(oxygen * co2)
    

Main()