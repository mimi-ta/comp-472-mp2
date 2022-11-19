
from parser import Parser
from testing import test
from board import Board

INPUT_FILE = "sample-input.txt"

def main():
    f = open(INPUT_FILE, "r")
    parser = Parser(f.read())
    puzzles : list[Board] = []
    for index, puzzle in enumerate(parser.getPuzzles()):
        board = Board(puzzle)
        puzzles.append(board)
        # board.printBoard()
        # board.printCars()
        print("")

    test(puzzles);

if __name__ == "__main__":
    main()
