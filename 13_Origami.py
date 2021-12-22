from os import linesep, write
from typing import Tuple, List
from Vector import Vector2

inputFile = "13_Origami_input.txt"
testInputFile = "13_Origami_test_input.txt"

class DotGrid:
    def __init__(self, squares: List[Vector2]) -> None:
        self._width = 0
        self._height = 0
        self._markedSquares = set()
        for square in squares:
            self._markedSquares.add(square)
            if square[0] > self._width:
                self._width = square[0]
            if square[1] > self._height:
                self._height = square[1]
        
    def MakeFold(self, fold : Vector2) -> None:
        foldAxis = int(fold[0] == 0)
        otherAxis = int(not foldAxis)
        newSquareSet = set()
        for item in self._markedSquares:
            distanceToFold = item[foldAxis] - fold[foldAxis]
            if distanceToFold > 0:
                newVec = Vector2(0,0)
                newVec[foldAxis] = item[foldAxis] - (distanceToFold * 2)
                newVec[otherAxis] = item[otherAxis]
                newSquareSet.add(newVec)
            else:
                newSquareSet.add(item)
        
        self._markedSquares = newSquareSet

    
    def GetDottedSquares(self) -> List[Tuple[int,int]]:
        return list(self._markedSquares)

    def PrintGrid(self) -> List[str]:
        output = []
        for i in range(0,self._height):
            row = ""
            for j in range(0, self._width):
                if Vector2(j,i) in self._markedSquares:
                    row += '#'
                else:
                    row += '_'
            output.append(row)
        return output


def ParseInput(filename : str) -> Tuple[List[Vector2], List[Vector2]]:    

    file = open(filename)
    coords = []
    folds = []
    lineBreak = False

    for line in file.readlines():
        if len(line.strip()) == 0:
            lineBreak = True
            continue

        if lineBreak:
            parsed = line.removeprefix("fold along").strip().split('=')
            axis = parsed[0]
            value = int(parsed[1])
            if axis == 'x':
                folds.append(Vector2(value, 0))
            else:
                folds.append(Vector2(0, value))

        else:
            split = line.strip().split(',')
            coords.append(Vector2(int(split[0]),int(split[1])))
        

    return coords, folds

def Main() -> None :
    coords, folds = ParseInput(inputFile)
    dotGrid = DotGrid(coords)

    # Part 1
    dotGrid.MakeFold(folds[0])
    print(len(dotGrid.GetDottedSquares()))
    
    # Part 2
    for fold in folds[0:]:
        dotGrid.MakeFold(fold)
    grid = dotGrid.PrintGrid()

    
Main()