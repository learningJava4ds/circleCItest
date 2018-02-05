def greeter(func):
    return "Hello, " + func()

def getName():
    return input("What is your name?\n")

def main():
    rnbl = greeter(getName)
    print(rnbl)
    return rnbl

if __name__ == "__main__":
    main()

