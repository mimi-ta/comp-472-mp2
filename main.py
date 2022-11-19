from parser import Parser

from board import Board

INPUT_FILE = "sample-input.txt"

def main():
    f = open(INPUT_FILE, "r")
    parser = Parser(f.read())
    puzzles : list[Board] = []
    for index, puzzle in enumerate(parser.getPuzzles()):
        board = Board(puzzle)
        puzzles.append(board)
        print(board)
        # board.printBoard();
        # board.printCars();
        print("")

    print(parser.getPuzzles()[0])
    puzzles[0].printBoard()

    # puzzles[0].



if __name__ == "__main__":
    main()
