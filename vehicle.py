from position import Position


class Vehicle:
    def __init__(self, letterName, position: list[Position], remainingFuel):
        self.letterName = letterName
        self.position = position
        self.remainingFuel = remainingFuel

    def __str__(self) -> str:
        positions = ""
        for coordinate in self.position:
            positions + Position.__str__(coordinate)
        return f"The vehicle {self.letterName} has coordinates {self.getAllCoordinates()} and has {self.remainingFuel} remaining fuel units."

    def isAmbulance(self) -> bool:
        return self.letterName == "A"

    def getAllCoordinates(self) -> str:
        positionsAsString = []
        for coordinate in self.position:
            positionsAsString.append(Position.__str__(coordinate))
        return " ".join(positionsAsString)


v1 = Vehicle("A", [Position("a",1), Position("b",1)], 0)
print(v1)