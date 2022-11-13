from parser import Parser

def main():
    f = open("./src/sample-input.txt", "r")
    p1 = Parser(f.read())
    print(len("BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL."))

if __name__ == "__main__":
    main()