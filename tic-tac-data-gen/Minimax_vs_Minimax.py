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
    output = insertLetterRand(player, position, board)
    return output

#####--------------------------------------------------------------#####
#comp move uses minimax algorithm
def compMove(board):
    bestScore = -math.inf
    alpha = -math.inf
    beta = math.inf
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, alpha, beta, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    output = insertLetter(bot, bestMove, board)
    return output

#defines minimax algorithm
def minimax(board, depth,alpha,beta,isMaximizing):
    #current_depth = 0
    if (checkWhichMarkWon(bot, board)):
        return 1
    elif (checkWhichMarkWon(player, board)):
        return -1
    elif (checkDraw(board)):
        return 0

    if (isMaximizing):
        bestScore = -math.inf
        for key in board.keys():

            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1,alpha, beta, False)
                board[key] = ' '
                alpha = max(alpha,score )
                if (score > bestScore):
                    bestScore = score
                if beta <= alpha:
                    break
        return bestScore
    else:
        bestScore = math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1,alpha,beta, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
                beta = min(beta,score)
                if beta <= alpha:
                    break
        return bestScore

#####--------------------------------------------------------------#####
def compMove2(board):
    bestScore = -math.inf
    alpha = -math.inf
    beta = math.inf
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = player
            score = minimax2(board, 0, alpha, beta, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    output = insertLetter(player, bestMove, board)
    return output

#defines minimax algorithm
def minimax2(board, depth,alpha,beta,isMaximizing):
    if (checkWhichMarkWon(player, board)):
        return 1
    elif (checkWhichMarkWon(bot, board)):
        return -1
    elif (checkDraw(board)):
        return 0

    if (isMaximizing):
        bestScore = -math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1,alpha, beta, False)
                board[key] = ' '
                alpha = max(alpha,score )
                if (score > bestScore):
                    bestScore = score
                if beta <= alpha:
                    break
        return bestScore
    else:
        bestScore = math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1,alpha,beta, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
                beta = min(beta,score)
                if beta <= alpha:
                    break
        return bestScore
#####--------------------------------------------------------------#####

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
        if (checkDraw(board)) and checkForWin(board)==False:
            output = "Draw!"
            print('Draw!')
            return output
            #exit()
        else:
            if checkForWin(board):
                if letter == 'X':
                    output = "Bot wins!"
                    print('Bot wins!')
                    return output
                else:
                    output = "Bot loses!"
                    print('Bot loses!')
                    return output

    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        output = insertLetter(letter, position, board)
        return output

#func to insert x or o into free position
def insertLetterRand(letter, position, board):
    if spaceIsFree(position, board):
        board[position] = letter
        #printBoard(board)
        if (checkDraw(board)) and checkForWin(board)==False:
            output = "Draw!"
            # print('Draw!')
            return output
        else:
            if checkForWin(board):
                if letter == 'X':
                    #print('Bot wins!')
                    output = "Bot wins!"
                    return output
                    #exit()
                else:
                    #print('Bot loses!')
                    output = "Bot loses!"
                    return output
                    #exit()
    else:
        position = random.randint(1,9)
        output = insertLetterRand(letter, position, board)
        return output

#func to check if space free
def spaceIsFree(position, board):
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

def main():
    board = initialise_board()
    while not checkForWin(board)== True and checkDraw(board)== False:
        #print('checkforwinnotcompleted')
        output = compMove(board)
        if not checkForWin(board)== True and checkDraw(board)== False:
            #print('checkforwinnotcompleted')
            output = compMove2(board)
    return output

if __name__ == "__main__":
    main()


