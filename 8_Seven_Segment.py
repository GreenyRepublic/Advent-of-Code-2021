from os import linesep
from collections import defaultdict
from typing import List, Tuple, DefaultDict

inputFile = "8_Seven_segment_input.txt"

DIGIT_SEGMENT_COUNTS = {
    2: [1],
    3: [7],
    4: [4],
    5: [2,3,5],
    6: [0, 6, 9],
    7: [8]
}

UNIQUE_DIGIT_SIZES = {
    2 : 1,
    4 : 4,
    3 : 7,
    7 : 8
}

DISPLAY_SEGMENTS = {
    "top",
    "middle",
    "bottom",
    "left_up",
    "left_down",
    "right_up",
    "right_down"
}

DIGIT_SEGMENT_MAPPINGS = {
    0 : {"top", "bottom", "right_up", "right_down", "left_up", "left_down"},
    1 : {"right_up", "right_down"},
    2 : {"top", "right_up", "middle", "left_down", "bottom"},
    3 : {"top", "right_up", "middle", "right_down", "bottom"},
    4 : {"left_up", "middle", "right_up", "right_down"},
    5 : {"top", "left_up", "middle", "right_down", "bottom"},
    6 : {"top", "left_up", "middle", "left_down", "right_down", "bottom"},
    7 : {"top", "right_up", "right_down"},
    8 : {"top", "middle", "bottom", "left_up", "left_down", "right_up", "right_down"},
    9 : {"top", "right_up", "left_up", "middle", "right_down", "bottom"},
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

        self._segments = {}
        for key in DISPLAY_SEGMENTS:
            self._segments[key] = {'a','b','c','d','g','e','f'}
        

    def GetUniqueDigitCountInOutput(self, digit : int) -> int:
        count = 0
        for num in self._displayedDigits:
            if len(num) in UNIQUE_DIGIT_SIZES.keys() and UNIQUE_DIGIT_SIZES[len(num)] == digit:
                count += 1
        return count

    # Parse the mapping of input letters to their 'actual' segments
    def ComputeMapping(self):
        for code in self._inputCodes:
            charSet = set()
            for char in code: 
                charSet.add(char)

            possibleDigits = DIGIT_SEGMENT_COUNTS[len(code)]
            for digit in possibleDigits:
                for segment in DIGIT_SEGMENT_MAPPINGS[digit]:
                    self._segments[segment].intersection_update(charSet)
        
        
        print(self._segments)

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
            occurences += signal.GetUniqueDigitCountInOutput(num)
    print(occurences)
    
    # Part 2
    signals[0].ComputeMapping()
            
Main()