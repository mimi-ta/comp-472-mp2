import numpy as np

from position import Position
from vehicle import Vehicle

class Board:
    def __init__(self, puzzle: list[str]):
      self.board = np.array(list(puzzle[0][0])).reshape(6,6)

    def __str__(self) -> str:
        return np.array2string(self.board)
