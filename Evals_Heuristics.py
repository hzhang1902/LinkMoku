"""evaluation function definitions and heuristics"""

<<<<<<< HEAD
board = []

=======

current_board = []
>>>>>>> master

"""set the entire board to 0"""
def initialize_board():
    index_x = 0
    while index_x < 15:
        index_y = 0
        while index_y < 15:
            current_board[index_x][index_y] = 0
            index_y += 1
        index_x += 1


"""get next level of empty nodes"""
def get_next_level(steps, c_player):
    imaginary_board = current_board
    update_imaginary_board(steps, imaginary_board)
    all_poss = []
    index_x = 0
    while index_x < 15:
        index_y = 0
        while index_y < 15:
            if imaginary_board[index_x][index_y] == 0:
                new_poss = Node(index_x, index_y, c_player)
                all_poss.append(new_poss)
            index_y += 1
        index_x += 1
    return all_poss


"""update the board by a list of steps"""
def update_imaginary_board(steps, imaginary_board):
    for n in steps:
        x = n.X
        y = n.Y
        player = n.player
        imaginary_board[x][y] = player


def update_current_board(node):
    current_board[node.X][node.Y] = node.player


def evaluate_value():
    return 0


class Node:
    X = 0
    Y = 0
    player = 0

    def __init__(self, node_x, node_y, node_player):
        self.X = node_x
        self.Y = node_y
        self.player = node_player