class Vehicle:
    def __init__(self, letterName, remainingFuel):
        self.letterName = letterName
        self.remainingFuel = remainingFuel

    def __str__(self) -> str:
        return f"Vehicle {self.letterName} has {self.remainingFuel} remaining fuel units."

    def isAmbulance(self) -> bool:
        return self.letterName == "A"
    
    def isVehicle(self) -> bool:
        return self.letterName != "."
        