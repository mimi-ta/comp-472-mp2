class Vehicle:
    def __init__(self, letterName, remainingFuel):
        self.letterName = letterName
        self.remainingFuel = remainingFuel

    def __str__(self) -> str:
        return f"Vehicle {self.letterName} has {self.remainingFuel} remaining fuel units."

    def __isAmbulance(self) -> bool:
        return self.letterName == "A"
    
    def __isVehicle(self) -> bool:
        return self.letterName != "."
    
    def setRemainingFuel(self, remainingFuel):
        self.remainingFuel = remainingFuel
