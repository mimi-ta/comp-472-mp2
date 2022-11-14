from parser import Parser
from board import Board


def main():
    f = open("./src/sample-input.txt", "r")
    parser = Parser(f.read())

    for puzzle in parser.getPuzzles():
        board = Board(puzzle)
        print(board)
        print("")


if __name__ == "__main__":
    main()
