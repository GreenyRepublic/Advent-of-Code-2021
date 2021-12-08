import sys
import io
import numpy
from numpy.core import numeric
from numpy.core.numeric import False_

inputFile = "4_Giant_Squid_input.txt"
testInputFile = "4_test_input.txt"

class BingoBoard:
    def __init__(self, grid : 'list[str]') -> None:
        self._GridWidth = 5
        self._GridSquares = dict()
        self._MarkedSquares = [[False] * self._GridWidth for i in range(self._GridWidth)]
        self._PopulateGrid(grid)

    def _PopulateGrid(self, grid : 'list[str]'):
        for x in range(0, self._GridWidth):
            line = grid[x].split()
            for y in range(0,self._GridWidth):
                key = int(line[y])
                self._GridSquares[key] = (x,y)

    def _IsRowWinner(self, row : int) -> True:
        for cell in self._MarkedSquares[row]:
            if not cell:
                return False
        return True

    def _IsColumnWinner(self, col : int) -> True:
        for row in self._MarkedSquares:
            if not row[col]:
                return False
        return True

    def MarkNumber(self, num : int) -> bool:
        if num in self._GridSquares.keys():
            coords = self._GridSquares[num]
            self._MarkedSquares[coords[0]][coords[1]] = True
            return self.HasWon()
        return False

    def HasWon(self) -> bool:
        for i in range(0,self._GridWidth):
            if self._IsColumnWinner(i) or self._IsRowWinner(i):
                return True
        return False

    def GetUnmarkedNumberSum(self) -> int:
        sum = 0
        for number, coord in self._GridSquares.items():
            if self._MarkedSquares[coord[0]][coord[1]] == False:
                sum += number

        return sum

def UpdateGrids(grids : 'list[BingoBoard]', num : int) -> 'list[BingoBoard]':
    winners = []
    for grid in grids:
        winnerFound = grid.MarkNumber(num)
        if winnerFound:
            winners.append(grid)

    return winners

def SquidGame(numberSequence : 'list[int]', grids : 'list[BingoBoard]', getLast : bool = False) -> 'list[tuple[int, BingoBoard]]':

    winners = []    
    for number in numberSequence:
        thisRound = UpdateGrids(grids, number)
        for grid in thisRound:
            winners.append((number, grid))
            grids.remove(grid)

    return winners

def ParseInput(filename : str) -> 'tuple[int, list[BingoBoard]]':

    lines = open(filename).readlines()
    
    numberList = list(map(int, lines[0].split(',')))
    gridList = []
    currentGrid = []

    for line in lines[2:]:
        if len(line.strip()) == 0: # Hit an empty line
            gridList.append(BingoBoard(currentGrid))
            currentGrid.clear()
            continue
        currentGrid.append(line.strip())
    
    gridList.append(BingoBoard(currentGrid)) # Catch the last line/EOF
    return numberList, gridList

def Main():

    numberSequence, grids = ParseInput(inputFile)

    winners = SquidGame(numberSequence, grids, False)

    # Part 1
    firstNum, firstGrid = winners[0]
    sum = firstGrid.GetUnmarkedNumberSum()
    print(sum * firstNum)

    # Part 2
    lastNum, lastGrid = winners[-1]
    sum = lastGrid.GetUnmarkedNumberSum()
    print(sum * lastNum)
            
Main()