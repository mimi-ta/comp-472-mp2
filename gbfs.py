# from node import Node
# from queue import PriorityQueue
# from board import Board
# import timeit
#
#
# class GBFS:
#     def __init__(self, heuristic):
#         self.heuristic = heuristic
#
#     def runUCS(self, initialBoard: Board):
#         start = timeit.default_timer()
#         searchPathLength = 0
#         closed = []
#         open = PriorityQueue()
#
#         initialNode = Node(initialBoard, None, 0,0)
#         open.put((1,initialNode))
#
#
#         while (not open.empty()):
#             # Taking the next node in the open list
#             currentNode: Node = open.popleft()
#
#             currentNode.board.boardToString()
#             # Append it to the closed list
#             closed.append(currentNode)
#
#             # Check if it is in the goal state
#             if currentNode.getBoard().getVehicleAtExit() == "A":
#                 stop = timeit.default_timer()
#                 return UCS(currentNode, stop-start, searchPathLength)
#
#             searchPathLength += 1
#
#             # Append all the children into the end of the open list
#             children = self.generateChildren(currentNode, closed, open)
#
#             open.extend(children)
#         stop = timeit.default_timer()
#         return UCS(None, stop-start, searchPathLength)
#
#     def generateChildren(self, currentNode , closedListOfNodes, openListofNodes):
#         newNodes = []
#         childrenBoards = currentNode.board.allPossibleMoves()
#         # Create new Nodes
#         for oneBoard in childrenBoards:
#             newNodes.append(Node(oneBoard, currentNode,0,0))
#
#         nodesToRemove = []
#         for node in newNodes:
#             if node in closedListOfNodes:
#                 nodesToRemove.append(node)
#             if node in openListofNodes:
#                 nodesToRemove.append(node)
#
#         for node in nodesToRemove:
#             newNodes.remove(node)
#         return newNodes
#
