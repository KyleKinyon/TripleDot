import sys

# Checks to see if there is a dictionary and test case present on execution
# Input: None
# Output:
#   - '.json' if a .json test case file is provided
#   - '.txt' if a .txt test case file is provided
#   - 0 if there is an error
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
# Input: .txt file (assume no errors in .txt file)
# Output: 2D char array
def parseTxtFile(fileName):
    example = [["A", "B", "C", "D"],
              ["E", "F", "G", "H"],
              ["I", "J", "K", "L"],
              ["M", "N", "O", "P"]]
    output = []

    # Open the .txt file
    with open(fileName, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Create an empty list for each row in the 2D array
            row = []
            # Iterate over each character in the line
            for char in line:
                # Append the character to the row list
                if char != '\n':
                    row.append(char)
            # Append the row list to the 2D array
            output.append(row)
            
    print(output)
    return output
# Print the resulting 2D array

    # Loop over each character on each line and add it to the 2D array until the new line character 
    # is reached.
    # Example:
    # ABCD
    # EFGH
    # IJKL
    # MNOP
    # -> [[A,B,C,D],
    #     [E,F,G,H],
    #     [I,J,K,L],
    #     [M,N,O,P]]
    
    for x in output:
        print(x)
    return output

# Parses through .json file and adds each boggle board to an array of boggle boards
# Input: .json file containing an array of 1 or more boggle boards (assume no errors in .json file)
# Output: Returns array of 2D char arrays
def parseJsonFile(fileName):
    output = []
    output.append([ ["A", "B", "C", "D"],
                    ["E", "F", "G", "H"],
                    ["I", "J", "K", "L"],
                    ["M", "N", "O", "P"]])
    output.append([ ["Q", "R", "S", "T"],
                    ["U", "V", "W", "X"],
                    ["Y", "Z", "A", "B"],
                    ["C", "D", "E", "F"]])

    # Open the .json file

    # Similar to instructions in parseTxtFile() but ignore json syntax

    return output

# Brute force DFS
# Loop through each word in the provided dictionary and perform DFS to see if any of the words exist
# Prints the number of words found in the boggle board on a new line
# Also prints the words found if the -showList argument is provided
# Input: 2D array of chars, .txt file of dictionary, boolean (for showList)
# Output: None
def searchBoard():

    # Open dictionary file

    # Get next word in dictionary

    # Check if word exists in board using DFS

    return

# Loop through each word in the provided dictionary and perform DFS to see if any of the words exist.
# If a word does not exist on the board, skip all words with the same starting letter(s).
# Prints the number of words found in the boggle board on a new line
# Also prints the words found if the -showList argument is provided
# Input: 2D array of chars, .txt file of dictionary, boolean (for showList)
# Output: None
def optimizedBoardSearch():

    # Open dictionary file

    # Get next word in dictionary (skip any if possible)

    # Check if word exists in board using DFS
    
    # If word does not exist in the board, return it and skip all words with the same starting letter(s)

    return

# todo
def DFS():

    return

def main():
    boards = []

    # Check input for dictionary and test case (in that order)
    # If no files are provided, return
    inputType = checkInput()
    if inputType == 0:
        return
    elif inputType == "json":
        boards = parseJsonFile(sys.argv[2])
    elif inputType == "txt":
        boards.append(parseTxtFile(sys.argv[2]))
    else:
        print("Undefined error in main")
        return

    # Search board(s) for all words in the provided dictionary 
    for board in boards:
        searchBoard()

    return

if __name__ == "__main__":
    main()
