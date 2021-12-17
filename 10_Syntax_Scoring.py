from os import linesep
from typing import Deque, List, Tuple

inputFile = "10_Syntax_Scoring_input.txt"
testInputFile = "10_Syntax_Scoring_test_input.txt"

MATCHING_BRACES = {
    '{' : '}',
    '[' : ']',
    '(' : ')',
    '<' : '>'
}

BRACE_SCORES_ONE = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

BRACE_SCORES_TWO = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

# Returns first invalid brace if line corrupted, empty if fine

def IsLineCorrupted(line : str) -> Tuple[bool, str]:
    braceStack = Deque()
    for char in line:
        if char in MATCHING_BRACES.keys():
            braceStack.append(char)

        elif char in MATCHING_BRACES.values():
            if MATCHING_BRACES[braceStack.pop()] != char:
                return char
    
    return ""

# Get the braces to finish an incomplete line
def GetLineCompletion(line : str) -> str:
    braceStack = Deque()
    for char in line:
        if char in MATCHING_BRACES.keys():
            braceStack.append(char)

        elif char in MATCHING_BRACES.values():
            braceStack.pop()
    
    output = ""
    braceStack.reverse()
    for brace in braceStack:
        output += MATCHING_BRACES[brace]

    return output

def ScoreLineCompletion(line : str) -> int:
    score = 0
    completedLine = GetLineCompletion(line)
    for char in completedLine:
        score *= 5
        score += BRACE_SCORES_TWO[char]

    return score


def ScoreLineCorruption(lines : List[str]) -> int:
    score = 0
    for line in lines:
        char = IsLineCorrupted(line)
        if len(char) > 0:
            score += BRACE_SCORES_ONE[char]
    return score

def ParseInput(filename : str) -> List[str]:    

    file = open(filename)
    output = []
    for line in file.readlines():
        output.append(line.strip())
    return output

def Main() -> None :

    syntaxLines = ParseInput(inputFile)
    
    # Part 1
    corruptionScore = ScoreLineCorruption(syntaxLines)
    print(corruptionScore)

    # Part 2
    incompleteLineScores = []
    for line in syntaxLines:
        if IsLineCorrupted(line) == "":
            incompleteLineScores.append(ScoreLineCompletion(line))
    incompleteLineScores.sort()
    middleIndex = int((len(incompleteLineScores)) / 2)
    print(incompleteLineScores[middleIndex])

Main()