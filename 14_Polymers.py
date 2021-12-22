from os import linesep, write
from typing import Tuple, List, Dict

inputFile = "14_Polymers_input.txt"
testInputFile = "14_Polymers_test_input.txt"

def ParseInput(filename : str) -> Tuple[str, List[Dict[str, str]]]:  

    file = open(filename)
    startchain = ""
    rules = []
    lineBreak = False

    for line in file.readlines():
        if len(line.strip()) == 0:
            lineBreak = True
            continue

        if lineBreak:
            parsed = line.strip().split('->')
            pattern = parsed[0]
            insert = parsed[1]
            rules.append({"pattern" : pattern, "insert" : insert})

        else:
            startchain = line
        

    return startchain, rules

def Main() -> None :
    startChain, rules = ParseInput(inputFile)
    print(startChain)
    print(rules)

    # Part 1
    
    # Part 2

    
Main()