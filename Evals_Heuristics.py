"""evaluation function definitions and heuristics"""

<<<<<<< HEAD
current_board = []
=======

>>>>>>> master
BOARD_SIZE = 15


# get an empty board
def initialize_board():
    current_board = [[0]*15]*15
    return current_board


# get next level of boards
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


def evaluate_value(current_board, c_player):
    return 0

<<<<<<< HEAD
=======

def num_x(board, c_player):

    num_x1 = 0
    num_x2 = 0
    num_x3 = 0
    num_x4 = 0
    num_x5 = 0

    index_x = 0
    while index_x < BOARD_SIZE:
        index_y = 0
        while index_y < BOARD_SIZE:

            index_y += 1
        index_x += 1
    return 0

def num_y(board, c_player):
    return 0



def num_o(board, c_player):
    return 0


def num_p(board, c_player):
    return 0


>>>>>>> master
