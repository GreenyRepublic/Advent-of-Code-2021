from os import linesep, write
from typing import Tuple, Dict
from collections import defaultdict, Counter


inputFile = "14_Polymers_input.txt"
testInputFile = "14_Polymers_test_input.txt"

def ExpandPolymer(polymer : str, rules : Dict[str,str], steps : int):
    charCount = defaultdict(int)
    pairCount = defaultdict(int)

    for char in polymer:
        charCount[char] += 1
    
    for i  in range(0,len(polymer) - 1):
        pair = polymer[i:i+2]
        pairCount[pair] += 1

    for i in range(0,steps):
        newPairCount = defaultdict(int)
        for rule in rules.keys():
            count = pairCount[rule]

            newChar = rules[rule]
            charCount[newChar] += count
            newPairA = rule[0] + newChar
            newPairB = newChar + rule[1]
            newPairCount[newPairA] += count
            newPairCount[newPairB] += count
            
        pairCount = newPairCount

    return charCount

def ParseInput(filename : str) -> Tuple[str, Dict[str, str]]:  

    file = open(filename)
    startchain = ""
    rules = {}
    lineBreak = False

    for line in file.readlines():
        if len(line.strip()) == 0:
            lineBreak = True
            continue

        if lineBreak:
            parsed = line.strip().split('->')
            pattern = parsed[0].strip()
            insert = parsed[1].strip()
            rules[pattern] = insert

        else:
            startchain = line.strip()
        

    return startchain, rules

def Main() -> None :
    startChain, rules = ParseInput(inputFile)
    
    # Part 1
    firstPolymer = ExpandPolymer(startChain, rules, 10)
    counts = Counter(firstPolymer).most_common()
    largest = counts[0][1]
    smallest  = counts[-1][1]
    print(largest - smallest)

    # Part 2
    secondPolymer = ExpandPolymer(startChain, rules, 40)
    counts = Counter(secondPolymer).most_common()
    largest = counts[0][1]
    smallest  = counts[-1][1]
    print(largest - smallest)

    
Main()