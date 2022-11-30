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

    def __copy__(self):
        tempVehicle = Vehicle(None, None, None, None, False)
        tempVehicle.letterName = self.letterName
        tempVehicle.size = self.size
        tempVehicle.remainingFuel = self.remainingFuel
        tempVehicle.positions = self.positions
        tempVehicle.isHorizontal = self.isHorizontal
        return tempVehicle
        
    def getFuelString(self) -> str:
        return f"{self.letterName}:{self.remainingFuel}"

    def isAmbulance(self) -> bool:
        return self.letterName == "A"

    def isVehicle(self) -> bool:
        return self.letterName != "."

    def setRemainingFuel(self, remainingFuel) -> None:
        self.remainingFuel = remainingFuel

    def getRemainingFuel(self) -> int:
        return self.remainingFuel

    def setPositions(self, positions) -> None:
        self.positions = positions

    def getPositions(self) -> list[int]:
        return self.positions

    def getIsHorizontal(self):
        return self.isHorizontal
