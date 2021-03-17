#Tic Tac Toe

board = [' ' for x in range(10)] #filling board with a bunch of blank spaces

#Insert letter into board list
def insertLetter(letter, pos) :
    board[pos] = letter
    pass 

#Check if space inserting into is free or not
def spaceIsFree(pos) :
    return board[pos] == ' ' #returns a true or false value

def printBoard(board) :
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#Checks for winner based on current board
def isWinner(bo, le) :
    return (bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove () :
    run = True #initial set run to true
    while run:
        move = input('Please select a position to place an X (1-9) :')
        try:
            move = int(move)
            if move > 0 and move < 10: #checking if between 1-9
                if spaceIsFree(move): #checing if space is free
                    run = False #if space is free, run is false so loop stops running
                    insertLetter('X', move)
                else:
                    print('space is not free- try another space')
            else:
                print('Please type a number within the range')
        except:
            print('Type a number')

def compMove () :
    pass

def selectRandom(board) :
    pass

#returns true or false if the board is full
def isBoardFull(board) :
    if board.count(' ') > 1:
        return True
    else:
        return False

def main() :
    print("Computer goes first! Good luck with the game!")
    print("Positions are as follow:")
    print("1, 2, 3 ")
    print("4, 5, 6 ")
    print("7, 8, 9 ")
    printBoard()

    while not(isBoardFull(board)): #If board is full- implies game is tied so dont continue while loop
        if not(isWinner(board, 'O')) : #Check to see if computer has won- straight line of o's
            playerMove() #no point in player moving since comp has won
            printBoard()
        else:
            print('Sorry, Comp wins!')
        break #out of while loop so doesnt continue if winner is found

        if not(isWinner(board, 'X' )) :
            move = compMove()
            if move == 0: #if unable to come up with a move
                print('Game is Tied!')
            else:
                insertLetter('O',board)
                print('Computer placed an O in position', move ,':')
                printBoard()
        else:
            print('Win! Good job!')
            break

    if isBoardFull(board) :
        print ('Game is Tied!')