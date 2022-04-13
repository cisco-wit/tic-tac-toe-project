"""Tic-Tac-Toe, by Al Sweigart al@inventwithpython.com
The classic board game.
Tags: short, board game, game, two-player"""

ALL_SPACES = ['1','2',,] # Add spaces for each tic tac toe space
X, O, BLANK = 'X', 'O', ' '  # Constants for string values.


def main():
    print('Welcome to Tic-Tac-Toe!')
    gameBoard = getBlankBoard()  # Create a TTT board dictionary.
    currentPlayer, nextPlayer = # Create players X and O

    while True:  # Main game loop.
        # Display the board on the screen:
        print(getBoardStr(gameBoard))

        # Keep asking the player until they enter a number 1-9:
        move = None
        while not isValidSpace(gameBoard, move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input('> ')
        updateBoard(gameBoard, move, currentPlayer)  # Make the move.

        # Check if the game is over:
        if isWinner(gameBoard, currentPlayer):  # Check for a winner.
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):  # Check for a tie.
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break

        # Switch turns to the next player:
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')


def getBlankBoard():
    """Create a new, blank tic-tac-toe board. Using an Array and ALL SPACES constant"""
    # Map of space numbers: 1|2|3
    #                       -+-+-
    #                       4|5|6
    #                       -+-+-
    #                       7|8|9
    # Keys are 1 through 9, the values are X, O, or BLANK:
   


def getBoardStr(board):
    """Return a text-representation of the board. Use format funciton."""
    return

def isValidSpace(board, space):
    """Returns True if the space on the board is a valid space number
    and the space is blank."""
    return 


def isWinner(board, player):
    """Return True if player is a winner on this TTTBoard."""
    # Shorter variable names used here for readablility:
    b, p = board, player
    # Check for 3 marks across 3 rows, 3 columns, and 2 diagonals.
    return ((b['1'] == b['2'] == b['3'] == p) or  # Across top
            () or  # Across middle
            () or  # Across bottom
            () or  # Down left
            () or  # Down middle
            () or  # Down right
            () or  # Diagonal
            ())    # Diagonal

def isBoardFull(board):
    """Return True if every space on the board has been taken."""
    # If any space is blank, return False.
    # No spaces are blank, so return True.


def updateBoard(board, space, mark):
    """Sets the space on the board to mark."""
    


if __name__ == '__main__':
    main()  # Call main() if this module is run, but not when imported.