from copy import copy

from vehicle import Vehicle

DEFAULT_FUEL: int = 100


class Board:
    def __init__(self, puzzle: list[str], cars=None):
        if puzzle:
            self.board = list(puzzle[0])
        else:
            self.board = []
        self.vehicles = cars or self.initializeVehicles(puzzle)
        self.move = ""

    def __str__(self) -> str:
        return "".join(self.board)

    def __copy__(self):
        tempBoard = Board(None, None)
        tempBoard.board = [str(element) for element in self.board]
        tempBoard.vehicles = {key: copy(value) for key, value in self.vehicles.items()}
        return tempBoard

    def boardToString(self) -> str:
        output = ""
        for index, cell in enumerate(self.board):
            if index % 6 == 5:
                output += cell + "\n"
            else:
                output += cell + " "
        return output

    def getAllCarFuels(self) -> str:
        output = ""
        for car in self.vehicles.values():
            output += car.getFuelString() + " "
        return output

    def getVehicleAtExit(self) -> str:
        return self.board[17]

    # Create dictionary for vehicles (i.e. a set with key-value pairs ("Name", Vehicle))
    def initializeVehicles(self, puzzle: list[str]):
        if puzzle:
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
                                        True,
                                        index,
                                        (puzzle[0].count(letter) + index) - 1,
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
                                        False,
                                        index,
                                        (puzzle[0].count(letter) - 1) * 6 + index,
                                    )
                                }
                            )

            # Look for fuel definitions and if present then set them
            for fuelDefinition in puzzle[1:]:
                vehiclesDict.get(fuelDefinition[0]).remainingFuel = int(
                    fuelDefinition[1:]
                )
            return vehiclesDict
        else:
            return dict()

    def canMoveUp(self, vehicleLetterName: str, multiplier: int) -> bool:
        vehicle = self.vehicles.get(vehicleLetterName)
        if vehicle.remainingFuel < multiplier:
            return False
        head = vehicle.head
        if head < 6:
            return False
        if head - 6 * multiplier < 0:
            return False
        if self.board[(head - 6 * multiplier)] != ".":
            return False
        else:
            return True

    def canMoveDown(self, vehicleLetterName: str, multiplier: int) -> bool:
        vehicle = self.vehicles.get(vehicleLetterName)
        if vehicle.remainingFuel < multiplier:
            return False
        tail = vehicle.tail
        if tail > 29:
            return False
        if tail + 6 * multiplier > 35:
            return False
        if self.board[(tail + 6 * multiplier)] != ".":
            return False
        else:
            return True

    def canMoveLeft(self, vehicleLetterName: str, multiplier: int) -> bool:
        vehicle = self.vehicles.get(vehicleLetterName)
        if vehicle.remainingFuel < multiplier:
            return False
        head = vehicle.head
        if (head - multiplier + 1) % 6 == 0:
            return False
        if self.board[head - multiplier] != ".":
            return False
        else:
            return True

    def canMoveRight(self, vehicleLetterName: str, multiplier: int) -> bool:
        vehicle = self.vehicles.get(vehicleLetterName)
        if vehicle.remainingFuel < multiplier:
            return False
        tail = vehicle.tail
        if (tail + multiplier - 1) % 6 == 5:
            return False
        if self.board[tail + multiplier] != ".":
            return False
        else:
            return True

    def moveUp(self, vehicleLetterName: str, multiplier: int):
        vehicle = self.vehicles.get(vehicleLetterName)
        newHead = vehicle.head - multiplier * 6
        newTail = vehicle.tail - multiplier * 6
        size = vehicle.size

        if multiplier == 1:
            self.board[vehicle.tail] = "."
            self.board[newHead] = vehicleLetterName
        elif multiplier == 2:
            self.board[vehicle.tail] = "."
            self.board[vehicle.tail - 6] = "."
            self.board[vehicle.head - 6] = vehicleLetterName
            self.board[newHead] = vehicleLetterName
        else:
            if size == 3:
                self.board[vehicle.tail] = "."
                self.board[vehicle.tail - 6] = "."
                self.board[vehicle.head] = "."
                self.board[newTail] = vehicleLetterName
                self.board[newTail - 6] = vehicleLetterName
                self.board[newHead] = vehicleLetterName
            elif size == 2:
                self.board[vehicle.tail] = "."
                self.board[vehicle.head] = "."
                self.board[newHead] = vehicleLetterName
                self.board[newTail] = vehicleLetterName

        vehicle.head = newHead
        vehicle.tail = newTail

        vehicle.remainingFuel = vehicle.remainingFuel - multiplier
        self.move = f"{vehicleLetterName} Up {multiplier}\t\t{vehicle.remainingFuel} {self.__str__()}"

    def moveDown(self, vehicleLetterName: str, multiplier: int):
        vehicle = self.vehicles.get(vehicleLetterName)
        newHead = vehicle.head + multiplier * 6
        newTail = vehicle.tail + multiplier * 6
        size = vehicle.size

        if multiplier == 1:
            self.board[vehicle.head] = "."
            self.board[newTail] = vehicleLetterName
        elif multiplier == 2:
            self.board[vehicle.head] = "."
            self.board[vehicle.head + 6] = "."
            self.board[vehicle.tail + 6] = vehicleLetterName
            self.board[newTail] = vehicleLetterName
        else:
            if size == 3:
                self.board[vehicle.head] = "."
                self.board[vehicle.head + 6] = "."
                self.board[vehicle.tail] = "."
                self.board[newTail] = vehicleLetterName
                self.board[newHead + 6] = vehicleLetterName
                self.board[newHead] = vehicleLetterName
            elif size == 2:
                self.board[vehicle.tail] = "."
                self.board[vehicle.head] = "."
                self.board[newHead] = vehicleLetterName
                self.board[newTail] = vehicleLetterName

        vehicle.head = newHead
        vehicle.tail = newTail

        vehicle.remainingFuel = vehicle.remainingFuel - multiplier
        self.move = f"{vehicleLetterName} Down {multiplier}\t{vehicle.remainingFuel} {self.__str__()}"

    def moveLeft(self, vehicleLetterName: str, multiplier: int):
        vehicle = self.vehicles.get(vehicleLetterName)
        newHead = vehicle.head - multiplier
        newTail = vehicle.tail - multiplier
        size = vehicle.size

        if multiplier == 1:
            self.board[vehicle.tail] = "."
            self.board[newHead] = vehicleLetterName
        elif multiplier == 2:
            self.board[vehicle.tail] = "."
            self.board[vehicle.tail - 1] = "."
            self.board[vehicle.head - 1] = vehicleLetterName
            self.board[newHead] = vehicleLetterName
        else:
            if size == 3:
                self.board[vehicle.tail] = "."
                self.board[vehicle.tail - 1] = "."
                self.board[vehicle.head] = "."
                self.board[newHead] = vehicleLetterName
                self.board[newTail - 1] = vehicleLetterName
                self.board[newTail] = vehicleLetterName
            elif size == 2:
                self.board[vehicle.tail] = "."
                self.board[vehicle.head] = "."
                self.board[newHead] = vehicleLetterName
                self.board[newTail] = vehicleLetterName

        vehicle.head = newHead
        vehicle.tail = newTail

        vehicle.remainingFuel = vehicle.remainingFuel - multiplier
        self.move = f"{vehicleLetterName} Left {multiplier}\t{vehicle.remainingFuel} {self.__str__()}"

    def moveRight(self, vehicleLetterName: str, multiplier: int):
        vehicle = self.vehicles.get(vehicleLetterName)
        newHead = vehicle.head + multiplier
        newTail = vehicle.tail + multiplier
        size = vehicle.size

        if multiplier == 1:
            self.board[vehicle.head] = "."
            self.board[newTail] = vehicleLetterName
        elif multiplier == 2:
            self.board[vehicle.head] = "."
            self.board[vehicle.head + 1] = "."
            self.board[vehicle.tail + 1] = vehicleLetterName
            self.board[newTail] = vehicleLetterName
        else:
            if size == 3:
                self.board[vehicle.head] = "."
                self.board[vehicle.head + 1] = "."
                self.board[vehicle.tail] = "."
                self.board[newTail] = vehicleLetterName
                self.board[newHead + 1] = vehicleLetterName
                self.board[newHead] = vehicleLetterName
            elif size == 2:
                self.board[vehicle.tail] = "."
                self.board[vehicle.head] = "."
                self.board[newHead] = vehicleLetterName
                self.board[newTail] = vehicleLetterName

        vehicle.head = newHead
        vehicle.tail = newTail

        vehicle.remainingFuel = vehicle.remainingFuel - multiplier
        self.move = f"{vehicleLetterName} Right {multiplier}\t{vehicle.remainingFuel} {self.__str__()}"

        # remove car from board if it is in the goalstate
        if vehicle.tail == 17 and vehicleLetterName != "A":
            self.board[vehicle.head] = "."
            self.board[vehicle.tail] = "."
            if size == 3:
                self.board[vehicle.head + 1] = "."
            else:
                self.board[vehicle.head + 1] = "."
                self.board[vehicle.head + 2] = "."
            self.vehicles.pop(vehicleLetterName)

    def allPossibleMoves(self):
        moves = []
        for vehicle in self.vehicles.values():
            if vehicle.isHorizontal:
                i = 1
                while i <= (6 - vehicle.size):
                    if not self.canMoveRight(vehicle.letterName, i):
                        break
                    board = self.__copy__()
                    board.moveRight(vehicle.letterName, i)
                    moves.append(board)
                    i += 1
                i = 1
                while i <= (6 - vehicle.size):
                    if not self.canMoveLeft(vehicle.letterName, i):
                        break
                    board = self.__copy__()
                    board.moveLeft(vehicle.letterName, i)
                    moves.append(board)
                    i += 1
            else:
                i = 1
                while i <= (6 - vehicle.size):
                    if not self.canMoveDown(vehicle.letterName, i):
                        break
                    board = self.__copy__()
                    board.moveDown(vehicle.letterName, i)
                    moves.append(board)
                    i += 1
                i = 1
                while i <= (6 - vehicle.size):
                    if not self.canMoveUp(vehicle.letterName, i):
                        break
                    board = self.__copy__()
                    board.moveUp(vehicle.letterName, i)
                    moves.append(board)
                    i += 1
        return moves
