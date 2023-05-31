import sys

def checkInput():
    if len(sys.argv) != 3:
        print("Please provide a dictionary and test case")
        print("Example: python3 boggle.py Dictionaries/dictionary.txt TestCases/Input/input1.txt")
        return 0

    if not sys.argv[1].endswith('.txt'):
        print("Please provide a dictionary .txt file")
        return 0

    # If test case is a .txt file, there will only be one test
    if sys.argv[2].endswith('.txt'):
        return 'txt'

    # If test case is a .json file, there might be multiple tests
    elif sys.argv[2].endswith('.json'):
        return 'json'

    else:
        print("Please provide a .txt or .json test case file")
        return 0

# Parses through .txt file and adds boggle board to 2D char array
# Prints the number of words found in the boggle board on a new line
# Also prints the words found if the -showList argument is provided
# Input: .txt file (assume no errors in .txt file), boolean (for showList)
# Output: 2D char array
def parseTxtFile(fileName):
    output = []

    return output

# Parses through .json file and tests each boggle board individually
# Prints the number of words found in each boggle board one a new line with the board's number
# Also prints the words found if the -showList argument is provided
# Input: .json file containing an array of 1 or more boggle boards (assume no errors in .json file)
# Output: Returns array of 2D char arrays
def parseJsonFile(fileName):
    output = []

    return output

def convertInputToArray():

    return

def searchBoard():

    return

def main():
    # # Check input for dictionary and test case (in that order)
    # # If no files are provided, return
    inputType = checkInput()

    if inputType == 0:
        return
    elif inputType == "json":
        boards = parseJsonFile(sys.argv[2])
    elif inputType == "txt":
        boards = parseTxtFile(sys.argv[2])
    else:
        print("Undefined error in main")
        return

    for board in boards:
        searchBoard()

    return

if __name__ == "__main__":
    main()
