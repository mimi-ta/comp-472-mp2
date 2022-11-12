class Position:
    def __init__(self, x: str, y: int):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def isExit(self):
        return self.x == "f" and self.y == 3
