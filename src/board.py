import numpy as np

from vehicle import Vehicle

DEFAULT_FUEL: int = 100


class Board:
    def __init__(self, puzzle: list[str]):
        self.board = puzzle[0]
        self.vehicles = self.__initializeVehicles(puzzle)

    def __str__(self) -> str:
        return self.board

    def getFinalConfiguration(self) -> str:
        # print the 6x6
        pass

    # Create dictionary for vehicles (i.e. a set with key-value pairs ("Name", Vehicle))
    def __initializeVehicles(self, puzzle: list[str]):
        vehiclesDict = dict()

        # Initialize vehicles with default fuel amount
        for letter in puzzle[0]:
            if letter not in vehiclesDict:
                vehiclesDict.update({letter: Vehicle(letter, puzzle[0].count(letter), DEFAULT_FUEL)})

        # Look for fuel definitions and if present then set them
        for fuelDefinition in puzzle[1:]:
            vehiclesDict.get(fuelDefinition[0]).setRemainingFuel(
                int(fuelDefinition[1:])
            )

        return vehiclesDict