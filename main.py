import copy
import re
from io import TextIOWrapper
from collections import deque

from board import Board
from node import Node
from puzzleParser import PuzzleParser
from ucs import UCS

INPUT_FILE = "sample-input.txt"


def printGameOutcomeToConsole(ucsResult: UCS, isWin):
    if isWin:
        print("You've Won!")
        print(f"Runtime: {ucsResult.getRuntime()} seconds\n")
        print(f"Winning board:\n{ucsResult.getWinningNode().getBoard().boardToString()}")
    else:
        print(f"Runtime: {ucsResult.getRuntime()} seconds")
        print("No solution.\n\n")


def writeSolutionPath(winningNode, f: TextIOWrapper):
    winningNodeIterator = copy.deepcopy(winningNode)
    solutionPath = []
    while winningNodeIterator.parentNode != None:
        solutionPath.append(re.split(r"\t+", winningNodeIterator.board.move)[0] + "; " if winningNodeIterator.parentNode != None else "")
        winningNodeIterator = winningNodeIterator.parentNode

    f.write(f"Solution path length: {len(solutionPath)} moves\n")  # TODO
    f.write(f"Solution path: ")
    for i in range(len(solutionPath)):
        f.write(solutionPath.pop())

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

    UCSa = UCS(None,None,None)
    ucsResult = UCSa.runUCS(board)
    isWin = type(ucsResult.getWinningNode()) == type(Node(None, None,None, None))

    printGameOutcomeToConsole(ucsResult, isWin)

    f.write(f"Runtime: {ucsResult.getRuntime()} seconds\n")

    if isWin:
        f.write(f"Search path length: {ucsResult.getSearchPathLength()} states\n")  # TODO
        writeSolutionPath(ucsResult.getWinningNode(), f)

        f.write("\n")
        f.write(ucsResult.getWinningNode().getBoard().boardToString())
    else:
        f.write("No solution.")


def main():
    f = open(INPUT_FILE, "r")
    parser = PuzzleParser(f.read())
    for i, puzzle in enumerate(parser.getPuzzles()):
        generateUcsOutputFiles(i, puzzle)


if __name__ == "__main__":
    main()
