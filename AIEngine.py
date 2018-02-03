import Evals_Heuristics as eh

"""engine of Minimax algorithm with alpha-beta pruning"""

current_board = []
BOARD_SIZE = 15

class Minimax:
    
    def __init__(self, gameTree): # gameTree is board?
        self.gameTree = gameTree
        #self.root = gameTree.root
        self.currentNode = None 
        self.successors = []
        print "Successfully created minimax gameTree."
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
            return self.getUtility(curren_board)

        infinity = float('inf')
        max_value = -infinity

        all_poss = eh.get_next_level(current_board, c_player)  # get the next steps
        print "all poss:", all_poss
        # max_value_list = []
        for poss in all_poss:
            print "calc min"
            max_value = max(max_value, self.min_value(poss)) # TODO
        print "calculate max value success"
        return max_value


    def min_value(self, current_board): # get the min value of the possible moves
        #print "MiniMax-->MIN: Visited Node :: " + node.Name
        if self.isTerminal(current_board):
            return self.getUtility(current_board)

        infinity = float('inf')
        min_value = infinity

        all_poss = eh.get_next_level(current_board, c_player)  # get the next steps
        for poss in all_poss:
            min_value = min(min_value, self.max_value(all_poss))
        print "calculate min value"
        return min_value

    # def getSuccessor in eval_Heuristic

    
    def isTerminal(self, current_board, c_player):
        assert current_board is not None
        return len(eh.get_next_level(current_board, c_player)) == 0

    def getUtility(self, current_board):
        assert current_board is not None
        return evaluate_value(current_board, c_player)


#gameTree = eh.initialize_board()
gameTree = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
player1 = 1
player2 = 2
sudoku1 = Minimax(gameTree)
sudoku1.minimax_decision(gameTree, 1)
