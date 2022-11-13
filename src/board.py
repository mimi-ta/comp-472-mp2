import numpy as np

from position import Position
from vehicle import Vehicle

class Board:
    def __init__(self, puzzle: list[str]):
      self.board = np.array(list(puzzle[0])).reshape(6,6)

    def __str__(self) -> str:
      return np.array2string(self.board)

    def __initializeVehicles(self, puzzle: list[str]):
      vehiclesDict = dict()
      for letter in puzzle[0]:
        if letter not in vehiclesDict:
          vehiclesDict.update({letter: Vehicle(letter, "infinite")})
      
      for fuelDefinition in puzzle[1:]:
          vehiclesDict.get(fuelDefinition[0]).setRemainingFuel(int(fuelDefinition[1:]))

      return vehiclesDict
        
    def __initializePositions(self, puzzleConfiguration: str) -> list[Position]:
      pass
