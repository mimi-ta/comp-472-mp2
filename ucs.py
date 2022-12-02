from node import Node
from collections import deque
from board import Board
import timeit


class UCS:
    def __init__(self, winningNode, runtime, searchPathLength):
        self.winningNode = winningNode
        self.runtime = runtime
        self.searchPathLength = searchPathLength

    # Returns winning node or returns runtime
    def runUCS(self, initialBoard: Board):
        start = timeit.default_timer()
        searchPathLength = 0
        closed = []
        open = deque()

        initialNode = Node(initialBoard, None, 0, 0)
        open.append(initialNode)

        while len(open) > 0:
            # Taking the next node in the open list
            currentNode: Node = open.popleft()

            currentNode.board.boardToString()
            # Append it to the closed list
            closed.append(currentNode)

            # Check if it is in the goal state
            if currentNode.board.getVehicleAtExit() == "A":
                stop = timeit.default_timer()
                return UCS(currentNode, stop - start, searchPathLength)

            searchPathLength += 1

            # Append all the children into the end of the open list
            children = self.generateChildren(currentNode, closed, open)

            open.extend(children)
        stop = timeit.default_timer()
        return UCS(None, stop - start, searchPathLength)

    def generateChildren(self, currentNode, closedListOfNodes, openListofNodes):
        newNodes = []
        childrenBoards = currentNode.board.allPossibleMoves()

        # Create new Nodes
        for oneBoard in childrenBoards:
            newNodes.append(Node(oneBoard, currentNode, currentNode.gn+1, 0))

        nodesToRemove = []
        for node in newNodes:
            if node in closedListOfNodes:
                nodesToRemove.append(node)
            if node in openListofNodes:
                nodesToRemove.append(node)

        for node in nodesToRemove:
            newNodes.remove(node)
        return newNodes
