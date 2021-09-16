board = [' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos]=letter
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def playerMove():
    run = True
    while run:
        move = input('Select the position to place X (1-9): ')
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceIsFree(move):
                    run=False
                    insertLetter('X',move)
                else:
                    print('Sorry the space is not available')

            else:
                print('Please type a number within the range')

        except:
            print('please type a number')

def spaceIsFree(pos):
    return board[pos] == ' '
def compMove():
    import random
    possibleMoves = []
    for x, letter in enumerate(board):
        if letter == ' ' and x > 0:
            possibleMoves.append(x)
    move=0
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i]=let
            if isWinner(boardCopy,let):
                move = i
                return move
    if 5 in possibleMoves:
        move=5
        return move
    cornersOpen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len (cornersOpen)>0:
        move = cornersOpen[random.randrange(0,len(cornersOpen))]
        return move

    edgesOpen= []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len (edgesOpen)>0:
        move = edgesOpen [random.randrange(0,len(edgesOpen))]

    return move



def printBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
def isWinner(bo,le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or  (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or  (bo[9] == le and bo[6] == le and bo[3] == le) or  (bo[7] == le and bo[5] == le and bo[3] == le) or (bo[9] == le and bo[5] == le and bo[1] == le))

def main():

    print('welcome to the game')
    printBoard(board)
    while not (isBoardFull(board)):
        if not (isWinner(board,'O')):
            playerMove()
            printBoard(board)

        else:
            print('sorry, O\'s won this time! ')
            break
        if not (isWinner(board,'X')):
            move=compMove()
            if move==0:
                break
            else:
                insertLetter('O',move)
                print('Computer Placed O in position ',move,':')
                printBoard(board)



        else:
            print('X\'s won this time! Well Done.. ')
            break



    if isBoardFull(board):
        print('Game is over, it is Tie !')
main()
play=True
while play:
    ans=input ('play again? y/n:')

    if ans=='n':
            play=False
            print('ending the game..')



    elif ans=='y':
            print('loading new game...')
            board = [' ' for x in range(10)]
            main()
    else:
            print('please only enter either character "y" or "n" :')





