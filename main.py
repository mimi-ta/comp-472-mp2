from board import Board
from node import Node
from puzzleParser import PuzzleParser
from ucs import UCS

INPUT_FILE = "sample-input.txt"


def generateUcsOutputFiles(board):
    pass


def main():
    f = open(INPUT_FILE, "r")
    parser = PuzzleParser(f.read())
    puzzles: list[Board] = []
    for puzzle in parser.getPuzzles():
        board = Board(puzzle)
        puzzles.append(board)

    winningNode = UCS(puzzles[0])

    if type(winningNode) == type(Node(None, None)):
        print("You've Won!")
        print(winningNode.getBoard().boardToString())
        while winningNode.parentNode != None:
            print(winningNode.board.move)
            winningNode = winningNode.parentNode
    else:
        print(f"Runtime: {winningNode} seconds")
        print("No possible solution.")


if __name__ == "__main__":
    main()
