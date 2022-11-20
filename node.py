from board import Board


class Node:
    GOAL_POSITION = 17  # array position so like starting from 0

    def __init__(self, board: Board, parentNode):
        self.board = board
        self.parentNode = parentNode

    def __eq__(self, other):
        if self and other:
            return self.board.boardToString() == other.board.boardToString()

    def setParentNode(self, parentNode):
        self.parentNode = parentNode

    def getParentNode(self):
        return self.parentNode

    def generateChildren(self, closedListOfNodes, openListofNodes):
        newNodes = []
        childrenBoards = self.board.allPossibleMoves()
        #Create new Nodes
        for oneBoard in childrenBoards:
            newNodes.append(Node(oneBoard,self))
            
        nodesToRemove = []
        for node in newNodes:
            if node in closedListOfNodes:
                nodesToRemove.append(node)
            if node in openListofNodes:
                nodesToRemove.append(node)

        for node in nodesToRemove:
            newNodes.remove(node)
        return newNodes

    def getBoard(self):
        return self.board
        
    def __str__(self) -> str:
        return f"Current node: \n{self.board.boardToString()} \nParent Node: \n{self.parentNode.board.boardToString()}"
