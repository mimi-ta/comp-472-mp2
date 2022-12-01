class PuzzleParser:
    def __init__(self, input: str) -> None:
        self.puzzles = input.splitlines()
        self.__parse()

    def __findLineComments(self) -> list[str]:
        linesToRemove = []
        for i in range(len(self.puzzles)):
            self.puzzles[i] = self.puzzles[i].strip()  # Remove whitespace
            if not self.puzzles[i] or self.puzzles[i].startswith("#"):
                linesToRemove.append(self.puzzles[i])
        return linesToRemove

    def __ignoreComments(self) -> None:
        for line in self.__findLineComments():
            self.puzzles.remove(line)

    def __separateConfigurationAndFuel(self):
        separatedPuzzles = []
        for puzzle in self.puzzles:
            separatedPuzzles.append(puzzle.split())
        return separatedPuzzles

    def __parse(self) -> list[list[str]]:
        self.__ignoreComments()
        self.puzzles = self.__separateConfigurationAndFuel()

    def __str__(self) -> str:
        return f"{self.puzzles}"
