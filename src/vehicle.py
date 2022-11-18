class Vehicle:
    def __init__(self, letterName, size, remainingFuel):
        self.letterName = letterName
        self.size = size
        self.remainingFuel = remainingFuel

    def __str__(self) -> str:
        return f"{self.letterName}:{self.remainingFuel}"

    def isAmbulance(self) -> bool:
        return self.letterName == "A"

    def isVehicle(self) -> bool:
        return self.letterName != "."

    def isVertical(self) -> bool:
        pass
    
    def setRemainingFuel(self, remainingFuel) -> None:
        self.remainingFuel = remainingFuel

    def getRemainingFuel(self) -> int:
        return self.remainingFuel
