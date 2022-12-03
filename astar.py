import heapq
import timeit

from board import Board
from node import Node


class ASTAR:
    def __init__(self, heuristic=1):
        print(f"USING HEURISTIC #{heuristic}")
        self.heuristic = heuristic

    def run(self, initialBoard: Board):
        start = timeit.default_timer()
        searchPathLength = 1

        closed = []
        open = []
        heapq.heapify(open)

        initialNode = Node(initialBoard, None, 0, 0, 0)
        heapq.heappush(open, initialNode)

        while not len(open) == 0:

            # Taking the next node in the open list
            currentNode: Node = heapq.heappop(open)

            # Check if it is in the goal state
            if currentNode.board.getVehicleAtExit() == "A":
                stop = timeit.default_timer()
                return currentNode, stop - start, searchPathLength

            # Append all the children into the end of the open list
            children = self.generateChildren(currentNode, closed, open)

            if children == "DUPLICATE":
                continue

            for eachChild in children:
                heapq.heappush(open, eachChild)

            # Append to closed list
            closed.append(currentNode)
            searchPathLength += 1

        # No solution found
        stop = timeit.default_timer()
        print(f"Searched through {searchPathLength} states")
        return None, stop - start, searchPathLength

    def generateChildren(self, currentNode, closedListOfNodes, openList):

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
                    currentNode.gn + 1,
                    self.heuristicPicker(oneBoard),
                    currentNode.depth + 1,
                )
            )

        nodesToRemove = []
        for node in newNodes:
            if node in closedListOfNodes:
                if (node.gn + node.hn) > (
                    closedListOfNodes[closedListOfNodes.index(node)].gn
                    + closedListOfNodes[closedListOfNodes.index(node)].hn
                ):
                    nodesToRemove.append(node)
            elif node in openList:
                if (
                    openList[openList.index(node)].gn
                    + openList[openList.index(node)].hn
                ) > (node.gn + node.hn):
                    openList.remove(node)
                    heapq.heapify(openList)
                else:
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
