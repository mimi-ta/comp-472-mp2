from board import Board
from puzzleParser import PuzzleParser
from testing import test

INPUT_FILE = "sample-input.txt"


def main():
    f = open(INPUT_FILE, "r")
    parser = PuzzleParser(f.read())
    puzzles: list[Board] = []
    for index, puzzle in enumerate(parser.getPuzzles()):
        board = Board(puzzle)
        puzzles.append(board)
        print(board.boardToString())
        print(board.allPossibleMoves())
        
    # test(puzzles);


if __name__ == "__main__":
    main()
