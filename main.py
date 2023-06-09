import numpy as np
import random
import pygame
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1

PLAYER_PIECE = 1
AI_PIECE = 2

EMPTY = 0
WINDOW_LENGTH = 4
choice=0
depth_level=0
import pygame
import sys

import pygame
import sys

# GUI setup
pygame.init()
SQUARESIZE = 100
width = 400
height = 200
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace", 20)

# Define message and button parameters
msg = "Choose an algorithm:"
msg_label = myfont.render(msg, 1, (0, 0, 0))
msg_x = int(width / 2 - msg_label.get_width() / 2)
msg_y = int(height / 4 - msg_label.get_height() / 2)

button_width = 120
button_height = 30
button_x_1 = int(width / 4 - button_width / 2)
button_x_2 = int(3 * width / 4 - button_width / 2)
button_y = int(height / 2 - button_height / 2)
button_color = (255, 0, 0)

# Define button labels
button_label_1_text = "Minimax"
button_label_1 = myfont.render(button_label_1_text, 1, (255, 255, 255))
button_label_x_1 = int(button_x_1 + button_width / 2 - button_label_1.get_width() / 2)
button_label_y = int(button_y + button_height / 2 - button_label_1.get_height() / 2)


button_label_2_text = "Alpha-Beta Minimax"
button_label_2 = myfont.render(button_label_2_text, 1, (255, 255, 255))
button_label_x_2 = int(button_x_2 + button_width / 2 - button_label_2.get_width() / 2)

# Display the message and buttons
screen.fill((255, 255, 255))
screen.blit(msg_label, (msg_x, msg_y))

pygame.draw.rect(screen, button_color, (button_x_1, button_y, button_width, button_height))
screen.blit(button_label_1, (button_label_x_1, button_label_y))

pygame.draw.rect(screen, button_color, (button_x_2, button_y, button_width, button_height))
screen.blit(button_label_2, (button_label_x_2, button_label_y))

pygame.display.update()

# Get the user's choice in the GUI
while not 1 <= choice <= 2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x_1 <= mouse_x <= button_x_1 + button_width and button_y <= mouse_y <= button_y + button_height:
                choice = 1
            elif button_x_2 <= mouse_x <= button_x_2 + button_width and button_y <= mouse_y <= button_y + button_height:
                choice = 2

    # Update the button colors to indicate the current choice
    button_color_1 = (0, 255, 0) if choice == 1 else (255, 0, 0)
    button_color_2 = (0, 255, 0) if choice == 2 else (255, 0, 0)
    screen.fill((255, 255, 255))
    screen.blit(msg_label, (msg_x, msg_y))
    pygame.draw.rect(screen, button_color_1, (button_x_1, button_y, button_width, button_height))
    screen.blit(button_label_1, (button_label_x_1, button_label_y))
    pygame.draw.rect(screen, button_color_2, (button_x_2, button_y, button_width, button_height))
    screen.blit(button_label_2, (button_label_x_2, button_label_y))
    pygame.display.update()
# GUI setup
pygame.init()
SQUARESIZE = 100
width = 6 * SQUARESIZE
height = 2 * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace", 45)
# Define button parameters
button_width = 80
button_height = 30
button_x_1 = int(width / 8 - button_width / 2)
button_x_2 = int(3 * width / 8 - button_width / 2)
button_x_3 = int(5 * width / 8 - button_width / 2)
button_x_4 = int(7 * width / 8 - button_width / 2)
button_y = int(height / 2 - button_height / 2)
button_color = (255, 0, 0)

# Define button labels
button_label_1_text = "1"
button_label_1 = myfont.render(button_label_1_text, 1, (255, 255, 255))
button_label_x_1 = int(button_x_1 + button_width / 2 - button_label_1.get_width() / 2)
button_label_y = int(button_y + button_height / 2 - button_label_1.get_height() / 2)

button_label_2_text = "2"
button_label_2 = myfont.render(button_label_2_text, 1, (255, 255, 255))
button_label_x_2 = int(button_x_2 + button_width / 2 - button_label_2.get_width() / 2)

button_label_3_text = "3"
button_label_3 = myfont.render(button_label_3_text, 1, (255, 255, 255))
button_label_x_3 = int(button_x_3 + button_width / 2 - button_label_3.get_width() / 2)

button_label_4_text = "4"
button_label_4 = myfont.render(button_label_4_text, 1, (255, 255, 255))
button_label_x_4 = int(button_x_4 + button_width / 2 - button_label_4.get_width() / 2)

# Display the message and buttons
screen.fill((255, 255, 255))
label = myfont.render("Enter depth level:", 1, (0, 0, 0))
screen.blit(label, (20, 10))

pygame.draw.rect(screen, button_color, (button_x_1, button_y, button_width, button_height))
screen.blit(button_label_1, (button_label_x_1, button_label_y))

pygame.draw.rect(screen, button_color, (button_x_2, button_y, button_width, button_height))
screen.blit(button_label_2, (button_label_x_2, button_label_y))

pygame.draw.rect(screen, button_color, (button_x_3, button_y, button_width, button_height))
screen.blit(button_label_3, (button_label_x_3, button_label_y))

pygame.draw.rect(screen, button_color, (button_x_4, button_y, button_width, button_height))
screen.blit(button_label_4, (button_label_x_4, button_label_y))

pygame.display.update()

# Get the depth level from the user in the GUI
while not 1 <= depth_level <= 4:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x_1 <= mouse_x <= button_x_1 + button_width and button_y <= mouse_y <= button_y + button_height:
                depth_level = 1
            elif button_x_2 <= mouse_x <= button_x_2 + button_width and button_y <= mouse_y <= button_y + button_height:
                depth_level = 2
            elif button_x_3 <= mouse_x <= button_x_3 + button_width and button_y <= mouse_y <= button_y + button_height:
                depth_level = 3
            elif button_x_4 <= mouse_x <= button_x_4 + button_width and button_y <= mouse_y <= button_y + button_height:
                depth_level = 4

    # Update the button colors to indicate the current choice
    button_color_1 = (0, 255, 0) if depth_level == 1 else (255, 0, 0)
    button_color_2 = (0, 255, 0) if depth_level == 2 else (255, 0, 0)
    button_color_3 = (0, 255, 0) if depth_level == 3 else (255, 0, 0)
    button_color_4 = (0, 255, 0) if depth_level == 4 else (255, 0, 0)
    screen.fill((255, 255, 255))
    label = myfont.render("Enter depth level:", 1, (0, 0, 0))
    screen.blit(label, (20, 10))
    pygame.draw.rect(screen, button_color_1, (button_x_1, button_y, button_width, button_height))
    screen.blit(button_label_1, (button_label_x_1, button_label_y))
    pygame.draw.rect(screen, button_color_2, (button_x_2, button_y, button_width, button_height))
    screen.blit(button_label_2, (button_label_x_2, button_label_y))
    pygame.draw.rect(screen, button_color_3, (button_x_3, button_y, button_width, button_height))
    screen.blit(button_label_3, (button_label_x_3, button_label_y))
    pygame.draw.rect(screen, button_color_4, (button_x_4, button_y, button_width, button_height))
    screen.blit(button_label_4, (button_label_x_4, button_label_y))
    pygame.display.update()

def create_board():
    board = np.zeros((6, 7))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[5][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


game_over = False
board = create_board()
print_board(board)


def wining_move(board, piece):
    # Check Horizontal Locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True
    # Check Vertical Locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True
    # Check Positively Sloped Diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True
    # Check Negatively Sloped Diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 100
    elif window.count(opp_piece) == 2 and window.count(EMPTY) == 2:
        score -= 5

    return score


def score_position(board, piece):
    score = 0

    ## Score center column
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    ## Score Horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    ## Score Vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    ## Score posiive sloped diagonal
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score


def terminal_node(board):
    return wining_move(board, PLAYER_PIECE) or wining_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0


def minimax(board, depth, maximizing_player):
    valid_locations = get_valid_locations(board)
    is_terminal = terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if wining_move(board, AI_PIECE):
                return None, 100000000000000
            elif wining_move(board, PLAYER_PIECE):
                return None, -10000000000000
            else:
                return None, 0
        else:
            return None, score_position(board, AI_PIECE)
    if maximizing_player:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, AI_PIECE)
            new_score = minimax(temp_board, depth - 1, False)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value
    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, PLAYER_PIECE)
            new_score = minimax(temp_board, depth - 1, True)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value
def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    valid_locations = get_valid_locations(board)
    is_terminal = terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if wining_move(board, AI_PIECE):
                return None, 100000000000000
            elif wining_move(board, PLAYER_PIECE):
                return None, -10000000000000
            else:
                return None, 0
        else:
            return None, score_position(board, AI_PIECE)
    if maximizing_player:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, AI_PIECE)
            new_score = minimax_alpha_beta(temp_board, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, PLAYER_PIECE)
            new_score = minimax_alpha_beta(temp_board, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


def pick_best_move(board, piece):
    valid_locations = get_valid_locations(board)
    best_score = -10000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col

    return best_col


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, (0, 0, 255), (c * SQUARESIZE,
                                                   r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, (0, 0, 0), (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, (255, 0, 0), (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, (255, 255, 0), (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

def isBoardFull(board):
    for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT):
            if board[i][j] == EMPTY:
                return False
    return True
pygame.init()
ok=0
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 75)
turn = random.randint(PLAYER, AI)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()

    if turn == PLAYER and not game_over:
        if choice == 1:
            col, minimax_score = minimax(board, depth_level, True)
        else:
            col, minimax_score = minimax_alpha_beta(board, depth_level, -math.inf, math.inf, True)
        if isBoardFull(board):
            label = myfont.render("Tie Game!!!", 1, (0, 255, 0))
            screen.blit(label, (40, 10))
            game_over = True
        elif is_valid_location(board, col):
            pygame.time.wait(700)
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, PLAYER_PIECE)
            if wining_move(board, PLAYER_PIECE):
                label = myfont.render("Player 1 Wins!!!", 1, (255, 0, 0))
                screen.blit(label, (40, 10))
                game_over = True
        turn = 1
        print_board(board)
        draw_board(board)

    # Ask for Player 2 Input
    if turn == AI and not game_over:
        col = pick_best_move(board, AI_PIECE)
        if isBoardFull(board):
            label = myfont.render("Tie!!!", 1, (0, 255, 0))
            screen.blit(label, (40, 10))
            game_over = True
        elif is_valid_location(board, col):
             pygame.time.wait(700)
             row = get_next_open_row(board, col)
             drop_piece(board, row, col, AI_PIECE)
             turn = 0
             if wining_move(board, AI_PIECE):
                label = myfont.render("Player 2 Wins!!!", 1, (255, 255, 0))
                screen.blit(label, (40, 10))
                game_over = True
        print_board(board)
        draw_board(board)

    if game_over:
        pygame.time.wait(3000)
