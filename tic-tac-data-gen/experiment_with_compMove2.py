import math
import time
import random

player = 'O'
bot = 'X'

#func to allow user to input
def playerMove(board):
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position, board) #where player defines the letter played, bestMove defines the position played in, and board is a required input
    return

#func to allow playing a player who places pieces randomly
def randMove(board):
    position = random.randint(1,9)
    insertLetterRand(player, position, board)
    return

#comp move uses minimax algorithm- comp will always = bot
def compMove(board):
    bestScore = -800
    bestMove = 0
    #print('compmove1 used')
    #time1 = time.time()
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    #print(bestMove)
    #print(time.time() - time1)
    insertLetter(bot, bestMove, board) #where bot defines the letter played, bestMove defines the position played in, and board is a required input
    return

#defines minimax algorithm
def minimax(board, depth, isMaximizing):
    #print('minimax1 used')
    if (checkWhichMarkWon(bot, board)):
        return 1
    elif (checkWhichMarkWon(player, board)):
        return -1
    elif (checkDraw(board)): #does not need 'mark'- bot/player as an input as only checks if all spaces are full
        return 0

    if (isMaximizing):
        bestScore = - math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                #print(board)  # nathan added
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                #print('score after minimax on that key (maximising part):',score) #nath
                #print('current bestScore:', bestScore) #nath
                if (score > bestScore):
                    bestScore = score
        #print('bestScore (after all moves tried with minimax(maximising part) - propogate score back:', bestScore)  # nathan added
        return bestScore

    else:
        bestScore = math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                #print(board)  # nathan added
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                #print('score after minimax on that key (maximising part):',score) #nath
                #print('current bestScore:', bestScore) #nath
                if (score < bestScore):
                    bestScore = score
        #print('bestScore (after all moves tried with minimax (minimising part) - propogate score back:', bestScore)  # nathan
        return bestScore

#comp move2 uses minimax algorithm- comp2 will always = player
def compMove2(board):
    bestScore = -800
    bestMove = 0
    #print('compmove2 used')
    #time1 = time.time()
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = player
            score = minimax2(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    #print(bestMove)
    #print(time.time() - time1)
    insertLetter(player, bestMove, board) #where bot defines the letter played, bestMove defines the position played in, and board is a required input
    return

#defines minimax algorithm
def minimax2(board, depth, isMaximizing):
    #print('minimax2 used')
    if (checkWhichMarkWon(player, board)):
        return 1
    elif (checkWhichMarkWon(bot, board)):
        return -1
    elif (checkDraw(board)): #does not need 'mark'- bot/player as an input as only checks if all spaces are full
        return 0

    if (isMaximizing):
        bestScore = - math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax2(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax2(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore

def checkWhichMarkWon(mark, board):
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

#define the board env elements with grid
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")

#func to insert x or o into free position
def insertLetter(letter, position, board):
    if spaceIsFree(position, board):
        board[position] = letter
        printBoard(board)
        #if (checkDraw(board)):
            #print("Draw!")
            #exit()
        #if checkForWin(board):
            #if letter == 'X':
                #print("Bot wins!")
                #exit()
            #else:
                #print("Player wins!")
                #exit()
        return

    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position, board)
        return

#func to insert x or o into free position
def insertLetterRand(letter, position, board):
    if spaceIsFree(position, board):
        board[position] = letter
        printBoard(board)
        if (checkDraw(board)):
            print("Draw!")
            #exit()
        if checkForWin(board):
            if letter == 'X':
                print("Bot wins!")
                #exit()
            else:
                print("Player wins!")
                #exit()
        return

    else:
        position = random.randint(1,9)
        insertLetter2(letter, position, board)
        return

#func to check if space free
def spaceIsFree(position, board):
    #print(position)
    if board[position] == ' ':
        return True
    else:
        return False

#check for a draw
def checkDraw(board):
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

#func to check for win
def checkForWin(board):
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

def initialise_board():
    return ({1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '})


def check_game_finished(board):
    if checkForWin(board) == True:
        if checkWhichMarkWon('X', board) == True:
            return 'Bot wins!'
        elif checkWhichMarkWon('O', board) == True:
            return 'Bot loses!'

    elif checkDraw(board) == True:
        return 'Draw!'

    else:
        return False


def main():
    board = initialise_board()
    while check_game_finished(board) == False:
        compMove(board)  # x bot
        if check_game_finished(board) == False:
            compMove2(board)  # o player
        else:
            #print(check_game_finished(board))
            output = check_game_finished(board)
            return output
    else:
        # print(check_game_finished(board))
        output = check_game_finished(board)
        return output


if __name__ == "__main__":
    main()


