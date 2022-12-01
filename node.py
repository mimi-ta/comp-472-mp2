from board import Board


class Node:
    def __init__(self, board: Board, parentNode, gn, hn):
        self.board = board
        self.parentNode = parentNode
        self.runtime = 0
        self.gn = gn
        self.hn = hn

    def __eq__(self, other):
        if self and other:
            return self.board.boardToString() == other.board.boardToString()

    def __str__(self) -> str:
        return f"Current node: \n{self.board.boardToString()} \nParent Node: \n{self.parentNode.board.boardToString()}"
