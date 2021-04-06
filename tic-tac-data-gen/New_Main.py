import math
import time


# func to check if space free
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


# func to insert x or o into free position
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            # exit()
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                # exit()
            else:
                print("Player wins!")
                # exit()
        return

    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return

# func to check for win
def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

# check for a draw
def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

# comp move uses minimax algorithm
def compMove(board):
    bestScore = -800
    bestMove = 0
    time1 = time.time()
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return

def initialise_board():
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
    return (board)

# defines minimax algorithm
def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = - math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore

while not checkForWin():
    time1 = time.time()
    compMove()
    playerMove()


# def name(inputs):
#    return(output)

# output = name(inputs)

def check_board(board):
    output = ''
    if checkDraw():
        output = 'draw'
    if checkForWin():
        output = 'win'


def play():
    board = initialise_board
    # computer does its first move
    board = computermove(board)

    board_state = check_board(board)

    while board_state == '':
        board = playermove(board)  # give the user the board, they make their move and the board updates
        board_state = check_board()
        board = computermove(board)
        board_state = check_board()

    # If there has been a draw or a win the while loop will end, otherwise it will loop
    # Now check which player has won

    winner = 'computer'
    # winner is the variable that denotes who has won, '[0,1]' 'computer won', 'user won'
    # if computer has won or the user
    return (winner)

def playagain():
    while (itterate < 1000)
        if (checkDraw())
            return True
        if checkForWin()
            return True
        itterate = itterate + 1

    winner = checkForWin(board)
    if winner is True


if __name__ == "__main__":
    winner = play()

