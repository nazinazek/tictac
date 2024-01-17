import random

board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currentPlayer = 'X'
winner = None
gameRunning = True


# Game Board
def gameBoard(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(f'---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')


# Player input
def playerInput(board):
    if currentPlayer == 'X':
        inputFromPlayer = int(input('Enter numbers between 1-9: '))
    else:
        inputFromPlayer = random.randint(1,9)
    
    if inputFromPlayer >= 1 and inputFromPlayer <=9 and board[inputFromPlayer - 1 ] == '-':
        board[inputFromPlayer-1] = currentPlayer
    else:
            print('Input is invalid.')


# Check for win algorithms 
def checkWinHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] != '-':
        winner = board[6]
        return True
    


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] != '-':
        winner = board[3]
        return True
    elif board[2] == board[5] == board[8] != '-':
        winner = board[6]
        return True
    


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] != '-':
        winner = board[3]
        return True
    

   
def checkTie(board):
    global gameRunning
    if '-' not in board:
        print(f'It is a tie!')
        gameBoard(board)
        gameRunning = False

# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
        print('Current player is O')
    else:
        currentPlayer = 'X'
        print('Current player is X')

# Check for win
def checkWin(board):
    global gameRunning
    if checkWinHorizontal(board):
        gameBoard(board) 
        print(f'The winner is {winner}')
        gameRunning = False

    elif checkDiagonal(board):
        gameBoard(board) 
        print(f'The winner is {winner}')
        gameRunning = False

    elif checkRow(board):
        gameBoard(board)
        print(f'The winner is {winner}')
        gameRunning = False



while gameRunning:
    gameBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
    checkWin(board)
    checkTie(board)
