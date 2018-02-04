"""evaluation function definitions and heuristics"""

from copy import deepcopy

BOARD_SIZE = 15


# get an empty board
def initialize_board():
    current_board = []
    index_x = 0
    while index_x < BOARD_SIZE:
        col = [0]*BOARD_SIZE
        current_board.append(col)
        index_x += 1
    return current_board


# get next level of boards
def get_next_level(board, c_player):
    all_poss = []
    index_y = 0
    while index_y < BOARD_SIZE:
        index_x = 0
        while index_x < BOARD_SIZE:
            if board[index_x][index_y] == 0:
                imaginary_board = deepcopy(board)
                imaginary_board[index_x][index_y] = c_player
                all_poss.append(imaginary_board)
            index_x += 1
        index_y += 1
    return all_poss


def link_direction(board, stone, already_linked, direction):

    if direction == "top_left":
        next_x = stone.x - 1
        next_y = stone.y + 1
    elif direction == "bottom_right":
        next_x = stone.x + 1
        next_y = stone.y - 1
    elif direction == "top_right":
        next_x = stone.x + 1
        next_y = stone.y + 1
    elif direction == "bottom_left":
        next_x = stone.x - 1
        next_y = stone.y - 1
    elif direction == "top":
        next_x = stone.x
        next_y = stone.y + 1
    elif direction == "bottom":
        next_x = stone.x
        next_y = stone.y - 1
    elif direction == "left":
        next_x = stone.x - 1
        next_y = stone.y
    elif direction == "right":
        next_x = stone.x + 1
        next_y = stone.y
    else:
        return None

    if (next_x < 0) or (next_x >= BOARD_SIZE) or (next_y < 0) or (next_y >= BOARD_SIZE):
        return [stone]

    if Stone(next_x, next_y, board[next_x][next_y]) in already_linked:
        return None

    if board[next_x][next_y] == 0:
        return [stone]

    elif board[next_x][next_y] == stone.player:
        next_line = link_direction(board, Stone(next_x, next_y, stone.player), already_linked, direction)
        if next_line is None:
            return None
        else:
            next_line.append(stone)
            return next_line
    else:
        o_player = 1
        if stone.player == 1:
            o_player = 2
        return [stone, Stone(next_x, next_y, o_player)]


def link_line(board, stone, already_linked, direction):
    if direction == "top_left_diagonal":
        side1_direction = "top_left"
        side2_direction = "bottom_right"
    elif direction == "top_right_diagonal":
        side1_direction = "bottom_left"
        side2_direction = "top_right"
    elif direction == "horizontal":
        side1_direction = "right"
        side2_direction = "left"
    elif direction == "vertical":
        side1_direction = "top"
        side2_direction = "bottom"
    else:
        return None

    line = []
    side1 = link_direction(board,
                           Stone(stone.x, stone.y, stone.player),
                           already_linked,
                           side1_direction)

    side2 = link_direction(board,
                           Stone(stone.x, stone.y, stone.player),
                           already_linked,
                           side2_direction)

    if (side1 is None) or (side2 is None):
        return None

    o_player = 1
    if stone.player == 1:
        o_player = 2

    num_o_player_stone = 0
    for a_stone in side1:
        if (a_stone.player == stone.player) and (not a_stone == stone):
            line.append(a_stone)
        elif a_stone.player == o_player:
            num_o_player_stone += 1

    for a_stone in side2:
        if (a_stone.player == stone.player) and (not a_stone == stone):
            line.append(a_stone)
        elif a_stone.player == o_player:
            num_o_player_stone += 1

    if len(line) > 0:
        line.append(stone)
    else:
        return None

    """print "current stone", stone.x, stone.y, "dir", direction
    for a_stone in line:
        print str(a_stone)
    """
    if num_o_player_stone > 1:
        return None
    elif num_o_player_stone > 0:
        return Link(line, "close")
    else:
        return Link(line, "open")


def contains_stone(a_list, stone):
    for a_stone in a_list:
        if a_stone.__eq__(stone):
            return True
    return False


# get a list of links given a board and a stone
def get_links(board, stone, already_linked):
    links = []

    # top left diagonal
    link = link_line(board, stone, already_linked, "top_left_diagonal")
    if (link is not None) and (len(link.stones) > 0):
        links.append(link)

    # vertical
    link = link_line(board, stone, already_linked, "vertical")
    if (link is not None) and (len(link.stones) > 0):
        links.append(link)

    # top right diagonal
    link = link_line(board, stone, already_linked, "top_right_diagonal")
    if (link is not None) and (len(link.stones) > 0):
        links.append(link)

    # horizontal
    link = link_line(board, stone, already_linked, "horizontal")
    if (link is not None) and (len(link.stones) > 0):
        links.append(link)

    return links
"""
def evaluate_value(board, c_player):
    return 0

"""
def evaluate_value(board, c_player):
    o_player = 1
    if c_player == 1:
        o_player = 2

    # list of links for current player
    evaluated_c_player_stones = []
    # list of links for other player
    evaluated_o_player_stones = []

    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0

    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0
    y5 = 0

    o1 = 0
    o2 = 0
    o3 = 0
    o4 = 0
    o5 = 0

    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0

    index_x = 0
    while index_x < BOARD_SIZE:
        index_y = 0
        while index_y < BOARD_SIZE:
            if board[index_x][index_y] == c_player:
                links = get_links(board, Stone(index_x, index_y, c_player), evaluated_c_player_stones)
                evaluated_c_player_stones.append(Stone(index_x, index_y, c_player))
                for link in links:
                    if len(link.stones) == 1:
                        if link.type == "open":
                            x1 += 1
                        else:
                            y1 += 1
                    elif len(link.stones) == 2:
                        if link.type == "open":
                            x2 += 1
                        else:
                            y2 += 1
                    elif len(link.stones) == 3:
                        if link.type == "open":
                            x3 += 1
                        else:
                            y3 += 1
                    elif len(link.stones) == 4:
                        if link.type == "open":
                            x4 += 1
                        else:
                            y4 += 1
                    elif len(link.stones) == 5:
                        if link.type == "open":
                            x5 += 1
                        else:
                            y5 += 1
            elif board[index_x][index_y] == o_player:
                links = get_links(board, Stone(index_x, index_y, o_player), evaluated_o_player_stones)
                evaluated_o_player_stones.append(Stone(index_x, index_y, o_player))
                for link in links:
                    if len(link.stones) == 1:
                        if link.type == "open":
                            o1 += 1
                        else:
                            p1 += 1
                    elif len(link.stones) == 2:
                        if link.type == "open":
                            o2 += 1
                        else:
                            p2 += 1
                    elif len(link.stones) == 3:
                        if link.type == "open":
                            o3 += 1
                        else:
                            p3 += 1
                    elif len(link.stones) == 4:
                        if link.type == "open":
                            o4 += 1
                        else:
                            p4 += 1
                    elif len(link.stones) == 5:
                        if link.type == "open":
                            o5 += 1
                        else:
                            p5 += 1
            index_y += 1
        index_x += 1


    return 3 * (x1 + 5*x2 + 12*x3 + 60*x4 + 1000*x5) + (y1 + 3*y2 + 9*y3 + 50*y4 + 1000*y5) \
        - 2 * (3*(o1 + 5*o2 + 12*o3 + 60*o4 + 1000*o5) + (p1 + 3*p2 + 9*p3 + 50*p4 + 1000*p5))


class Stone:
    def __init__(self, x_pos, y_pos, player):
        self.x = x_pos
        self.y = y_pos
        self.player = player

    def __str__(self):
        return "[" + str(self.x) \
               + "," + str(self.y) \
               + "," + str(self.player) \
               + "]"

    def __eq__(self, other):
        if self.x == other.x \
                and self.y == other.y \
                and self.player == other.player:
            return True
        else:
            return False


class Link:
    def __init__(self, list_of_stone, link_type):
        self.stones = list_of_stone
        self.type = link_type

    def __eq__(self, other):
        if len(self.stones) != len(other.stones):
            return False

        for stone in self.stones:
            if self.stones.count(stone) != other.stones.count(stone):
                return False

        return True

"""
new_board = initialize_board()
new_board[1][1] = 1
new_board[2][2] = 1
poss = get_next_level(new_board, 1)

# print all possibilities


for one_poss in poss:
    print evaluate_value(one_poss, 1)
    y = BOARD_SIZE - 1
    while y >= 0:
        x = 0
        row = []
        while x < BOARD_SIZE:
            row.append(one_poss[x][y])
            x += 1
        print row
        y -= 1
    print "\n"
"""
