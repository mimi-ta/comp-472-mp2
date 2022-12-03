from board import Board


class Node:
    def __init__(self, board: Board, parentNode, gn, hn, depth=None):
        self.board = board
        self.parentNode = parentNode
        self.runtime = 0
        self.gn = gn
        self.hn = hn
        self.depth = depth

    def __eq__(self, other):
        if self and other:
            return self.board.boardToString() == other.board.boardToString()

    def __ne__(self, other):
        if self and other:
            return not (self.board.boardToString() == other.board.boardToString())

    def __lt__(self, other):
        if self and other:
            return self.gn + self.hn < other.gn + other.hn

    def __gt__(self, other):
        if self and other:
            return self.gn + self.hn > other.gn + other.hn

    def __le__(self, other):
        if self and other:
            return (self.gn + self.hn <= other.gn + other.hn) or (
                self.gn + self.hn == other.gn + other.hn
            )

    def __ge__(self, other):
        # if self and other:
        return (self.gn + self.hn > other.gn + other.hn) or (
            self.gn + self.hn == other.gn + other.hn
        )

    def __str__(self) -> str:
        return f"Current node: \n{self.board.boardToString()} \nParent Node: \n{self.parentNode.board.boardToString()}"

    def h1(self):
        board = self.board.board
        ambulanceTail = self.board.vehicles.get("A").tail
        iterator = 17 - ambulanceTail
        counter = 0
        for x in range(iterator):
            position = ambulanceTail + 1 + x
            previous = position - 1
            if not board[position] == "." and not board[position] == board[previous]:
                counter += 1
        return counter

    def h2(self):
        board = self.board.board
        ambulanceTail = self.board.vehicles.get("A").tail
        iterator = 17 - ambulanceTail
        counter = 0
        for x in range(iterator):
            position = ambulanceTail + 1 + x
            if not board[position] == ".":
                counter += 1
        return counter

    def h3(self):
        return 3 * self.h1()
