import numpy as np

from vehicle import Vehicle

DEFAULT_FUEL: int = 100
GOAL_POSITION = 17  # array position so like starting from 0


class Board:
    def __init__(self, puzzle: list[str]):
        self.board = list(puzzle[0])
        self.vehicles = self.__initializeVehicles(puzzle)

    def __str__(self) -> str:
        return self.board

    def printBoard(self):
        for index, cell in enumerate(self.board):
            if index % 6 == 5:
                print(cell)
            else:
                print(cell, end=' ')

    def getVehicleAtExit(self) -> Vehicle:
        return self.board[17]

    def printCars(self):
        for car in self.vehicles.values():
            print(car)

    def testCanMoveUp(self, letter):
        print(letter, "can move up : ", self.canMoveUp(letter))

    def testCanMoveDown(self, letter):
        print(letter, "can move down : ", self.canMoveDown(letter))

    def testCanMoveLeft(self, letter: str):
        print(letter, "can move left : ", self.canMoveLeft(letter))

    def testCanMoveRight(self, letter: str):
        print(letter, "can move right : ", self.canMoveRight(letter))

    # End Of Testing Functions

    def getFinalConfiguration(self) -> str:
        # print the 6x6
        pass

    # Create dictionary for vehicles (i.e. a set with key-value pairs ("Name", Vehicle))
    def __initializeVehicles(self, puzzle: list[str]):
        vehiclesDict = dict()

        # Initialize vehicles with default fuel amount
        for index, letter in enumerate(puzzle[0]):
            if letter != ".":
                if letter not in vehiclesDict:
                    if puzzle[0][index + 1] == letter:
                        vehiclesDict.update(
                            {letter: Vehicle(letter, puzzle[0].count(letter), DEFAULT_FUEL, [index], True)})
                    else:
                        vehiclesDict.update(
                            {letter: Vehicle(letter, puzzle[0].count(letter), DEFAULT_FUEL, [index], False)})
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
    def canMoveUp(self, vehicleLetterName: str, multiplier: int) -> bool:
        positions = self.vehicles.get(vehicleLetterName).getPositions()
        if positions[0] < 6:
            return False
        if positions[0] - 6 * multiplier < 0:
            return False
        if self.board[(positions[0] - 6 * multiplier)] != '.':
            return False
        else:
            return True

    def canMoveDown(self, vehicleLetterName: str, multiplier: int) -> bool:
        positions = self.vehicles.get(vehicleLetterName).getPositions()
        if positions[-1] > 29:
            return False
        if positions[-1] + 6 * multiplier > 35:
            return False
        if self.board[(positions[-1] + 6 * multiplier)] != '.':
            return False
        else:
            return True

    def canMoveLeft(self, vehicleLetterName: str, multiplier: int) -> bool:
        positions = self.vehicles.get(vehicleLetterName).getPositions()
        if positions[0] % 6 == 0:
            return False
        if self.board[positions[0] - multiplier] != '.':
            return False
        else:
            return True

    def canMoveRight(self, vehicleLetterName: str, multiplier: int) -> bool:
        positions = self.vehicles.get(vehicleLetterName).getPositions()
        if positions[-1] % 6 == 5:
            return False
        if self.board[positions[-1] + multiplier] != '.':
            return False
        else:
            return True

    # TODO include fuel modification
    def moveUp(self, vehicleLetterName: str, multiplier: int):
        updatePositions = self.vehicles.get(vehicleLetterName).getPositions()
        for index, x in enumerate(updatePositions):
            self.board[int(x)] = '.'
            updatePositions[index] = x - 6
        for x in updatePositions:
            self.board[x] = vehicleLetterName
        self.vehicles.get(vehicleLetterName).setPositions(updatePositions)
        return True

    def moveDown(self, vehicleLetterName: str, multiplier: int):
        updatePositions = self.vehicles.get(vehicleLetterName).getPositions()
        for index, x in enumerate(updatePositions):
            self.board[int(x)] = '.'
            updatePositions[index] = x + 6 * multiplier
        for x in updatePositions:
            self.board[x] = vehicleLetterName
        self.vehicles.get(vehicleLetterName).setPositions(updatePositions)
        return True

    def moveLeft(self, vehicleLetterName: str, multiplier: int):
        updatePositions = self.vehicles.get(vehicleLetterName).getPositions()
        for index, x in enumerate(updatePositions):
            self.board[int(x)] = '.'
            updatePositions[index] = x - 1 * multiplier
        for x in updatePositions:
            self.board[x] = vehicleLetterName
        self.vehicles.get(vehicleLetterName).setPositions(updatePositions)
        return True

    def moveRight(self, vehicleLetterName: str, multiplier: int):
        updatePositions = self.vehicles.get(vehicleLetterName).getPositions()
        for index, x in enumerate(updatePositions):
            self.board[int(x)] = '.'
            updatePositions[index] = x + 1 * multiplier
        for x in updatePositions:
            self.board[x] = vehicleLetterName
        self.vehicles.get(vehicleLetterName).setPositions(updatePositions)
        return True

    def allPossibleMoves(self):
        print(self.printBoard())
        for vehicle in self.vehicles.values():
            if vehicle.getIsHorizontal():
                i = 1
                while i < 4:
                    if self.canMoveRight(vehicle.letterName, i):
                        board = Board([self.board])
                        board.moveRight(vehicle.letterName, i)
                        print(board.printBoard())
                        i += 1
                    else:
                        break
                i = 1
                while i < 4:
                    if self.canMoveLeft(vehicle.letterName, i):
                        board = Board([self.board])
                        board.moveLeft(vehicle.letterName, i)
                        print(board.printBoard())
                        i += 1
                    else:
                        break

            if not vehicle.getIsHorizontal():
                i = 1
                while i < 4:
                    if self.canMoveDown(vehicle.letterName, i):
                        board = Board([self.board])
                        board.moveDown(vehicle.letterName, i)
                        print(board.printBoard())
                        i += 1
                    else:
                        break
                i = 1
                while i < 4:
                    if self.canMoveUp(vehicle.letterName, i):
                        board = Board([self.board])
                        board.moveUp(vehicle.letterName, i)
                        print(board.printBoard())
                        i += 1
                    else:
                        break
