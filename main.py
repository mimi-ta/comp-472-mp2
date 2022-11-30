from copy import deepcopy
from re import split
from io import TextIOWrapper
import timeit
from board import Board
from node import Node
from puzzleParser import PuzzleParser
from ucs import UCS
import xlsxwriter

INPUT_FILE = "sample-input.txt"
# INPUT_FILE = "generatedPuzzles.txt"
PUZZLE_NUMBER = "puzzleNumber"
ALGORITHM = "algo"
HEURISTIC = "heuristic"
SOLUTION_LENGTH = "solutionLength"
SEARCH_PATH_LENGTH = "searchPathLength"
EXECUTION_TIME = "executionTime"


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


def getNumMovesWriteSolutionPathToFile(winningNode, f: TextIOWrapper):
    winningNodeIterator = deepcopy(winningNode)
    solutionPath = getSolutionPath(winningNodeIterator)
    solutionPathLength = len(solutionPath)
    f.write(f"Solution path length: {solutionPathLength} moves\n")

    f.write(f"Solution path: ")
    for i in range(solutionPathLength):
        f.write(solutionPath.pop())
    f.write("\n\n")

    # Reset iterator to the winning node (because by now it has become the initial node)
    winningNodeIterator = winningNode

    # Write to file the move and the corresponding board output
    while winningNodeIterator.parentNode != None:
        f.write(winningNodeIterator.board.move + "\n")
        winningNodeIterator = winningNodeIterator.parentNode

    return solutionPathLength


def generateUcsOutputFiles(i, puzzle: list[str], excelsheet, excelRow):
    output = dict()
    output.update({PUZZLE_NUMBER: i + 1, ALGORITHM: "UCS", HEURISTIC: "N/A"})

    board = Board(puzzle)

    f = open(f"./output/ucs-sol-{i+1}.txt", "w")
    f.write(f"Initial board configuration: {' '.join(puzzle)}\n\n")
    f.write(board.boardToString() + "\n")
    f.write(f"Car fuel available: {board.getAllCarFuels()}\n\n")

    UCSa = UCS(None, None, None)
    ucsResult = UCSa.runUCS(board)
    isWin = type(ucsResult.getWinningNode()) == type(Node(None, None, None, None))

    printGameOutcomeToConsole(ucsResult, isWin, board.boardToString())

    f.write(f"Runtime: {ucsResult.getRuntime()} seconds\n")

    if isWin:
        f.write(f"Search path length: {ucsResult.getSearchPathLength()} states\n")
        solutionLength = getNumMovesWriteSolutionPathToFile(
            ucsResult.getWinningNode(), f
        )
        output.update(
            {
                SOLUTION_LENGTH: solutionLength,
                SEARCH_PATH_LENGTH: ucsResult.getSearchPathLength(),
                EXECUTION_TIME: ucsResult.getRuntime(),
            }
        )
        f.write("\n")
        f.write(ucsResult.getWinningNode().getBoard().boardToString())

        for j, element in enumerate(output.values()):
            excelsheet.write(excelRow, j, element)
    else:
        f.write("No solution.")
        output.update(
            {
                SOLUTION_LENGTH: "No solution.",
                SEARCH_PATH_LENGTH: ucsResult.getSearchPathLength(),
                EXECUTION_TIME: ucsResult.getRuntime(),
            }
        )
        for j, element in enumerate(output.values()):
            excelsheet.write(excelRow, j, element)
    return excelRow + 1


def main():
    start = timeit.default_timer()
    f = open(INPUT_FILE, "r")
    parser = PuzzleParser(f.read())

    # Initialize excel spreadsheet
    workbook = xlsxwriter.Workbook("analysis.xlsx")
    excelsheet = workbook.add_worksheet()

    # Write headers to file
    for i, header in enumerate(
        [
            "Puzzle Number",
            "Algorithm",
            "Heuristic",
            "Length of the solution",
            "Length of the search path",
            "Execution time (seconds)",
        ]
    ):
        excelsheet.write(0, i, header)

    excelRow = 1  # Row that is not header
    for i, puzzle in enumerate(parser.getPuzzles()):
        excelRow = generateUcsOutputFiles(i, puzzle, excelsheet, excelRow)
        print(
            "------------------------------------------------------------------------------------------"
        )
    stop = timeit.default_timer()
    workbook.close()
    print(
        f"Total runtime for the {len(parser.getPuzzles())} puzzles: {stop-start} seconds or {(stop-start)/60/60} hours"
    )


if __name__ == "__main__":
    main()
