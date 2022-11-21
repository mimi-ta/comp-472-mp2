from node import Node
from collections import deque
from board import Board
closed = []
open = deque()

def UCS(initialBoard: Board):
    initialNode = Node(initialBoard,None)

    open.append(initialNode)

    while(len(open)>0):
        #Taking the next node in the open list
        theNode = open.popleft()

        theNode.board.boardToString();
        #Append it to the closed list
        closed.append(theNode)

        #Check if it is in the goal state
        if theNode.getBoard().getVehicleAtExit() == "A":
            return theNode

        #Append all the children into the end of the open list
        theChildrenOfThisNode = theNode.generateChildren(closed,open)


        open.extend(theChildrenOfThisNode)

    return None;
