from parser import Parser

def main():
    f = open("./src/sample-input.txt", "r")
    p1 = Parser(f.read())
    print(p1)

if __name__ == "__main__":
    main()