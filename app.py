def greeter(func):
    print("Hello, " + func())

def getName():
    return input("What is your name?\n")

def main():
    greeter(getName)

if __name__ == "__main__":
    main()

