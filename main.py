import copy
import re
from io import TextIOWrapper

from board import Board
from node import Node
from puzzleParser import PuzzleParser
from ucs import UCS

INPUT_FILE = "sample-input.txt"

def countSolutionPath(winningNode:Node, isWin:bool):
    # -1 because IDK if I should count the original node as a "state visited"
    count=-1
    if(isWin):
        while(winningNode):
            count+=1
            winningNode=winningNode.parentNode

    return count

def getRuntimeAndPrintStuffToConsole(winningNode: Node, isWin: bool):
    if isWin:
        print("You've Won!")
        runtime = winningNode.runtime
        print(f"Runtime: {runtime} seconds")
        print(f"Winning board:\n{winningNode.getBoard().boardToString()}")

    else:
        runtime = winningNode
        print(f"Runtime: {runtime} seconds")
        print("No solution.\n\n")
    return runtime


def writeSolutionPath(winningNode, f: TextIOWrapper):
    f.write(f"Solution path: ")
    winningNodeIterator = copy.deepcopy(winningNode)
    while winningNodeIterator.parentNode != None:
        f.write(
            re.split(r"\t+", winningNodeIterator.board.move)[0] + "; "
            if winningNodeIterator.parentNode != None
            else ""
        )
        winningNodeIterator = winningNodeIterator.parentNode

    f.write("\n\n")

    winningNodeIterator = winningNode
    while winningNodeIterator.parentNode != None:
        f.write(winningNodeIterator.board.move + "\n")
        winningNodeIterator = winningNodeIterator.parentNode


def generateUcsOutputFiles(i, puzzle: list[str]):
    f = open(f"./output/ucs-sol-{i+1}.txt", "w")
    f.write(f"Initial board configuration: {' '.join(puzzle)}\n\n")

    board = Board(puzzle)
    f.write(board.boardToString() + "\n")
    print(f"Initial board:\n{board.boardToString()}")
    f.write(f"Car fuel available: {board.getAllCarFuels()}\n\n")

    winningNode, numberOfNodesVisited = UCS(board)
    isWin = type(winningNode) == type(Node(None, None))
    runtime = getRuntimeAndPrintStuffToConsole(winningNode, isWin)
    solutionPathLength = countSolutionPath(winningNode,isWin)
    f.write(f"Runtime: {runtime} seconds\n")

    if isWin:
        f.write(f"Search path length: {numberOfNodesVisited}\n")
        f.write(f"Solution path length: {solutionPathLength}\n")

        writeSolutionPath(winningNode, f)

        f.write("\n")
        f.write(winningNode.getBoard().boardToString())
    else:
        f.write("No solution.")


def main():
    f = open(INPUT_FILE, "r")
    parser = PuzzleParser(f.read())
    for i, puzzle in enumerate(parser.getPuzzles()):
        generateUcsOutputFiles(i, puzzle)


if __name__ == "__main__":
    main()
