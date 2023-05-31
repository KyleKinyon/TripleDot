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
    # Print the resulting 2D array   
    print(output)
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

# Loop through each word in the provided dictionary and perform DFS to see if any of the words exist
# Prints the number of words found in the boggle board on a new line
# TODO: Also prints the words found if the -showList argument is provided
# Input: 2D array of chars, .txt file of dictionary, boolean (for showList)
# Output: None
def searchBoard(board, dictionary, showList):

    # Open dictionary file
    with open(dictionary, 'r') as file:
        # Get next word in dictionary 
        for line in file:
            # Remove new line character
            word = line.rstrip()
            # Check if word exists in board using DFS
            wordSearch(board, word)
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

def wordSearch(board, word):
    wordIndex = 0
    visited = [[]]

    for x in range(len(board[0])):
        for y in range(len(board)):
            wordSearchHelper(board, word, wordIndex, x, y, visited)

# TODO
def wordSearchHelper(board, word, wordIndex, row, column, visited):
    # Mark node as visited
    # visited[row][column] = True

    # If letter does not match, stop searching
    if word[wordIndex].lower() != board[row][column].lower():
        return
    # If we've reached the end of the word, we have a match
    if wordIndex+1 == len(word):
        print(word)
        return
    
    # Check each neighbor
    if row < len(board[0])-1:
        if column < len(board)-1:
            # Check bottom-right
            wordSearchHelper(board, word, wordIndex+1, row+1, column+1, visited)
        elif column > 0:
            # Check top-right
            wordSearchHelper(board, word, wordIndex+1, row+1, column-1, visited)
        else:
            # Check right
            wordSearchHelper(board, word, wordIndex+1, row+1, column, visited)
    if row > 0:
        if column < len(board)-1:
            # Check bottom-left
            wordSearchHelper(board, word, wordIndex+1, row-1, column+1, visited)
        elif column > 0:
            # Check top-left
            wordSearchHelper(board, word, wordIndex+1, row-1, column-1, visited)
        else:
            # Check left
            wordSearchHelper(board, word, wordIndex+1, row-1, column, visited)
    # Check bottom
    if column < len(board)-1:
        wordSearchHelper(board, word, wordIndex+1, row, column+1, visited)
    # Check top
    if column > 0:
        wordSearchHelper(board, word, wordIndex+1, row, column-1, visited)

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
        searchBoard(board, sys.argv[1], False)

    return

def wordSearchTester():
    board =  [["A", "B", "C", "D"],
              ["E", "F", "G", "H"],
              ["I", "J", "K", "L"],
              ["M", "N", "O", "P"]]
    word = "ABGLO"
    visited = [[False]*len(board[0]) for i in range(len(board))]
    wordSearch(board, word, 0, 0, 0, visited)


if __name__ == "__main__":
    main()