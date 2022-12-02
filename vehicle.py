class Vehicle:
    def __init__(
            self, letterName, size, remainingFuel, isHorizontal, head, tail
    ):
        self.letterName = letterName
        self.size = size
        self.remainingFuel = remainingFuel
        self.isHorizontal = isHorizontal
        self.head = head
        self.tail = tail

    def __str__(self) -> str:
        return f"{self.letterName} | fuel-{self.remainingFuel} | size-{self.size} | Horizontal? {self.isHorizontal} | " \
               f"head-{self.head} | tail-{self.tail} "

    def getFuelString(self) -> str:
        return f"{self.letterName}:{self.remainingFuel}"

