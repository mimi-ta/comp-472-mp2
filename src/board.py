import numpy as np

from position import Position
from vehicle import Vehicle

DEFAULT_FUEL: int = 100


class Board:
    def __init__(self, puzzle: list[str]):
        self.board = np.empty(dtype=np.dtype(Position), shape=(6, 6))
        self.vehicles = self.__initializeVehicles(puzzle)
        self.__initializePositions(puzzleConfiguration=puzzle[0])

    def __str__(self) -> str:
        output = ""
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                output += self.board[i][j].__str__() + " "
            output += "\n"
        return output.strip()

    # Create dictionary for vehicles (i.e. a set with key-value pairs ("Name", Vehicle))
    def __initializeVehicles(self, puzzle: list[str]):
        vehiclesDict = dict()

        # Initialize vehicles with default fuel amount
        for letter in puzzle[0]:
            if letter not in vehiclesDict:
                vehiclesDict.update({letter: Vehicle(letter, DEFAULT_FUEL)})

        # Look for fuel definitions and if present then set them
        for fuelDefinition in puzzle[1:]:
            vehiclesDict.get(fuelDefinition[0]).setRemainingFuel(
                int(fuelDefinition[1:])
            )

        return vehiclesDict

    def __initializePositions(self, puzzleConfiguration: str):
        puzzleConfigurationAs6x6 = np.array_split(list(puzzleConfiguration), 6)

        # Traverse all puzzle position by position, initialize board
        for i in range(len(puzzleConfigurationAs6x6)):
            for j in range(len(puzzleConfigurationAs6x6)):
                letterName = puzzleConfigurationAs6x6[i][j]
                self.board[i][j] = Position(self.vehicles.get(letterName), j + 1, i + 1)
