import timeit
from queue import PriorityQueue

from board import Board
from node import Node


class GBFS:
    def __init__(self, heuristic=1):
        print(f"USING HEURISTIC #{heuristic}")
        self.heuristic = heuristic

    def run(self, initialBoard: Board):
        start = timeit.default_timer()
        searchPathLength = 1

        closed = []
        open = PriorityQueue()

        initialNode = Node(initialBoard, None, 0, 0, 0)
        open.put(initialNode)

        while not open.empty():

            # Taking the next node in the open list
            currentNode: Node = open.get()

            # Check if it is in the goal state
            if currentNode.board.getVehicleAtExit() == "A":
                stop = timeit.default_timer()
                return (currentNode, stop - start, searchPathLength)

            # Append all the children into the end of the open list
            children = self.generateChildren(currentNode, closed)

            # If the return value is of type DUPLICATE then there is no need to add it to the closed list
            # The algorithm should just continue
            if children == "DUPLICATE":
                continue

            for eachChild in children:
                open.put(eachChild)

            # Append to closed list
            closed.append(currentNode)
            searchPathLength += 1

        # No solution found
        stop = timeit.default_timer()
        print(f"Searched through {searchPathLength} states")
        return (None, stop - start, searchPathLength)

    def generateChildren(self, currentNode, closedListOfNodes):

        if currentNode in closedListOfNodes or currentNode.depth > 93:
            return "DUPLICATE"

        newNodes = []

        childrenBoards = currentNode.board.allPossibleMoves()

        # Create new Nodes
        for oneBoard in childrenBoards:

            newNodes.append(
                Node(
                    oneBoard,
                    currentNode,
                    0,
                    self.heuristicPicker(oneBoard),
                    currentNode.depth + 1,
                )
            )

        nodesToRemove = []
        for node in newNodes:
            if node in closedListOfNodes:
                nodesToRemove.append(node)

        for node in nodesToRemove:
            newNodes.remove(node)

        return newNodes

    def heuristicPicker(self, aBoard: Board):
        if self.heuristic == 1:
            return self.heuristic1(aBoard)
        if self.heuristic == 2:
            return self.heuristic2(aBoard)
        if self.heuristic == 3:
            return self.heuristic3(aBoard)
        if self.heuristic == 4:
            return self.heuristic4(aBoard)

    def heuristic1(self, aBoard: Board):
        setOfBlockingCars = set()
        tail = aBoard.vehicles.get("A").tail
        for x in range(tail, 18):
            if aBoard.board[x] != ".":
                setOfBlockingCars.add(aBoard.board[x])
        return len(setOfBlockingCars)

    def heuristic2(self, aBoard: Board):
        count = 0
        tail = aBoard.vehicles.get("A").tail
        for x in range(tail, 18):
            if aBoard.board[x] != ".":
                count += 1
        return count

    def heuristic3(self, aBoard: Board):
        multiplier = 2
        return self.heuristic1(aBoard) * multiplier

    def heuristic4(self, aBoard: Board):
        return (
            len(aBoard.allPossibleMoves())
            - self.heuristic1(aBoard)
            - self.heuristic2(aBoard)
        ) * -1
