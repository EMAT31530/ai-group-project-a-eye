#define the board env elements with grid
# Test for comment - B
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")

#func to check if space free
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False

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

#func to check for win
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

#check for a draw
def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

#func to allow user to input
def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return

#comp move uses minimax algorithm
def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot #play the move

            print('compmovefunction move:')
            #print(board)  # nathan added
            printBoard(board)  # nathan added

            print('call minimax')
            score = minimax(board, 0, False) #board is 0depth and minimising, output score at end of recursive (should be better than -800)
            board[key] = ' ' #clear the move
            print('end of comp move (reached terminal state)')
            print('compmovefunction bestScore (after comp move done):', bestScore, 'bestMove after comp move:', key)
            print('next comp move...')
            if (score > bestScore):
                bestScore = score

                bestMove = key #if the score is better than -800 then this is now bestscore and bestmove
    print('final bestscore:',bestScore)
    insertLetter(bot, bestMove)
    return

#defines minimax algorithm
def minimax(board, depth, isMaximizing):
    maxDepth = 0
    if (checkWhichMarkWon(bot)): #for end states only?
        print('found a win and do not execute anymore of minimax function for that iteration. Return +1 as score output to previously called minimax')
        return 1 #so rest of function is not executed as soon as something is returned
    elif (checkWhichMarkWon(player)):
        print('found a loss and do not execute anymore of minimax function for that iteration. Return -1 as score output to previously called minimax')
        return -1
    elif (checkDraw()):
        print('found a draw and do not execute anymore of minimax function for that iteration. Return 0 as score output to previously called minimax')
        return 0

    if (isMaximizing):
        bestScore = -800
        print('maximising,','bestScore (before maximising):',bestScore)  # nathan added
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot #make the move

                print('depth:',depth)# nathan added
                print(board) # nathan added
                printBoard(board)# nathan added

                if depth < maxDepth:
                    print('call minimise')
                    score = minimax(board, depth + 1, False) #recursive call minimax function but depth +1 and now minimising
                else:
                    print('max depth of',maxDepth,'reached')
                    print('bestScore:',bestScore)
                    return bestScore

                board[key] = ' ' #clear the move
                print('score after minimax on that key (maximising part):',score)
                print('current bestScore:', bestScore)
                if (score > bestScore):
                    bestScore = score
                    print('changed bestScore to:', bestScore)

        print('bestScore (after all moves tried with minimax(maximising part) - propogate score back:', bestScore)  # nathan added
        return bestScore


    else:
        bestScore = 800

        print('minimising,','bestScore (before minimising):',bestScore) #nathan added

        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player #make move (as an o)

                print('depth:', depth)  # nathan added
                print(board)#nathan added
                printBoard(board)#nathan added

                if depth < maxDepth:
                    print('call maximising')
                    score = minimax(board, depth + 1, True) #now call mimimax again but maximising (recursive)
                else:
                    print('max depth of',maxDepth,'reached')
                    print('bestScore:',bestScore)
                    return bestScore

                board[key] = ' ' #clear move
                print('score after minimax on that key (minimising part):',score)
                print('current bestScore:', bestScore)

                if (score < bestScore):
                    bestScore = score
                    print('changed bestScore to:', bestScore)

        print('bestScore (after all moves tried with minimax (minimising part) - propogate score back:', bestScore)  # nathan added
        return bestScore



#board = {1: ' ', 2: ' ', 3: ' ',
         #4: ' ', 5: ' ', 6: ' ',
         #7: ' ', 8: ' ', 9: ' '}

board = {1: 'X', 2: 'X', 3: ' ',
         4: 'O', 5: 'O', 6: ' ',
         7: 'X', 8: 'O', 9: ' '}

printBoard(board)
print("Computer goes first! Good luck with the game!")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'


global firstComputerMove
firstComputerMove = True



while not checkForWin():
    compMove()
    playerMove()
