def unitTestingCanMove(puzzles):
    print("Testing can move up and down on a vertical car w good cars")
    print(puzzles[0].printBoard())
    puzzles[0].testCanMoveUp("L")
    puzzles[0].testCanMoveDown("M")

    print("Testing can move left and right on a horizontal car w good cars")
    puzzles[2].printBoard()
    puzzles[2].testCanMoveLeft("H")
    puzzles[2].testCanMoveRight("H")

    print("Testing can move up and down on a horizontal car")
    print(puzzles[0].printBoard())
    puzzles[0].testCanMoveUp("C")
    puzzles[0].testCanMoveDown("C")

    print("Testing can left and right on a vertical car")
    puzzles[2].printBoard()
    puzzles[2].testCanMoveLeft("N")
    puzzles[2].testCanMoveRight("N")

    print("Testing can move up and down on a vertical car that is blocked")
    print(puzzles[0].printBoard())
    puzzles[0].testCanMoveUp("K")
    puzzles[0].testCanMoveDown("K")

    print("Testing can left and right on a horizontal car that is blocked")
    puzzles[2].printBoard()
    puzzles[2].testCanMoveLeft("G")
    puzzles[2].testCanMoveRight("G")

    print("Testing can move up and down on a vertical car that is at the corner")
    print(puzzles[0].printBoard())
    puzzles[0].testCanMoveUp("G")
    puzzles[0].testCanMoveDown("G")


def unitTestingMove(puzzles):
    print("Testing move left")
    print(puzzles[0].printBoard())
    print(puzzles[0].moveLeft("H", 2))
    print("After moving left")
    print(puzzles[0].printBoard())

    print("Testing move right")
    print(puzzles[0].printBoard())
    print(puzzles[0].moveRight("H", 2))
    print("After moving right")
    print(puzzles[0].printBoard())

    print("Testing move up")
    print(puzzles[0].printBoard())
    puzzles[0].moveUp("L", 1)
    print("After moving up")
    print(puzzles[0].printBoard())

    print("Testing move down")
    print(puzzles[0].printBoard())
    puzzles[0].moveDown("L", 1)
    print("After moving down")
    print(puzzles[0].printBoard())


def test(puzzles):
    print(" ")
    # unitTestingCanMove(puzzles);
    unitTestingMove(puzzles)
