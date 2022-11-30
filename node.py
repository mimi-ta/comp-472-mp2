from board import Board


class Node:
    def __init__(self, board: Board, parentNode, gn=0, hn=0):
        self.board = board
        self.parentNode = parentNode
        self.runtime = 0
        self.gn = gn
        self.hn = hn

    def __eq__(self, other):
        if self and other:
            return self.board.boardToString() == other.board.boardToString()

    def __ne__(self, other):
        if self and other:
            return not (self.gn + self.hn == other.gn + other.hn)

    def __lt__(self, other):
        if self and other:
            return self.gn + self.hn < other.gn + other.hn

    def __gt__(self, other):
        if self and other:
            return self.gn + self.hn > other.gn + other.hn

    def __le__(self, other):
        if self and other:
            return (self.gn + self.hn < other) or (
                self.gn + self.hn == other.gn + other.hn
            )

    def __ge__(self, other):
        if self and other:
            return (self.gn + self.hn > other.gn + other.hn) or (
                self.gn + self.hn == other.gn + other.hn
            )

    def __str__(self) -> str:
        return f"Current node: \n{self.board.boardToString()} \nParent Node: \n{self.parentNode.board.boardToString()}"
