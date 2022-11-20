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
        print("Before popLeft")
        theNode = open.popleft()
        print("AFter popLeft")

        print(f"Pop board from open list:\n{theNode.board.boardToString()}")
        #Append it to the closed list
        print("Before append")
        closed.append(theNode)
        print("After append")

        #Check if it is in the goal state
        if theNode.getBoard().getVehicleAtExit() == "A":
            return theNode

        #Append all the children into the end of the open list
        theChildrenOfThisNode = theNode.generateChildren(closed,open)
        i = 1
        for child in theChildrenOfThisNode:
            print(f"Child: {i}")
            print(child.board.boardToString())
            i += 1

        open.extend(theChildrenOfThisNode)
        print("*****************************************************************************")

    return None;
