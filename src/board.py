import numpy as np

from position import Position


class Board:
    def __init__(self) -> None:
      self.board = np.zeros(dtype=Position,shape=(6,6))

    def __str__(self) -> str:
        return np.array2string(self.board)

b1 = Board()
print(b1)