import Evals_Heuristics as eh
import time

"""engine of Minimax algorithm with alpha-beta pruning"""

BOARD_SIZE = 15
TIME_LIMIT = 9.5


class Minimax:
    
    def __init__(self, board): 
        self.board = board
        self.currentNode = None 
        self.successors = []
        # print "Successfully created minimax board."
        return
    
    """
    def thread_timer(self, second):
        #time.sleep(second)
        t = threading.Timer(9, minimax_decision)
        t.start()
    """


    def minimax_decision(self, current_board, c_player):
        start_time = time.time()
        print "deciding..."
        infinity = float('inf')
        MAX_DEPTH = 1
        D_LIMIT = 4
        best_move_e = None
        best_value = -infinity

        while MAX_DEPTH <= D_LIMIT:

            alpha = -infinity
            beta = infinity
            best_move = None
            # max_val = self.max_value(current_board, c_player) ###
            next_steps = eh.get_next_level(current_board, c_player) ### 
            #print "MiniMax:  Utility Value of Root Node: = " + str(max_val)
            #print next_steps
            # Find the best move
            for step in next_steps:
                current_depth = 0
                max_value = self.min_value(step, alpha, beta, c_player, current_depth, MAX_DEPTH, start_time)
                if max_value is None:
                    print "timeout, depth =", MAX_DEPTH
                    print "best_move"
                    for row in best_move_e:
                        print row
                    print best_value
                    return best_move_e
                if max_value > alpha:
                    alpha = max_value
                    best_move = step
            best_move_e = best_move
            best_value = alpha
            MAX_DEPTH += 1

        print "best_move"
        for row in best_move_e:
            print row
        print best_value
        return best_move_e

    def max_value(self, current_board, alpha, beta, max_player, last_depth, MAX_DEPTH, start_time):  # get the max value of the possible moves
        #print "MAX different" + str(time.time() - start_time)
        if time.time() - start_time > TIME_LIMIT:
            return None
        current_depth = last_depth + 1
        if current_depth >= MAX_DEPTH:
            return eh.evaluate_value(current_board, max_player)
        else:
            all_poss = eh.get_next_level(current_board, max_player)  # get the next steps
            if len(all_poss) <= 0:
                eval_value = eh.evaluate_value(current_board, max_player)
                #print "!!!MAX eval_value == " + str(eval_value)
                return eval_value

            max_value = alpha

            for poss in all_poss:
                #print "calc min"
                next_lvl_value = self.min_value(poss, max_value, beta, max_player, current_depth, MAX_DEPTH, start_time)
                if next_lvl_value is None:
                    return None
                max_value = max(max_value, next_lvl_value) # TODO
                #if max_value >= beta:
                    #return max_value
                if max_value >= beta:
                    return alpha
                #alpha = max(alpha, max_value)
            #print "calculate max value success"
            #print "max_value is: " + str(max_value)
            return max_value

    def min_value(self, current_board, alpha, beta, max_player, last_depth, MAX_DEPTH, start_time): # get the min value of the possible moves
        if time.time() - start_time > TIME_LIMIT:
            return None
        min_player = 1
        if max_player == 1:
            min_player = 2

        current_depth = last_depth + 1
        if current_depth >= MAX_DEPTH:
            #print "min end of depth, val =", eh.evaluate_value(current_board, max_player)
            return eh.evaluate_value(current_board, max_player)
        else:
            #print "MIN current_depth: " + str(current_depth)
            all_poss = eh.get_next_level(current_board, min_player)  # get the next steps

            if len(all_poss) <= 0:
                eval_value = eh.evaluate_value(current_board, max_player)
                #print "!!!MIN eval_value == " + str(eval_value)
                return eval_value
            
            min_value = beta

            for poss in all_poss:
                next_lvl_value = self.max_value(poss, alpha, min_value, max_player, current_depth, MAX_DEPTH, start_time)
                if next_lvl_value is None:
                    return None
                min_value = min(min_value, next_lvl_value)
                #if min_value <= alpha:
                    #return min_value
                if alpha >= min_value:
                    return beta
            #print "calculate min value"
            #print "min_value is: " + str(min_value)
            return min_value

# in ms


def board_full(board):
    x = 0
    while x < BOARD_SIZE:
        y = 0
        while y < BOARD_SIZE:
            if board[x][y] == 0:
                return False
            y += 1
        x += 1
    return True


