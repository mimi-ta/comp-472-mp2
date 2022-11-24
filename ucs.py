from node import Node
from collections import deque
from board import Board
import timeit

closed = []
open = deque()

# Returns winning node or returns runtime
def UCS(initialBoard: Board):
    start = timeit.default_timer()
    initialNode = Node(initialBoard, None)

    open.append(initialNode)

    while len(open) > 0:
        # Taking the next node in the open list
        currentNode: Node = open.popleft()

        currentNode.board.boardToString()
        # Append it to the closed list
        closed.append(currentNode)

        # Check if it is in the goal state
        if currentNode.getBoard().getVehicleAtExit() == "A":
            stop = timeit.default_timer()
            currentNode.setRuntime(stop - start)
            return currentNode

        # Append all the children into the end of the open list
        children = currentNode.generateChildren(closed, open)

        open.extend(children)
    stop = timeit.default_timer()
    return stop - start
