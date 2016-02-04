
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################
    
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

theBoard={'top-L':'','top-M':'','top-R':'',
          'mid-L':'','mid-M':'','mid-R':'',
          'low-L':'','low-M':'','low-R':''}
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    return((board['top-L']==player and board['top-M']==player and board['top-R']==player) or #top horizontal
           (board['mid-L']==player and board['mid-M']==player and board['mid-R']==player) or #middle horizontal
           (board['low-L']==player and board['low-M']==player and board['low-R']==player) or #bottom horizontal
           (board['top-L']==player and board['mid-L']==player and board['low-L']==player) or #left vertical
           (board['top-M']==player and board['mid-M']==player and board['low-M']==player) or #middle vertical
           (board['top-R']==player and board['mid-R']==player and board['low-R']==player) or #right vertical
           (board['top-L']==player and board['mid-M']==player and board['low-R']==player) or #diagonal
           (board['top-R']==player and board['mid-M']==player and board['low-L']==player))  #diagonal

    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

def startGame(startingPlayer, board): 
    turn = startingPlayer #Here we designate the starting play/start of the game.
    for i in range(9): #Declares a for loop for the range of the 9 move options.
        printBoard(board) #Here the program prints the tic tac toe board.
        print('Turn for ' + turn + '. Move on which space?') #Here the program is asking the user whose turn it is what space they want to move.
        move = input() #Here is the user's decision as to where to move.
        board[move] = turn #Here we illustrate the board with the player's move on it.
        if( checkWinner(board, 'X') ): #Here the program calls the checkWinner function above to verify whether the X player is a winner.
            print('X wins!') #Here the program informs the X player they have won.
            break #Here the program breaks out of the for loop since a winner has been designated.
        elif ( checkWinner(board, 'O') ): #Here the program calls the checkWinner function above to verify whether the O player is a winner.
            print('O wins!') #Here the program informs the O player they have won.
            break #Here the program breaks out of the for loop since a winner has been designated.
    
        if turn == 'X':  #Here we are saying if it isn't X's turn it is O's turn.
            turn = 'O'
        else:
            turn = 'X' #Here we are saying if it isn't O's turn it is X's turn.

    printBoard(board)
    
