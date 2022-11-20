from board import Board


class Node:
    GOAL_POSITION = 17  # array position so like starting from 0

    def __init__(self, board: Board):
        self.board = board
        self.parentNode = None

    def setParentNode(self, parentNode):
        self.parentNode = Node(parentNode)

    def getParentNode(self):
        return self.parentNode

    def generateChildren(self) -> list[Board]:
        return self.board.allPossibleMoves()

    def __str__(self) -> str:
        return f"Current node: \n{self.board.boardToString()} \nParent Node: \n{self.parentNode.board.boardToString()}"
