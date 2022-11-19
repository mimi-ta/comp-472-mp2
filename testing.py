def unitTestingCanMove(puzzles):
    print("Testing can move up and down on a vertical car w good cars")
    puzzles[0].printBoard()
    puzzles[0].testCanMoveUp("L")
    puzzles[0].testCanMoveDown("M")

    print("Testing can move left and right on a horizontal car w good cars")
    puzzles[2].printBoard()
    puzzles[2].testCanMoveLeft("H")
    puzzles[2].testCanMoveRight("H")

    print("Testing can move up and down on a horizontal car")
    puzzles[0].printBoard()
    puzzles[0].testCanMoveUp("C")
    puzzles[0].testCanMoveDown("C")

    print("Testing can left and right on a vertical car")
    puzzles[2].printBoard()
    puzzles[2].testCanMoveLeft("N")
    puzzles[2].testCanMoveRight("N")

    print("Testing can move up and down on a vertical car that is blocked")
    puzzles[0].printBoard()
    puzzles[0].testCanMoveUp("K")
    puzzles[0].testCanMoveDown("K")

    print("Testing can left and right on a horizontal car that is blocked")
    puzzles[2].printBoard()
    puzzles[2].testCanMoveLeft("G")
    puzzles[2].testCanMoveRight("G")

    print("Testing can move up and down on a vertical car that is at the corner")
    puzzles[0].printBoard()
    puzzles[0].testCanMoveUp("G")
    puzzles[0].testCanMoveDown("G")


def unitTestingMove(puzzles):
    print("Testing move left")
    puzzles[2].printBoard();
    puzzles[2].moveLeft("H");
    print("After moving left")
    puzzles[2].printBoard();

    print("Testing move right")
    puzzles[2].printBoard();
    puzzles[2].moveRight("H");
    print("After moving right")
    puzzles[2].printBoard();

    print("Testing move up")
    puzzles[2].printBoard();
    puzzles[2].moveUp("L");
    print("After moving up")
    puzzles[2].printBoard();

    print("Testing move down")
    puzzles[2].printBoard();
    puzzles[2].moveDown("L");
    print("After moving down")
    puzzles[2].printBoard();
def test(puzzles):
    print(" ")
    # unitTestingCanMove(puzzles);
    unitTestingMove(puzzles);
