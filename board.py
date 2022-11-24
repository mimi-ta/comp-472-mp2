import copy

import numpy as np

from vehicle import Vehicle

DEFAULT_FUEL: int = 100
GOAL_POSITION = 17  # array position so like starting from 0


class Board:
    def __init__(self, puzzle: list[str]):
        self.board = list(puzzle[0])
        self.vehicles = self.__initializeVehicles(puzzle)
        self.move = ""

    def __str__(self) -> str:
        return "".join(self.board)

    def boardToString(self) -> str:
        output = ""
        for index, cell in enumerate(self.board):
            if index % 6 == 5:
                output += cell + "\n"
            else:
                output += cell + " "
        return output

    def getVehicleAtExit(self) -> str:
        return self.board[17]

    def carsToString(self) -> str:
        output = ""
        for car in self.vehicles.values():
            output += car.__str__() + "\n"
        return output

    def testCanMoveUp(self, letter):
        print(letter, "can move up : ", self.__canMoveUp(letter))

    def testCanMoveDown(self, letter):
        print(letter, "can move down : ", self.__canMoveDown(letter))

    def testCanMoveLeft(self, letter: str):
        print(letter, "can move left : ", self.__canMoveLeft(letter))

    def testCanMoveRight(self, letter: str):
        print(letter, "can move right : ", self.__canMoveRight(letter))

    # End Of Testing Functions

    # Create dictionary for vehicles (i.e. a set with key-value pairs ("Name", Vehicle))
    def __initializeVehicles(self, puzzle: list[str]):
        vehiclesDict = dict()

        # Initialize vehicles with default fuel amount
        for index, letter in enumerate(puzzle[0]):
            if letter != ".":
                if letter not in vehiclesDict:
                    if puzzle[0][index + 1] == letter:
                        vehiclesDict.update(
                            {
                                letter: Vehicle(
                                    letter,
                                    puzzle[0].count(letter),
                                    DEFAULT_FUEL,
                                    [index],
                                    True,
                                )
                            }
                        )
                    else:
                        vehiclesDict.update(
                            {
                                letter: Vehicle(
                                    letter,
                                    puzzle[0].count(letter),
                                    DEFAULT_FUEL,
                                    [index],
                                    False,
                                )
                            }
                        )
                elif letter != ".":
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
    def __canMoveUp(self, vehicleLetterName: str, multiplier: int) -> bool:
        if self.vehicles.get(vehicleLetterName).getRemainingFuel() < multiplier:
            return False
        positions = self.vehicles.get(vehicleLetterName).getPositions()
        if positions[0] < 6:
            return False
        if positions[0] - 6 * multiplier < 0:
            return False
        if self.board[(positions[0] - 6 * multiplier)] != ".":
            return False
        else:
            return True

    def __canMoveDown(self, vehicleLetterName: str, multiplier: int) -> bool:
        if self.vehicles.get(vehicleLetterName).getRemainingFuel() < multiplier:
            return False
        positions = self.vehicles.get(vehicleLetterName).getPositions()
        if positions[-1] > 29:
            return False
        if positions[-1] + 6 * multiplier > 35:
            return False
        if self.board[(positions[-1] + 6 * multiplier)] != ".":
            return False
        else:
            return True

    def __canMoveLeft(self, vehicleLetterName: str, multiplier: int) -> bool:
        if self.vehicles.get(vehicleLetterName).getRemainingFuel() < multiplier:
            return False
        positions = self.vehicles.get(vehicleLetterName).getPositions()
        if (positions[0] - multiplier + 1) % 6 == 0:
            return False
        if self.board[positions[0] - multiplier] != ".":
            return False
        else:
            return True

    def __canMoveRight(self, vehicleLetterName: str, multiplier: int) -> bool:
        if self.vehicles.get(vehicleLetterName).getRemainingFuel() < multiplier:
            return False
        positions = self.vehicles.get(vehicleLetterName).getPositions()
        if (positions[-1] + multiplier - 1) % 6 == 5:
            return False
        if self.board[positions[-1] + multiplier] != ".":
            return False
        else:
            return True

    def moveUp(self, vehicleLetterName: str, multiplier: int):
        updatePositions = self.vehicles.get(vehicleLetterName).getPositions()
        for index, x in enumerate(updatePositions):
            self.board[int(x)] = "."
            updatePositions[index] = x - 6 * multiplier
        for x in updatePositions:
            self.board[x] = vehicleLetterName
        self.vehicles.get(vehicleLetterName).setPositions(updatePositions)
        self.vehicles.get(vehicleLetterName).setRemainingFuel(
            self.vehicles.get(vehicleLetterName).getRemainingFuel() - multiplier
        )
        self.move = f"{vehicleLetterName} Up {multiplier}\t{self.vehicles.get(vehicleLetterName).getRemainingFuel()} ${self.__str__()}"
        return True

    def moveDown(self, vehicleLetterName: str, multiplier: int):
        updatePositions = self.vehicles.get(vehicleLetterName).getPositions()
        for index, x in enumerate(updatePositions):
            self.board[int(x)] = "."
            updatePositions[index] = x + 6 * multiplier
        for x in updatePositions:
            self.board[x] = vehicleLetterName
        self.vehicles.get(vehicleLetterName).setPositions(updatePositions)
        self.vehicles.get(vehicleLetterName).setRemainingFuel(
            self.vehicles.get(vehicleLetterName).getRemainingFuel() - multiplier
        )
        self.move = f"{vehicleLetterName} Down {multiplier}\t{self.vehicles.get(vehicleLetterName).getRemainingFuel()} ${self.__str__()}"
        return True

    def moveLeft(self, vehicleLetterName: str, multiplier: int):
        updatePositions = self.vehicles.get(vehicleLetterName).getPositions()
        for index, x in enumerate(updatePositions):
            self.board[int(x)] = "."
            updatePositions[index] = x - 1 * multiplier
        for x in updatePositions:
            self.board[x] = vehicleLetterName
        self.vehicles.get(vehicleLetterName).setPositions(updatePositions)
        self.vehicles.get(vehicleLetterName).setRemainingFuel(
            self.vehicles.get(vehicleLetterName).getRemainingFuel() - multiplier
        )
        self.move = f"{vehicleLetterName} Left {multiplier}\t{self.vehicles.get(vehicleLetterName).getRemainingFuel()} ${self.__str__()}"
        return True

    def moveRight(self, vehicleLetterName: str, multiplier: int):
        updatePositions = self.vehicles.get(vehicleLetterName).getPositions()
        for index, x in enumerate(updatePositions):
            self.board[int(x)] = "."
            updatePositions[index] = x + 1 * multiplier
        for x in updatePositions:
            self.board[x] = vehicleLetterName
        self.vehicles.get(vehicleLetterName).setPositions(updatePositions)
        self.vehicles.get(vehicleLetterName).setRemainingFuel(
            self.vehicles.get(vehicleLetterName).getRemainingFuel() - multiplier
        )
        self.move = f"{vehicleLetterName} Right {multiplier}\t{self.vehicles.get(vehicleLetterName).getRemainingFuel()} {self.__str__()}"

        # remove car from board if it is in the goalstate
        if updatePositions[-1] == 17 and vehicleLetterName != "A":
            for index, x in enumerate(updatePositions):
                self.board[int(x)] = "."
            self.vehicles.pop(vehicleLetterName)
        return True

    def allPossibleMoves(self):
        moves = []
        for vehicle in self.vehicles.values():
            if vehicle.getIsHorizontal():
                i = 1
                while i < 5:
                    if self.__canMoveRight(vehicle.letterName, i):
                        board = copy.deepcopy(self)
                        board.moveRight(vehicle.letterName, i)
                        moves.append(board)
                        i += 1
                    else:
                        break
                i = 1
                while i < 5:
                    if self.__canMoveLeft(vehicle.letterName, i):
                        board = copy.deepcopy(self)
                        board.moveLeft(vehicle.letterName, i)
                        moves.append(board)
                        i += 1
                    else:
                        break

            if not vehicle.getIsHorizontal():
                i = 1
                while i < 5:
                    if self.__canMoveDown(vehicle.letterName, i):
                        board = copy.deepcopy(self)
                        board.moveDown(vehicle.letterName, i)
                        moves.append(board)
                        i += 1
                    else:
                        break
                i = 1
                while i < 5:
                    if self.__canMoveUp(vehicle.letterName, i):
                        board = copy.deepcopy(self)
                        board.moveUp(vehicle.letterName, i)
                        moves.append(board)
                        i += 1
                    else:
                        break
        return moves