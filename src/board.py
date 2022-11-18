import numpy as np

from vehicle import Vehicle

DEFAULT_FUEL: int = 100
GOAL_POSITION = 17 # array position so like starting from 0

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
    
    # TODO: Implement all these
    # Only moves up one spot atm ( logically, haven't tested)
    def canMoveUp(self, vehicleLetterName: str, puzzle: str) -> bool:
        if self.vehicles.get(vehicleLetterName).isVertical():
            positions = []
            for index, x in enumerate(puzzle):
                if x == vehicleLetterName:
                    positions.append(index)
            if positions[0] < 6:
                return False
            if puzzle[(positions[0] - 6)] != '.':
                return False
            else:
                return True
        return False

    def canMoveDown(self, vehicleLetterName: str, puzzle: str) -> bool:
        if self.vehicles.get(vehicleLetterName).isVertical():
            positions = []
            for index, x in enumerate(puzzle):
                if x == vehicleLetterName:
                    positions.append(index)
            if positions[-1] > 29:
                return False
            if puzzle[(positions[-1] + 6)] != '.':
                return False
            else:
                return True
        return False

    def canMoveLeft(self, vehicleLetterName: str, puzzle: str) -> bool:
        if not self.vehicles.get(vehicleLetterName).isVertical():
            positions = []
            for index, x in enumerate(puzzle):
                if x == vehicleLetterName:
                    positions.append(index)
            if positions[0]%6 == 0:
                return False
            if puzzle(positions[0] - 1) != '.':
                return False
            else:
                return True
        return False

    def canMoveRight(self, vehicleLetterName: str, puzzle: str) -> bool:
        if not self.vehicles.get(vehicleLetterName).isVertical():
            positions = []
            for index, x in enumerate(puzzle):
                if x == vehicleLetterName:
                    positions.append(index)
            if positions[0] % 6 == 5:
                return False
            if puzzle(positions[0] + 1) != '.':
                return False
            else:
                return True
        return False

    def moveUp(self, vehicleLetterName: str):
        if self.canMoveUp(vehicleLetterName):
            pass
        pass

    def moveDown(self, vehicleLetterName: str):
        if self.canMoveDown(vehicleLetterName):
            pass
        pass

    def moveLeft(self, vehicleLetterName: str):
        if self.canMoveLeft(vehicleLetterName):
            pass
        pass

    def moveRight(self, vehicleLetterName: str):
        if self.canMoveRight(vehicleLetterName):
            pass
        pass