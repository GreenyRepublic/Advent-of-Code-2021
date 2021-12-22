from os import linesep
from typing import Tuple, Dict, List
import math

inputFile = "13_Origami_input.txt"
inputTestFile = "13_Origami_test_input.txt"

class Vector2:
    def __init__(self, xCoord : float, yCoord : float) -> None:
        self._x = xCoord
        self._y = yCoord
        self.length = math.sqrt(self._x ** 2 + self._y ** 2)

    def __sub__(self, other):
        return Vector2(self._x - other.x, self._y - other.y)
    
    def __add__(self, other):
        return Vector2(self._x + other.x, self._y + other.y)
    
    def __lt__(self, other)-> bool:
        return (self.MagnitudeSquared()) < (other.MagnitudeSquared())

    def __gt__(self, other)-> bool:
        return (self.MagnitudeSquared()) > (other.MagnitudeSquared())
    
    def __eq__(self, other) -> bool:
        return self.__hash__() == other.__hash__()

    def __mul__(self, factor : int):
        return Vector2(self._x * factor, self._y * factor)

    def __div__(self, factor : int):
        return Vector2(self._x / factor, self._y / factor)

    def __getitem__(self, key : int):
        if key == 0:
            return self._x
        return self._y

    def __setitem__(self, key : int, value) -> None:
        if key == 0:
            self._x = value
        else:
            self._y = value

    def __hash__(self):
        return hash(self.ToTuple())

    def RoundUp(self) -> None:
        self._x = math.ceil(self._x)
        self._y = math.ceil(self._y)

    def MagnitudeSquared(self) -> int:
        return self.length ** 2

    def Magnitude(self) -> float:
        return self.length

    def Normalised(self):
        if (abs(self._x) == abs(self._y)):
            return Vector2(self._x/abs(self._x), self._y/abs(self._y))
        return Vector2(math.ceil(self._x / self.Magnitude()), math.ceil(self._y / self.Magnitude()))

    def Dot(self, other):
        return (self._x * other.x) + (self._y * other.y)

    def ToTuple(self) -> Tuple[int,int]:
        return (int(self._x), int(self._y))

    def x(self) -> int:
        return self._x
    
    def y(self) -> int:
        return self._y