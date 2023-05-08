import numpy as np
import pygame
import sys
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
def wining_move(board,piece):
    # Check Horizontal Locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True
    # Check Vertical Locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True
    # Check Positively Sloped Diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True
    # Check Negatively Sloped Diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,(0,0,255),(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,(0,0,0),(int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
    pygame.display.update()

pygame.init()
SQUARESIZE=100
width=COLUMN_COUNT*SQUARESIZE
height=(ROW_COUNT+1)*SQUARESIZE
size=(width,height)
RADIUS=int(SQUARESIZE/2-5)
screen=pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
while not game_over:
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                # Ask for Player 1 Input
                if turn == 0:
                    col = int(input("Player 1 Make your Selection (0-6):"))
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)
                    if wining_move(board, 1):
                        print("Player 1 Wins!!!")
                        game_over = True
                        break
                    turn = 1
                    # Ask for Player 2 Input
                else:
                    col = int(input("Player 2 Make your Selection (0-6):"))
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)
                    if wining_move(board, 2):
                        print("Player 2 Wins!!!")
                        game_over = True
                        break
                    turn = 0
                print_board(board)
                
