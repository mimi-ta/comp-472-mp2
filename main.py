from board import Board
from puzzleParser import PuzzleParser
from ucs import UCS

INPUT_FILE = "sample-input.txt"


def main():
    f = open(INPUT_FILE, "r")
    parser = PuzzleParser(f.read())
    puzzles: list[Board] = []
    for index, puzzle in enumerate(parser.getPuzzles()):
        board = Board(puzzle)
        puzzles.append(board)

    theWinningNode = UCS(puzzles[0])

    if(theWinningNode):
        print("You've Won!")
        print(theWinningNode.getBoard().boardToString())
    else:
        print("No Possible Solution")

    while (theWinningNode.parentNode!=None):
        print(theWinningNode.board.move)
        print(theWinningNode.board.boardToString())
        theWinningNode = theWinningNode.parentNode


if __name__ == "__main__":
    main()
