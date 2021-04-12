import math
import time
import random

player = 'O'
bot = 'X'

#func to allow playing a player who places pieces randomly
def randMove(board):
    position = random.randint(1,9)
    insertLetterRand(player, position, board)
    return

#func to allow playing a player who places pieces randomly
def randMove2(board):
    position = random.randint(1,9)
    insertLetterRand2(bot, position, board)
    return

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
def insertLetterRand(letter, position, board):
    if spaceIsFree(position, board):
        board[position] = letter
        printBoard(board)
        if (checkDraw(board)) and checkForWin(board)==False:
            print("Draw!")
            #exit()
        else:
            if checkForWin(board):
                if letter == 'X':
                    print("Bot wins!")
                    #exit()
                else:
                    print("Bot loses!")
                    #exit()
        return

    else:
        position = random.randint(1,9)
        insertLetterRand(letter, position, board)
        return

#func to insert x or o into free position
def insertLetterRand2(letter, position, board):
    if spaceIsFree(position, board):
        board[position] = letter
        printBoard(board)
        if (checkDraw(board))and checkForWin(board)==False:
            print("Draw!")
            #exit()
        else:
            if checkForWin(board):
                if letter == 'X':
                    print("Bot wins!")
                    #exit()
                else:
                    print("Bot loses!")
                    #exit()
        return

    else:
        position = random.randint(1,9)
        insertLetterRand(letter, position, board)
        return

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
        randMove2(board)
        if not checkForWin(board)== True and checkDraw(board)== False:
            #print('checkforwinnotcompleted')
            randMove(board)

if __name__ == "__main__":
    main()




