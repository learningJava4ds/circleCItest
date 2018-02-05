def greeter(func):
    return "Hello, " + func()

def getName():
    return input("What is your name?\n")

def main():
    print(greeter(getName))

if __name__ == "__main__":
    main()

