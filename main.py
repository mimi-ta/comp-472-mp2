
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

<<<<<<< HEAD
    test(puzzles);

=======
>>>>>>> 4a8525f96150d3f34cdb204a20801596812baeb1
if __name__ == "__main__":
    main()
