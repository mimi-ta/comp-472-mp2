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

    def printCars(self):
        print(self.vehicles)

    # Create dictionary for vehicles (i.e. a set with key-value pairs ("Name", Vehicle))
    def __initializeVehicles(self, puzzle: list[str]):
        vehiclesDict = dict()

        # Initialize vehicles with default fuel amount
        for index, letter in enumerate(puzzle[0]):
            if letter != ".":
                if letter not in vehiclesDict:
                    if puzzle[0][index+1] == letter:
                        vehiclesDict.update({letter: Vehicle(letter, puzzle[0].count(letter), DEFAULT_FUEL, [index], True)})
                    else:
                        vehiclesDict.update({letter: Vehicle(letter, puzzle[0].count(letter), DEFAULT_FUEL, [index], False)})
                elif letter != '.':
                    positions = vehiclesDict.get(letter).getPositions()
                    positions.append(index)
                    vehiclesDict.get(letter).setPositions(positions)

        # Look for fuel definitions and if present then set them
        for fuelDefinition in puzzle[1:]:
            vehiclesDict.get(fuelDefinition[0]).setRemainingFuel(
                int(fuelDefinition[1:])
            )

        return vehiclesDict


    # TODO: Implement all these
    # Only moves up one spot atm ( logically, haven't tested)
    def canMoveUp(self, vehicleLetterName: str, puzzle: str) -> bool:
        if not self.vehicles.get(vehicleLetterName).getIsHorizontal():
            positions = self.vehicles.get(vehicleLetterName).getPositions()
            if positions[0] < 6:
                return False
            if puzzle[(positions[0] - 6)] != '.':
                return False
            else:
                return True
        return False

    def canMoveDown(self, vehicleLetterName: str, puzzle: str) -> bool:
        if not self.vehicles.get(vehicleLetterName).getIsHorizontal():
            positions = self.vehicles.get(vehicleLetterName).getPositions()
            if positions[-1] > 29:
                return False
            if puzzle[(positions[-1] + 6)] != '.':
                return False
            else:
                return True
        return False

    def canMoveLeft(self, vehicleLetterName: str, puzzle: str) -> bool:
        if self.vehicles.get(vehicleLetterName).getIsHorizontal():
            positions = self.vehicles.get(vehicleLetterName).getPositions()
            if positions[0] % 6 == 0:
                return False
            if puzzle(positions[0] - 1) != '.':
                return False
            else:
                return True
        return False

    def canMoveRight(self, vehicleLetterName: str, puzzle: str) -> bool:
        if self.vehicles.get(vehicleLetterName).getIsHorizontal():
            positions = self.vehicles.get(vehicleLetterName).getPositions()
            if positions[-1] % 6 == 5:
                return False
            if puzzle(positions[-1] + 1) != '.':
                return False
            else:
                return True
        return False

    # TODO include fuel modification
    def moveUp(self, vehicleLetterName: str, puzzle: str):
        if self.canMoveUp(vehicleLetterName):
            updatePositions = self.vehicles.get(vehicleLetterName).getPositions()
            for index, x in enumerate(updatePositions):
                updatePositions[index] = x + 6
            self.vehicles.get(vehicleLetterName).setPositions(updatePositions)

        pass

    def moveDown(self, vehicleLetterName: str):
        if self.canMoveDown(vehicleLetterName):
            updatePositions = self.vehicles.get(vehicleLetterName).getPositions()
            for index, x in enumerate(updatePositions):
                updatePositions[index] = x - 6
            self.vehicles.get(vehicleLetterName).setPositions(updatePositions)
        pass

    def moveLeft(self, vehicleLetterName: str):
        if self.canMoveLeft(vehicleLetterName):
            updatePositions = self.vehicles.get(vehicleLetterName).getPositions()
            for index, x in enumerate(updatePositions):
                updatePositions[index] = x - 1
            self.vehicles.get(vehicleLetterName).setPositions(updatePositions)
        pass

    def moveRight(self, vehicleLetterName: str):
        if self.canMoveRight(vehicleLetterName):
            updatePositions = self.vehicles.get(vehicleLetterName).getPositions()
            for index, x in enumerate(updatePositions):
                updatePositions[index] = x + 1
            self.vehicles.get(vehicleLetterName).setPositions(updatePositions)
        pass

    def allPossibleMoves(self):
        pass