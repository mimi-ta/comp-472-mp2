from vehicle import Vehicle

DEFAULT_FUEL: int = 100
GOAL_POSITION = 17  # array position so like starting from 0


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
        tempBoard.vehicles = {
            key: Vehicle.DEEZNUTS(value) for key, value in self.vehicles.items()
        }
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
                vehiclesDict.get(fuelDefinition[0]).remainingFuel = int(
                    fuelDefinition[1:]
                )

            return vehiclesDict
        else:
            return dict()

    def canMoveUp(self, vehicleLetterName: str, multiplier: int) -> bool:
        if self.vehicles.get(vehicleLetterName).remainingFuel < multiplier:
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

    def canMoveDown(self, vehicleLetterName: str, multiplier: int) -> bool:
        if self.vehicles.get(vehicleLetterName).remainingFuel < multiplier:
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

    def canMoveLeft(self, vehicleLetterName: str, multiplier: int) -> bool:
        if self.vehicles.get(vehicleLetterName).remainingFuel < multiplier:
            return False
        positions = self.vehicles.get(vehicleLetterName).getPositions()
        if (positions[0] - multiplier + 1) % 6 == 0:
            return False
        if self.board[positions[0] - multiplier] != ".":
            return False
        else:
            return True

    def canMoveRight(self, vehicleLetterName: str, multiplier: int) -> bool:
        if self.vehicles.get(vehicleLetterName).remainingFuel < multiplier:
            return False
        positions = self.vehicles.get(vehicleLetterName).getPositions()
        if (positions[-1] + multiplier - 1) % 6 == 5:
            return False
        if self.board[positions[-1] + multiplier] != ".":
            return False
        else:
            return True

    def moveUp(self, vehicleLetterName: str, multiplier: int):
        vehicle = self.vehicles.get(vehicleLetterName)
        updatePositions = vehicle.getPositions()

        for index, x in enumerate(updatePositions):
            self.board[int(x)] = "."
            updatePositions[index] = x - 6 * multiplier

        for x in updatePositions:
            self.board[x] = vehicleLetterName

        vehicle.setPositions(updatePositions)
        vehicle.setRemainingFuel(vehicle.getRemainingFuel() - multiplier)
        self.move = f"{vehicleLetterName} Up {multiplier}\t\t{vehicle.getRemainingFuel()} {self.__str__()}"

    def moveDown(self, vehicleLetterName: str, multiplier: int):
        vehicle = self.vehicles.get(vehicleLetterName)

        updatePositions = vehicle.getPositions()
        for index, x in enumerate(updatePositions):
            self.board[int(x)] = "."
            updatePositions[index] = x + 6 * multiplier
        for x in updatePositions:
            self.board[x] = vehicleLetterName

        vehicle.setPositions(updatePositions)
        vehicle.setRemainingFuel(vehicle.getRemainingFuel() - multiplier)
        self.move = f"{vehicleLetterName} Down {multiplier}\t{vehicle.getRemainingFuel()} {self.__str__()}"

        return True

    def moveLeft(self, vehicleLetterName: str, multiplier: int):
        vehicle = self.vehicles.get(vehicleLetterName)

        updatePositions = vehicle.getPositions()
        for index, x in enumerate(updatePositions):
            self.board[int(x)] = "."
            updatePositions[index] = x - 1 * multiplier
        for x in updatePositions:
            self.board[x] = vehicleLetterName

        vehicle.setPositions(updatePositions)
        vehicle.setRemainingFuel(vehicle.getRemainingFuel() - multiplier)
        self.move = f"{vehicleLetterName} Left {multiplier}\t{vehicle.getRemainingFuel()} {self.__str__()}"
        return True

    def moveRight(self, vehicleLetterName: str, multiplier: int):
        vehicle = self.vehicles.get(vehicleLetterName)

        updatePositions = vehicle.getPositions()
        for index, x in enumerate(updatePositions):
            self.board[int(x)] = "."
            updatePositions[index] = x + 1 * multiplier
        for x in updatePositions:
            self.board[x] = vehicleLetterName

        vehicle.setPositions(updatePositions)
        vehicle.setRemainingFuel(vehicle.getRemainingFuel() - multiplier)
        self.move = f"{vehicleLetterName} Right {multiplier}\t{vehicle.getRemainingFuel()} {self.__str__()}"

        # remove car from board if it is in the goalstate
        if updatePositions[-1] == 17 and vehicleLetterName != "A":
            for index, x in enumerate(updatePositions):
                self.board[int(x)] = "."
            self.vehicles.pop(vehicleLetterName)
        return True

    def allPossibleMoves(self):
        moves = []
        for vehicle in self.vehicles.values():
            if vehicle.isHorizontal:
                i = 1
                while i < 6 - vehicle.size:
                    if not self.canMoveRight(vehicle.letterName, i):
                        break
                    board = self.__copy__()
                    board.moveRight(vehicle.letterName, i)
                    moves.append(board)
                    i += 1
                i = 1
                while i < 6 - vehicle.size:
                    if not self.canMoveLeft(vehicle.letterName, i):
                        break
                    board = self.__copy__()
                    board.moveLeft(vehicle.letterName, i)
                    moves.append(board)
                    i += 1
            else:
                i = 1
                while i < 6 - vehicle.size:
                    if not self.canMoveDown(vehicle.letterName, i):
                        break
                    board = self.__copy__()
                    board.moveDown(vehicle.letterName, i)
                    moves.append(board)
                    i += 1
                i = 1
                while i < 6 - vehicle.size:
                    if not self.canMoveUp(vehicle.letterName, i):
                        break
                    board = self.__copy__()
                    board.moveUp(vehicle.letterName, i)
                    moves.append(board)
                    i += 1
        return moves
