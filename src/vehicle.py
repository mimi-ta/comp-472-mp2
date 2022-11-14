class Vehicle:
    def __init__(self, letterName, remainingFuel):
        self.letterName = letterName
        self.remainingFuel = remainingFuel

    def __str__(self) -> str:
        return f"{self.letterName}:{self.remainingFuel}"

    def __isAmbulance(self) -> bool:
        return self.letterName == "A"

    def __isVehicle(self) -> bool:
        return self.letterName != "."

    def setRemainingFuel(self, remainingFuel) -> None:
        self.remainingFuel = remainingFuel

    def getRemainingFuel(self) -> int:
        return self.remainingFuel
