"""evaluation function definitions and heuristics"""

from copy import deepcopy

BOARD_SIZE = 15

# get an empty board
def initialize_board():
    current_board = []
    x = 0
    while x < BOARD_SIZE:
        col = [0]*BOARD_SIZE
        current_board.append(col)
        x += 1

    return current_board


# get next level of boards
def get_next_level(current_board, c_player):
    all_poss = []
    index_x = 0
    while index_x < BOARD_SIZE:
        index_y = 0
        while index_y < BOARD_SIZE:
            if current_board[index_x][index_y] == 0:
                imaginary_board = deepcopy(current_board)
                imaginary_board[index_x][index_y] = c_player
                # print imaginary_board
                all_poss.append(imaginary_board)
            index_y += 1
        index_x += 1
    return all_poss


def evaluate_value(current_board, c_player):
    return 0


def get_link(board, c_player, x, y):
    link = []
    link.count()

    return


def link_equal(link1, link2):
    if len(link1) != len(link2):
        print "length not equal"
        return False

    for i in link1:
        if link1.count(i) != link2.count(i):

            print "not match " + i.to_string()
            return False

    return True


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
            if board[index_x][index_y] == c_player:
                get_link(board, c_player, index_x, index_y)
            index_y += 1
        index_x += 1
    return 0


def num_y(board, c_player):
    return 0


def num_o(board, c_player):
    return 0


def num_p(board, c_player):
    return 0


class Stone:
    def __init__ (self, x, y, player):
        self.x = x
        self.y = y
        self.player = player

    def to_string(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"


board = initialize_board()
all_poss = get_next_level(board, 1)
# print all possibilities
"""
for poss in all_poss:
    for row in poss:
        print row
    print "\n"
"""
equalornot = link_equal([Stone(2,1,2), Stone(1,1,1)],
                        [Stone(1,1,1), Stone(2,1,2)])
print equalornot
