from board import Board
class Node:
    GOAL_POSITION = 17 # array position so like starting from 0

    def __init__(self, board: Board, parentNode):
        self.board = board
        self.parentNode = parentNode
    
    def __init__(self, board):
        self.board = board
        self.parentNode = None

    def setParentNode(self, parentNode):
        self.parentNode = parentNode

    def getParentNode(self):
        return self.parentNode

    def generateChildren(self):
        pass