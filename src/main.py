from parser import Parser
from board import Board

def main():
    f = open("./src/sample-input.txt", "r")
    p1 = Parser(f.read())
    b1 = Board(p1.getPuzzles())
    print(b1)

if __name__ == "__main__":
    main()