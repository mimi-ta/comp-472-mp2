from vehicle import Vehicle


class Position:
    # x and y start at 1
    def __init__(self) -> None:
        self.vehicle = None
        self.x = None
        self.y = None

    def __init__(self, vehicle: Vehicle, x: int, y: int):
        self.vehicle = vehicle
        self.x = convertXtoChar(x)
        self.y = y

    def __str__(self) -> str:
        vehicleName = "None" if self.vehicle is None else self.vehicle.letterName
        return f"{vehicleName}@({self.x},{self.y})"

    def __isExit(self):
        return self.x == "f" and self.y == 3


# a=1, b=2, ..., etc. bc I think it's easier... for the sake of the assignment?
# So it doesn't match up to array values i.e. a!=0, b!=1, ...
# Can 100% be easily changed though
def convertXtoChar(x: int):
    if type(x) is int:
        return chr(x + 96)


def convertCharToX(x: chr):
    if type(x) is chr:
        return ord(x) - 96
