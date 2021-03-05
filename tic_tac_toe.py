# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

BOARD_SIZE = 10

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    top_board(board)
    print('-----------')
    mid_board(board)
    print('-----------')
    bottom_board(board)

def top_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def mid_board(board):
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')

def bottom_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return (
    (across_the_top(bo, le)) or # across the top
    (across_the_middle(bo, le)) or # across the middle    
    (across_the_bottom(bo, le)) or # across the bottom
    (down_the_left(bo, le)) or # down the left side
    (down_the_middle(bo, le)) or # down the middle
    (down_the_right(bo, le)) or # down the right side
    (diagonal_right(bo, le)) or # diagonal
    (diagonal_left(bo, le))) # diagonal

def across_the_top(bo, le):
    return bo[7] == le and bo[8] == le and bo[9] == le

def across_the_middle(bo, le):
    return bo[4] == le and bo[5] == le and bo[6] == le

def across_the_bottom(bo, le):
    return bo[1] == le and bo[2] == le and bo[3] == le

def down_the_left(bo, le):
    return bo[7] == le and bo[4] == le and bo[1] == le

def down_the_middle(bo, le):
    return bo[8] == le and bo[5] == le and bo[2] == le

def down_the_right(bo, le):
    return bo[9] == le and bo[6] == le and bo[3] == le

def diagonal_right(bo, le):
    return bo[7] == le and bo[5] == le and bo[3] == le

def diagonal_left(bo, le):
    return bo[9] == le and bo[5] == le and bo[1] == le

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for letter in range(len(board)):
        dupeBoard.append(board[letter])

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in their move.
    player_turn = ' ' # TODO: W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    while player_turn not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(player_turn)):
        print('What is your next move? (1-9)')
        player_turn = input()
    return int(player_turn)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if possibleMoves: # TODO: How would you write this pythanically? (You can google for it!)
        return random.choice(possibleMoves)
    return None

def getComputerMove(board, computer_turn): # TODO: W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer_turn == 'X':
        player_turn = 'O'
    else:
        player_turn = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, BOARD_SIZE):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computer_turn, i)
            if isWinner(copy, computer_turn):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, BOARD_SIZE):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, player_turn, i)
            if isWinner(copy, player_turn):
                return i

    # Try to take one of the corners, if they are free.
    next_turn = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if next_turn is not None: # TODO: Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
        return next_turn

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def player_move(theBoard, player_turn, computer_letter):
    "Player Move"
    drawBoard(theBoard)
    player_move = getPlayerMove(theBoard)
    makeMove(theBoard, player_turn, player_move)

def computer_move(theBoard, computer_letter, player_letter):
    "Computer Move"
    computer_move = getComputerMove(theBoard, computer_letter)
    makeMove(theBoard, computer_turn, computer_move)

def game_status(current_move, board_status, current_player_turn, current_computer_turn):
    "Checks logic if player wins, loses or goes in a tie"

    player_wins = isWinner(board_status, current_player_turn)
    computer_wins = isWinner(board_status, current_computer_turn)
    tie_game = isBoardFull(board_status)

    if player_wins or computer_wins:
        drawBoard(board_status)
        if current_move == 'player':
            print('Hooray! You have won the game!')
        else:
            print('The computer has beaten you! You lose.')
        return False
    if tie_game:
        drawBoard(board_status)
        print('The game is a tie!')
        return False
    return True


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, BOARD_SIZE):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')


while True:
    # Reset the board
    theBoard = [' '] * BOARD_SIZE 
    player_turn, computer_turn = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')

    while True: 
        if turn == 'player':
            # Player’s turn.
            player_move(theBoard, player_turn, computer_turn)

            if game_status(turn, theBoard, player_turn, computer_turn):
                turn = 'computer'
            else:
                break

        else:
            # Computer’s turn.
            computer_move(theBoard, player_turn, computer_turn)

            if game_status(turn, theBoard, computer_turn, player_turn):
                turn = 'player'
            else:
                break
    if not playAgain():
        break