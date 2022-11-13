class Parser:
    def __init__(self, input: str) -> None:
        self.lines = input.splitlines()
        self.__ignoreComments()
        print(self.lines)
    
    def __ignoreComments(self) -> None:
        for line in self.__findLineComments():
            self.lines.remove(line)
    
    def __findLineComments(self) -> list[str]:
        linesToRemove = []
        for i in range(len(self.lines)):
            self.lines[i] = self.lines[i].strip() # Remove whitespace
            if not self.lines[i] or self.lines[i].startswith("#"):
                linesToRemove.append(self.lines[i])
        return linesToRemove