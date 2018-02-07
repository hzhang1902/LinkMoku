"""evaluation function definitions and heuristics"""

from copy import deepcopy

BOARD_SIZE = 15
LENGTH_TO_WIN = 5


# get an empty board
def initialize_board():
    current_board = []
    index_x = 0
    while index_x < BOARD_SIZE:
        col = [0]*BOARD_SIZE
        current_board.append(col)
        index_x += 1
    return current_board


def update_board(board, stone):
    board[stone.x][stone.y] = stone.player


def get_step(old_board, new_board):
    index_x = 0
    while index_x < BOARD_SIZE:
        index_y = 0
        while index_y < BOARD_SIZE:
            if not old_board[index_x][index_y] == new_board[index_x][index_y]:
                return Stone(index_x, index_y, new_board[index_x][index_y])
            index_y += 1
        index_x += 1
    return None


# get next level of boards
def get_next_level(board, c_player):
    normal_poss = []
    priority_poss = []

    index_y = 0
    while index_y < BOARD_SIZE:
        index_x = 0
        while index_x < BOARD_SIZE:
            if board[index_x][index_y] == 0:
                heu_value = eval_heuristics(board, Stone(index_x, index_y, c_player))
                imaginary_board = deepcopy(board)
                imaginary_board[index_x][index_y] = c_player
                if heu_value == "normal":
                    normal_poss.append(imaginary_board)
                elif heu_value == "priority":
                    priority_poss.append(imaginary_board)
            index_x += 1
        index_y += 1

    priority_poss.extend(normal_poss)
    return priority_poss


def eval_heuristics(old_board, stone):

    # discard possibilities with manhattan distance to nearest existing stone > 4
    stone_within_area = False
    min_x = 1 - LENGTH_TO_WIN
    max_x = LENGTH_TO_WIN
    min_y = 1 - LENGTH_TO_WIN
    max_y = LENGTH_TO_WIN
    if stone.x + min_x < 0:
        min_x = 0 - stone.x
    if stone.x + max_x >= BOARD_SIZE:
        max_x = BOARD_SIZE - stone.x
    if stone.y + min_y < 0:
        min_y = 0 - stone.y
    if stone.y + max_y >= BOARD_SIZE:
        max_y = BOARD_SIZE - stone.y
    x = min_x
    while x < max_x:
        y = min_y
        while y < max_y:
            if old_board[stone.x + x][stone.y + y] > 0:
                stone_within_area = True
                break
            y += 1
        if stone_within_area:
            break
        x += 1
    if not stone_within_area:
        return "discard"

    # prioritize 3/3, 4/3, 4/4 situations
    return "normal"


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

    o_player = 1
    if stone.player == 1:
        o_player = 2

    if (next_x < 0) or (next_x >= BOARD_SIZE) or (next_y < 0) or (next_y >= BOARD_SIZE):
        # if next stone is out of board
        # pretend it's blocked by other player's stone
        return [stone, Stone(next_x, next_y, o_player)]

    if Stone(next_x, next_y, board[next_x][next_y]) in already_linked:
        # this link is already explored, give up
        return None

    if board[next_x][next_y] == 0:
        # link ends
        return [stone]

    elif board[next_x][next_y] == stone.player:
        # recursion until link ends or blocked by other player's stone
        next_line = link_direction(board, Stone(next_x, next_y, stone.player), already_linked, direction)
        if next_line is None:
            return None
        else:
            next_line.append(stone)
            return next_line
    else:
        # add other player's stone as well
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

    """
    print "current stone", stone.x, stone.y, stone.player, "dir", direction
    for a_stone in line:
        print str(a_stone)
    """
    if len(line) <= 0:
        return None

    line.append(stone)

    # a double closed link
    if num_o_player_stone > 1:
        if len(line) >= 5:
            return Link(line, "close")
        else:
            return None
    elif num_o_player_stone > 0:
        return Link(line, "close")
    else:
        return Link(line, "open")


# get a list of links given a board and a stone
def get_links(board, stone, already_linked):
    links = []
    added = 0

    # top left diagonal
    link = link_line(board, stone, already_linked, "top_left_diagonal")
    if (link is not None) and (len(link.stones) > 1):
        added += 1
        links.append(link)

    # vertical
    link = link_line(board, stone, already_linked, "vertical")
    if (link is not None) and (len(link.stones) > 1):
        added += 1
        links.append(link)

    # top right diagonal
    link = link_line(board, stone, already_linked, "top_right_diagonal")
    if (link is not None) and (len(link.stones) > 1):
        added += 1
        links.append(link)

    # horizontal
    link = link_line(board, stone, already_linked, "horizontal")
    if (link is not None) and (len(link.stones) > 1):
        added += 1
        links.append(link)

    if added == 0:
        if stone.x + 1 < BOARD_SIZE and \
                stone.y + 1 < BOARD_SIZE and \
                board[stone.x + 1][stone.y + 1] == 0:
            added += 1
        if stone.x + 1 < BOARD_SIZE and \
                board[stone.x + 1][stone.y] == 0:
            added += 1
        if stone.x + 1 < BOARD_SIZE and \
                stone.y - 1 >= 0 and \
                board[stone.x + 1][stone.y - 1] == 0:
            added += 1
        if stone.x - 1 >= 0 and \
            stone.y + 1 < BOARD_SIZE and \
                board[stone.x - 1][stone.y + 1] == 0:
            added += 1
        if stone.x - 1 >= 0 and \
                board[stone.x - 1][stone.y] == 0:
            added += 1
        if stone.y - 1 >= 0 and \
                stone.x - 1 >= 0 and \
                board[stone.x - 1][stone.y - 1] == 0:
            added += 1
        if stone.y + 1 < BOARD_SIZE and \
                board[stone.x][stone.y + 1] == 0:
            added += 1
        if stone.y + 1 >= 0 and \
                board[stone.x][stone.y - 1] == 0:
            added += 1

        if added >= 8:
            links.append(Link([stone], "open"))
        elif added > 0:
            links.append(Link([stone], "close"))

    return links


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

    """
    print "x1 =", x1
    print "x2 =", x2
    print "x3 =", x3
    print "x4 =", x4
    print "x5 =", x5

    print "y1 =", y1
    print "y2 =", y2
    print "y3 =", y3
    print "y4 =", y4
    print "y5 =", y5

    print "o1 =", o1
    print "o2 =", o2
    print "o3 =", o3
    print "o4 =", o4
    print "o5 =", o5

    print "p1 =", p1
    print "p2 =", p2
    print "p3 =", p3
    print "p4 =", p4
    print "p5 =", p5
    """
    eval1 = 3 * (y1 + 10*x2 + 100*x3 + 500*x4) + 10000*x5 + (x1 + 10*y2 + 100*y3 + 500*y4 + 10000*y5) \
        - 2 * (3 * (p1 + 10*o2 + 100*o3 + 500*o4) + 10000*o5 + (o1 + 10*p2 + 100*p3 + 500*p4 + 10000*p5))
    return eval1


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

