import numpy as np
ROW_COUNT=6
COLUMN_COUNT=7
def create_board():
    board=np.zeros((6,7))
    return board
def drop_piece(board,row,col,piece):
    board[row][col]=piece

def is_valid_location(board,col):
    return board[5][col]==0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r
def print_board(board):
    print(np.flip(board,0))
game_over=False
board=create_board()
print_board(board)
turn=0
while not game_over:
    # Ask for Player 1 Input
    if turn==0:
        col=int(input("Player 1 Make your Selection (0-6):"))
        if is_valid_location(board,col):
            row=get_next_open_row(board,col)
            drop_piece(board,row,col,1)
        turn=1

    # Ask for Player 2 Input
    else:
        col = int(input("Player 2 Make your Selection (0-6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
        turn = 0
    print_board(board)