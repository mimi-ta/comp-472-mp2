from copy import deepcopy
from re import split
from io import TextIOWrapper
import timeit
from board import Board
from node import Node
from puzzleParser import PuzzleParser
from ucs import UCS

INPUT_FILE = "sample-input.txt"
# INPUT_FILE = "generatedPuzzles.txt"


def printGameOutcomeToConsole(ucsResult: UCS, isWin, initialBoardString):
    if isWin:
        print("You've Won!")
        print(f"Runtime: {ucsResult.getRuntime()} seconds\n")
        print(f"Initial board:\n{initialBoardString}")
        print(
            f"Winning board:\n{ucsResult.getWinningNode().getBoard().boardToString()}"
        )
    else:
        print(f"Runtime: {ucsResult.getRuntime()} seconds")
        print("No solution.\n")


def getSolutionPath(winningNodeIterator) -> list[str]:
    solutionPath = []
    while winningNodeIterator.parentNode != None:
        solutionPath.append(
            split(r"\t+", winningNodeIterator.board.move)[0] + "; "
            if winningNodeIterator.parentNode != None
            else ""
        )
        winningNodeIterator = winningNodeIterator.parentNode
    return solutionPath


def writeSolutionPathToFile(winningNode, f: TextIOWrapper):
    winningNodeIterator = deepcopy(winningNode)
    solutionPath = getSolutionPath(winningNodeIterator)

    f.write(f"Solution path length: {len(solutionPath)} moves\n")

    f.write(f"Solution path: ")
    for i in range(len(solutionPath)):
        f.write(solutionPath.pop())
    f.write("\n\n")

    # Reset iterator to the winning node (because by now it has become the initial node)
    winningNodeIterator = winningNode

    # Write to file the move and the corresponding board output
    while winningNodeIterator.parentNode != None:
        f.write(winningNodeIterator.board.move + "\n")
        winningNodeIterator = winningNodeIterator.parentNode


def generateUcsOutputFiles(i, puzzle: list[str]):
    f = open(f"./output/ucs-sol-{i+1}.txt", "w")
    f.write(f"Initial board configuration: {' '.join(puzzle)}\n\n")

    board = Board(puzzle)
    f.write(board.boardToString() + "\n")
    f.write(f"Car fuel available: {board.getAllCarFuels()}\n\n")

    UCSa = UCS(None, None, None)
    ucsResult = UCSa.runUCS(board)
    isWin = type(ucsResult.getWinningNode()) == type(Node(None, None, None, None))

    printGameOutcomeToConsole(ucsResult, isWin, board.boardToString())

    f.write(f"Runtime: {ucsResult.getRuntime()} seconds\n")

    if isWin:
        f.write(f"Search path length: {ucsResult.getSearchPathLength()} states\n")
        writeSolutionPathToFile(ucsResult.getWinningNode(), f)

        f.write("\n")
        f.write(ucsResult.getWinningNode().getBoard().boardToString())
    else:
        f.write("No solution.")


def main():
    start = timeit.default_timer()
    f = open(INPUT_FILE, "r")
    parser = PuzzleParser(f.read())
    for i, puzzle in enumerate(parser.getPuzzles()):
        generateUcsOutputFiles(i, puzzle)
        print("--------------------------------------------")
    stop = timeit.default_timer()
    print(f"Total runtime for the 50 puzzles: {stop-start} seconds")


if __name__ == "__main__":
    main()
