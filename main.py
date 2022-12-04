import timeit
from copy import deepcopy
from io import TextIOWrapper
from re import split

import xlsxwriter

from astar import ASTAR
from board import Board
from gbfs import GBFS
from node import Node
from puzzleParser import PuzzleParser
from ucs import UCS

# INPUT_FILE = "sample-input.txt"
INPUT_FILE = "generatedPuzzles.txt"
PUZZLE_NUMBER = "puzzleNumber"
ALGORITHM = "algo"
HEURISTIC = "heuristic"
SOLUTION_LENGTH = "solutionLength"
SEARCH_PATH_LENGTH = "searchPathLength"
EXECUTION_TIME = "executionTime"


def printGameOutcomeToConsole(winningNode, runtime, isWin, initialBoardString):
    if isWin:
        print("You've Won!")
        print(f"Runtime: {runtime} seconds\n")
        print(f"Initial board:\n{initialBoardString}")
        print(f"Winning board:\n{winningNode.board.boardToString()}")
    else:
        print(f"Runtime: {runtime} seconds")
        print("No solution.\n")


def getSolutionPath(winningNodeIterator) -> list[str]:
    solutionPath = []
    while winningNodeIterator.parentNode:
        solutionPath.append(
            split(r"\t+", winningNodeIterator.board.move)[0] + "; "
            if winningNodeIterator.parentNode
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


def generateOutputFiles(
    i,
    puzzle: list[str],
    excelsheet,
    excelRow: int,
    algorithmName: str,
    algorithm,
    heuristic: str,
):
    output = dict()
    output.update(
        {PUZZLE_NUMBER: i + 1, ALGORITHM: algorithmName, HEURISTIC: heuristic}
    )

    board = Board(puzzle)
    if algorithmName == "UCS":
        f = open(f"./output/{algorithmName}/{algorithmName}-sol-{i + 1}.txt", "w")
    else:
        f = open(
            f"./output/{algorithmName}/heuristic-{heuristic}/{algorithmName}-sol-{i + 1}.txt",
            "w",
        )
    f.write(f"Initial board configuration: {' '.join(puzzle)}\n\n")
    f.write(board.boardToString() + "\n")
    f.write(f"Car fuel available: {board.getAllCarFuels()}\n\n")

    winningNode, runtime, searchPathLength = algorithm.run(board)
    isWin = type(winningNode) == type(Node(None, None, None, None, None))

    printGameOutcomeToConsole(winningNode, runtime, isWin, board.boardToString())

    f.write(f"Runtime: {runtime} seconds\n")

    if isWin:
        f.write(f"Search path length: {searchPathLength} states\n")
        solutionLength = getNumMovesWriteSolutionPathToFile(winningNode, f)
        output.update(
            {
                SOLUTION_LENGTH: solutionLength,
                SEARCH_PATH_LENGTH: searchPathLength,
                EXECUTION_TIME: runtime,
            }
        )
        f.write("\n")
        f.write(winningNode.board.boardToString())

        for j, element in enumerate(output.values()):
            excelsheet.write(excelRow, j, element)
    else:
        f.write("No solution.")
        output.update(
            {
                SOLUTION_LENGTH: "No solution.",
                SEARCH_PATH_LENGTH: searchPathLength,
                EXECUTION_TIME: runtime,
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
    for i, puzzle in enumerate(parser.puzzles):
        excelRow = generateOutputFiles(
            i, puzzle, excelsheet, excelRow, "UCS", UCS(None, None, None), "N/A"
        )

        for HEURISTICNUMBER in range(4):
            excelRow = generateOutputFiles(
                i,
                puzzle,
                excelsheet,
                excelRow,
                "GBFS",
                GBFS(HEURISTICNUMBER + 1),
                f"{HEURISTICNUMBER + 1}",
            )

        for HEURISTICNUMBER in range(4):
            excelRow = generateOutputFiles(
                i,
                puzzle,
                excelsheet,
                excelRow,
                "AA",
                ASTAR(HEURISTICNUMBER + 1),
                f"{HEURISTICNUMBER + 1}",
            )
        print(
            "------------------------------------------------------------------------------------------"
        )
    stop = timeit.default_timer()
    print(
        f"Total runtime for the {len(parser.puzzles)} puzzles: {stop - start} seconds or {(stop - start) / 60 / 60} hours"
    )
    workbook.close()


if __name__ == "__main__":
    main()
