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

        #Append it to the closed list
        closed.append(theNode)

        #Check if it is in the goal state
        if theNode.getBoard().getVehicleAtExit() == "A":
            return theNode

        #Append all the children into the end of the open list
        theChildrenOfThisNode = theNode.generateChildren(closed,open)
        open.extend(theChildrenOfThisNode)





    # theChildrenOfThisNode = open[0].generateChildren(closed)
    # open.extend(theChildrenOfThisNode)
    #
    # for node in theChildrenOfThisNode:
    #     if node.getBoard() in open:
    #         open.remove(node)
    #
    # printAllBoardsInAListOfNodes(open)
            # open.append("slay")
            # open.append("queen")
            # open.popleft()
            # print(open)

    return None;
# ucs = UCS()

def printAllBoardsInAListOfNodes(ListOfNodes):
    for eachNode in ListOfNodes:
        print(eachNode.getBoard().boardToString())
        print()