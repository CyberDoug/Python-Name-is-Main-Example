import sys

def importedFunction():
    print("This is being printed by a function that exists in another file!")

def main():
    print("This is being printed by the file it exists in!")

if __name__ == "__main__":
    main()