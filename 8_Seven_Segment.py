from os import linesep
from collections import defaultdict
from typing import List, Tuple, DefaultDict

inputFile = "8_Seven_segment_input.txt"

DIGIT_SEGMENT_COUNTS = {
    0 : 6,
    1 : 2,
    2 : 5,
    3 : 5,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 3,
    8 : 7,
    9 : 6
}

UNIQUE_DIGITS = {
    2 : 1,
    4 : 4,
    3 : 7,
    7 : 8
}

class Signal:
    def __init__(self, inputCodes: str, displayedDigits: str):
        self._inputCodes = []            
        self._displayedDigits = []
        for incode in inputCodes.split():
            sortedCode = ''.join(sorted(incode))
            self._inputCodes.append(sortedCode)
        for digit in displayedDigits.split():
            sortedCode = ''.join(sorted(digit))
            self._displayedDigits.append(sortedCode)

    def GetDigitCountInOutput(self, digit : int) -> int:
        count = 0
        for num in self._displayedDigits:
            if len(num) in UNIQUE_DIGITS.keys() and UNIQUE_DIGITS[len(num)] == digit:
                count += 1
        return count


def ParseInput(filename : str) -> List[Signal]:    
    lines = open(filename).readlines()
    outSignals = []
    for line in lines:
        split = line.split('|')
        outSignals.append(Signal(split[0], split[1]))
    return outSignals   

def Main() -> None :

    signals = ParseInput(inputFile)
    
    # Part 1
    digits = [1, 4, 7, 8]
    occurences = 0
    for signal in signals:
        for num in digits:
            occurences += signal.GetDigitCountInOutput(num)
    print(occurences)
    
    # Part 2    
            
Main()