import numpy as np 
import pygame
import sys 
#==================================================================================


ROW_COUNT = 6
COL_COUNT = 7
#^^ a global variable 

def create_board():
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece
    # ^^ fill in the board with whatever piece the player dropped

 
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0
    # ^^^ if the top col of the row [5th row] is 0 for the col you selected, 
    # then it is okay to drop a piece in that row
     

def get_next_open_row(board, col):
    for r in range(ROW_COUNT): # counts from r to (ROW_COUNT - 1)
        if board[r][col] == 0:
            return r
        # ^^ if the r = to 0, then it is emoty so return the first instance it is empty
         
def print_board(board):
    print(np.flip(board, 0)) # o is the axis

def winning_move(board, piece):
    # check all the horizontial locations
    for c in range(COL_COUNT - 3): # subtracted 3 because 3 of those col wouldnt work. you need 4 in a row to win.
        for r in range(ROW_COUNT): # horizontial win
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True 
    
    # verticle locations
    for c in range(COL_COUNT): # subtracted 3 because 3 of those col wouldnt work. you need 4 in a row to win.
        for r in range(ROW_COUNT-3): 
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True 

    # check for positively sloped diagnals 
    for c in range(COL_COUNT - 3): # subtracted 3 because 3 of those col wouldnt work. you need 4 in a row to win.
        for r in range(ROW_COUNT): 
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True 

    #check for the negatively sloped diaganols 
    for c in range(COL_COUNT - 3): # subtracted 3 because 3 of those col wouldnt work. you need 4 in a row to win.
        for r in range(3, ROW_COUNT): 
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True 

#==================================================================================
def draw_board(board):
    pass


# while loop
board = create_board() 
print_board(board) 
game_over = False # only becomes True when someone gets a 4 in a row
turn = 0

# need to start by inititalizing pygame
pygame.init() 
SQUARESIZE = 100 
width = COL_COUNT * SQUARESIZE
height = ROW_COUNT + 1 * SQUARESIZE # + 1 because added an aditional row where the piece will be

size = (width, height)
screen = pygame.display.set_mode(size)  # to get pygame to read size


# define screen size how big do you want to screen


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # allowing game to properly x out
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN: # THE GAME WILL RUN BY CLICKING DOWN ONA SPECIFC SPOT ON THE SCREEN WHERE U WANT TO DROP THE PIECE
            print("")
            """ # ask player one input
            if turn == 0:
                col = int(input('Player1 make your selection (0-6): '))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1) # player 1 the piece is 1

                    if winning_move(board, 1): # board and piece 1
                        print('Player1 Wins')
                        game_over = True


            # ask player two input
            else:
                col = int(input('Player2 make your selection (0-6): '))
                
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2) # player 2 the piece is 1
                    
                    if winning_move(board, 2): # board and piece 1
                        print('Player2 Wins')
                        game_over = True
                        break # to break out the loop if dont want to see boards turning at the end


            print_board(board) # calling the print_board function

            turn += 1
            # no matters whole turn it is, you want to increase turn by 1
            turn = turn % 2
            # ^^ turn = mod 2 means to take the reaminder of what our turn is and divide it by two. 
            # this willalternate between 0 and one so plyer one and player 2's turn
        #==================================================================================
 """