"""evaluation function definitions and heuristics"""

current_board = []
BOARD_SIZE = 15

"""set the entire board to 0"""
def initialize_board(current_board):
    index_x = 0
    while index_x < BOARD_SIZE:
        index_y = 0
        while index_y < BOARD_SIZE:
            current_board[index_x][index_y] = 0
            index_y += 1
        index_x += 1


"""get next level of empty nodes"""
def get_next_level(current_board, c_player):
    all_poss = []
    index_x = 0
    while index_x < BOARD_SIZE:
        index_y = 0
        while index_y < BOARD_SIZE:
            if current_board[index_x][index_y] == 0:
                imaginary_board = current_board
                imaginary_board[index_x][index_y] = c_player
                all_poss.append(imaginary_board)
            index_y += 1
        index_x += 1
    return all_poss


def evaluate_value(board):
    return 0

