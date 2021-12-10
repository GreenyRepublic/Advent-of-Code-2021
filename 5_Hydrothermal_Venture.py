from os import linesep
from collections import defaultdict
from typing import List, Tuple
import math

inputFile = "5_Hydrothermal_Venture_input.txt"
testInputFile = "5_Hydrothermal_Venture_test_input.txt"

class Vector2:
    def __init__(self, xCoord : float, yCoord : float) -> None:
        self.x = xCoord
        self.y = yCoord
        self.length = math.sqrt(self.x ** 2 + self.y ** 2)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __lt__(self, other)-> bool:
        return (self.MagnitudeSquared()) < (other.MagnitudeSquared())

    def __gt__(self, other)-> bool:
        return (self.MagnitudeSquared()) > (other.MagnitudeSquared())
    
    def __eq__(self, other) -> bool:
        return not self < other and not self > other

    def RoundUp(self) -> None:
        self.x = math.ceil(self.x)
        self.y = math.ceil(self.y)

    def MagnitudeSquared(self) -> int:
        return self.length ** 2

    def Magnitude(self) -> float:
        return self.length

    def Normalised(self):
        if (abs(self.x) == abs(self.y)):
            return Vector2(self.x/abs(self.x), self.y/abs(self.y))
        return Vector2(math.ceil(self.x / self.Magnitude()), math.ceil(self.y / self.Magnitude()))
        

    def Dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def ToTuple(self) -> Tuple[int,int]:
        return (int(self.x), int(self.y))

    


class LineSegment:
    def __init__(self, start : Vector2, end : Vector2) -> None:
        self._startPoint = start
        self._endPoint = end
        self._length = (start - end).Magnitude()
        if (self._length == 0):
            self._directionVector = Vector2(0,0)
        else:
            self._directionVector = (self._endPoint - self._startPoint).Normalised()
            
    
    # Line section length
    def Length(self) -> float:
        return self._length
    
    # Normalised direction vector
    def Direction(self) -> Vector2:
        return self._directionVector

    def IsPointOnLine(self, point : Vector2) -> bool:
        tempSegment = LineSegment(self._startPoint, point)
        if tempSegment.Length() == 0:
            return True
        return tempSegment.Length() <= self.Length() and self._directionVector.Dot(tempSegment._directionVector) == 1

    # Is this line segment at 90 degrees to the reference vector?
    def IsOrthogonal(self, referenceVector : Vector2) -> bool:
        dotProd = self._directionVector.Dot(referenceVector.Normalised())
        return (dotProd == 0.0)
    
    def IsVertical(self) -> bool:
        return (self._startPoint.x == self._endPoint.x)

    def IsHorizontal(self) -> bool:
        return (self._startPoint.y == self._endPoint.y)

    def GetIntersections(self, other : 'LineSegment') -> List[Vector2]:
        currentPoint = self._startPoint
        intersections = []
        while not currentPoint > self._endPoint:
            if other.IsPointOnLine(currentPoint):
                intersections.append(currentPoint)
            currentPoint = currentPoint + self._directionVector

        return intersections
    
    # Lists the points that this line covers
    def EnumeratePoints(self) -> List[Vector2]:
        points = []
        currentPoint = self._startPoint
        for i in range(0, max(abs(self._startPoint.x - self._endPoint.x), abs(self._startPoint.y - self._endPoint.y)) + 1):
            points.append(Vector2(currentPoint.x, currentPoint.y))
            currentPoint += self._directionVector
        return points

def ParseCoordinateString(coord : str) -> Vector2:
    nums = coord.split(',')
    return Vector2(int(nums[0]), int(nums[1]))

def ParseInput(filename : str) -> List[LineSegment]:

    lines = open(filename).readlines()
    outSegments = []

    for line in lines: 
        splitLine = line.strip().split('->')
        coordA = ParseCoordinateString(splitLine[0])
        coordB = ParseCoordinateString(splitLine[1])
        outSegments.append(LineSegment(coordA, coordB))

    return outSegments

def Main() -> None :

    lineSegments = ParseInput(inputFile)
    
    # Part 1
    overlappingCoordsOne = defaultdict(int)
    verticalHorizontalSegments = [line for line in lineSegments if line.IsVertical() or line.IsHorizontal()]
    for line in verticalHorizontalSegments:
        for point in line.EnumeratePoints():
            overlappingCoordsOne[point.ToTuple()] += 1

    overlapTotal = 0
    for count in overlappingCoordsOne.values():
        if count >= 2:
            overlapTotal += 1
    print(overlapTotal)    

    # Part 2    
    linesDone = 0
    overlappingCoordsTwo = defaultdict(int)
    for line in lineSegments:
        points = line.EnumeratePoints()
        for point in points:
            overlappingCoordsTwo[point.ToTuple()] += 1
        linesDone += 1

    overlapTotal = 0
    for count in overlappingCoordsTwo.values():
        if count >= 2:
            overlapTotal += 1
            
    print(overlapTotal)
            
Main()