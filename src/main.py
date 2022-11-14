from parser import Parser
from board import Board
from position import Position
from vehicle import Vehicle

INPUT_FILE = "./src/sample-input.txt"


def main():
    f = open(INPUT_FILE, "r")
    parser = Parser(f.read())

    p1 = Position(Vehicle(".", 100), 7, 3)
    print(p1)
    for puzzle in parser.getPuzzles():
        board = Board(puzzle)
        print(board)
        print("")


if __name__ == "__main__":
    main()
