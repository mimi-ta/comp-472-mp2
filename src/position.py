from vehicle import Vehicle


class Position:
    def __init__(self, vehicle: Vehicle, x: str, y: int):
        self.vehicle = vehicle
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"{self.vehicle.letterName}@({self.x},{self.y})"

    def isExit(self):
        return self.x == "f" and self.y == 3
