"""evaluation function definitions and heuristics"""

board = []


"""set the entire board to 0"""
def initialize_board():
    index_x = 0
    while index_x < 15:
        index_y = 0
        col = []
        while index_y < 15:
            col[index_y] = 0
            index_y += 1
        board[index_x] = col
        index_x += 1


"""get next level of empty nodes"""
def get_next_level(steps, c_player):
    update_board(steps)
    all_poss = []
    index_x = 0
    while index_x < 15:
        index_y = 0
        while index_y < 15:
            if board[index_x][index_y] == 0:
                new_poss = Node(index_x, index_y, c_player)
                all_poss.append(new_poss)
            index_y += 1
        index_x += 1
    return all_poss


"""update the board by a list of steps"""
def update_board(steps):
    for n in steps:
        x = n.X
        y = n.Y
        player = n.player
        board[x][y] = player


class Node:
    X = 0
    Y = 0
    player = 0

    def __init__(self, x, y, player):
        self.X = x
        self.Y = y
        self.player = player
