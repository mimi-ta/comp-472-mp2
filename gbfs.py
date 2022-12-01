import timeit
from queue import PriorityQueue

from board import Board
from node import Node


class GBFS:
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def run(self, initialBoard: Board):
        start = timeit.default_timer()
        searchPathLength = 0
        closed = []
        open = PriorityQueue()

        initialNode = Node(initialBoard, None, 0, 0)
        open.put((1, initialNode))

        while not open.empty():
            # Taking the next node in the open list
            currentNode: Node = open.get()[1]

            # currentNode.board.boardToString()
            # Append it to the closed list
            closed.append(currentNode)

            # Check if it is in the goal state
            if currentNode.board.getVehicleAtExit() == "A":
                stop = timeit.default_timer()
                return (currentNode, stop - start, searchPathLength)

            searchPathLength += 1

            # Append all the children into the end of the open list
            children = self.generateChildren(currentNode, closed)

            for eachChild in children:
                open.put((self.heuristicPicker(eachChild.board), eachChild))

        stop = timeit.default_timer()
        return (None, stop - start, searchPathLength)

    def generateChildren(self, currentNode, closedListOfNodes):
        newNodes = []
        childrenBoards = currentNode.board.allPossibleMoves()
        # Create new Nodes
        for oneBoard in childrenBoards:
            newNodes.append(Node(oneBoard, currentNode,0,self.heuristicPicker(oneBoard)))

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

    def heuristic1(self, aBoard: Board):
        setOfBlockingCars = set()
        for x in range(12, 18):
            if aBoard.board[x] != "A" and aBoard.board[x] != ".":
                setOfBlockingCars.add(aBoard.board[x])
        # Im returning -1 because priority queue returns from descending order so like a set
        # 3 8 5 2 will return 8 as the first element of a priority queue
        # but we want the opposite
        return len(setOfBlockingCars) * -1
