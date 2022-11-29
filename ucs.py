from node import Node
from collections import deque
from board import Board
import timeit

class UCS:
    def __init__(self, winningNode, runtime, searchPathLength):
        self.winningNode = winningNode
        self.runtime = runtime
        self.searchPathLength = searchPathLength

    def getWinningNode(self):
        return self.winningNode

    def getRuntime(self):
        return self.runtime

    def getSearchPathLength(self):
        return self.searchPathLength

    # Returns winning node or returns runtime
    def runUCS(initialBoard: Board):
        start = timeit.default_timer()
        searchPathLength = 0
        closed = []
        open = deque()

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
                return UCS(currentNode, stop-start, searchPathLength)

            searchPathLength += 1

            # Append all the children into the end of the open list
            children = currentNode.generateChildren(closed, open)

            open.extend(children)
        stop = timeit.default_timer()
        return UCS(None, stop-start, searchPathLength)
