import numpy as np

from position import Position
from vehicle import Vehicle


class Board:
    def __init__(self):
      self.board = np.empty(dtype=Position,shape=(6,6))
      
      i = 0
      for j in range(len(self.board)):
        for i in range (len(self.board[j])):
            print(self.board[i][j])

    def __str__(self) -> str:
        return np.array2string(self.board)

    def updatePosition(self, vehicle: Vehicle, x: str, y: int):
        pass
        #self.board[x][y] = 

b1 = Board()