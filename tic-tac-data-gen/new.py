player = 'O'
bot = 'X'

#func to allow user to input
def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return

#func to insert x or o into free position
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return

    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return

#func to check if space free
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False

#check for a draw
def checkDraw():
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
    while not checkForWin(board):
        playerMove()

    #print("Hello World!")


if __name__ == "__main__":
    main()


