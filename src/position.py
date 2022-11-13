from vehicle import Vehicle


class Position:
    # x and y start at 1
    def __init__(self, vehicle: Vehicle, x: int, y: int):
        self.vehicle = vehicle
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        vehicleName = "None" if self.vehicle is None else self.vehicle.letterName
        return f"{vehicleName}@({convertXtoChar(self.x)},{self.y})"

    def __isExit(self):
        return self.x == "f" and self.y == 3

# a=1, b=2, ..., etc. bc I think it's easier... for the sake of the assignment?
# So it doesn't match up to array values i.e. a!=0, b!=1, ...
# Can 100% be easily changed though
def convertXtoChar(x: int):
    return chr(x + 96)
