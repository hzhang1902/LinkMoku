import Evals_Heuristics as eh

"""engine of Minimax algorithm with alpha-beta pruning"""

current_board = []
BOARD_SIZE = 15

class Minimax:
    
    def __init__(self, board): 
        self.board = board
        #self.root = board.root
        self.currentNode = None 
        self.successors = []
        print "Successfully created minimax board."
        return


    def minimax_decision(self, current_board, c_player):
        max_val = self.max_value(current_board, c_player) ###
        next_steps = eh.get_next_level(current_board, c_player) ### 
        print "MiniMax:  Utility Value of Root Node: = " + str(max_val)
        
        # Find the best move
        best_move = None
        for step in next_steps:   
            if step.value == max_val:
                best_move = step
                break
        print "find best move success"
        return best_move


    def max_value(self, current_board, c_player):  # get the max value of the possible moves
        if self.isTerminal(current_board, c_player):
            return self.getEval(current_board, c_player)

        infinity = float('inf')
        max_value = -infinity

        all_poss = eh.get_next_level(current_board, c_player)  # get the next steps
        print "all poss:", all_poss
        # max_value_list = []
        for poss in all_poss:
            print "calc min"
            max_value = max(max_value, self.min_value(poss, c_player)) # TODO
        print "calculate max value success"
        return max_value


    def min_value(self, current_board, c_player): # get the min value of the possible moves
        #print "MiniMax-->MIN: Visited Node :: " + node.Name
        if self.isTerminal(current_board, c_player):
            return self.getEval(current_board)

        infinity = float('inf')
        min_value = infinity

        all_poss = eh.get_next_level(current_board, c_player)  # get the next steps
        for poss in all_poss:
            min_value = min(min_value, self.max_value(all_poss, c_player))
        print "calculate min value"
        return min_value
    
    def isTerminal(self, current_board, c_player):
        assert current_board is not None
        return len(eh.get_next_level(current_board, c_player)) == 0

    def getEval(self, current_board, c_player):
        assert current_board is not None
        return eh.evaluate_value(current_board, c_player)


#board = eh.initialize_board()
    """
board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,2,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            """
board = [[0,0,0], [0,2,0],[0,0,0]]
player1 = 1
player2 = 2
sudoku1 = Minimax(board)
sudoku1.minimax_decision(board, 1)
