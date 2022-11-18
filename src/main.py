from parser import Parser
from board import Board

INPUT_FILE = "./src/sample-input.txt"


def main():
    f = open(INPUT_FILE, "r")
    parser = Parser(f.read())
    for puzzle in parser.getPuzzles():
        board = Board(puzzle)
        print(board)
        print("")


if __name__ == "__main__":
    main()
