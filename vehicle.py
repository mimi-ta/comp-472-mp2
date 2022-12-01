from copy import copy


class Vehicle:
    def __init__(
        self, letterName, size, remainingFuel, positions: list[int], isHorizontal
    ):
        self.letterName = letterName
        self.size = size
        self.remainingFuel = remainingFuel
        self.positions = positions
        self.isHorizontal = isHorizontal

    def __str__(self) -> str:
        return f"{self.letterName} | fuel-{self.remainingFuel} | size-{self.size} | positions {self.positions} | Horizontal? {self.isHorizontal} "

    def DEEZNUTS(self):
        tempVehicle = copy(self)
        tempVehicle.positions = [int(element) for element in self.positions]
        return tempVehicle

    def getFuelString(self) -> str:
        return f"{self.letterName}:{self.remainingFuel}"

    def setPositions(self, positions) -> None:
        self.positions = positions

    def getPositions(self) -> list[int]:
        return self.positions
