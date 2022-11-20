from node import Node
from collections import deque
from board import Board

closed = []
open = deque()

def UCS(initialBoard: Board):
    if initialBoard.getVehicleAtExit() == "A":
        pass
    open.append("slay")
    open.append("queen")
    open.popleft()
    print(open)

ucs = UCS()
