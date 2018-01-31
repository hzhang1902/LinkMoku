import Evals_Heuristics

"""engine of Minimax algorithm with alpha-beta pruning"""

class Minimax(object):
    
    def __init__(self, gameTree):
        self.gameTree = gameTree
        self.root = gameTree.root
        self.currentNode = None 
        self.successors = []
        print "Successfully created minimax gameTree."
        return


    def minimax_decision(self, nodeList):  # nodeList is all the possible moves

        max_val = self.max_value(nodeList) 
        successors = self.getSuccessors(nodeList) ###
        print "MiniMax:  Utility Value of Root Node: = " + str(max_val)
        
        # Find the best move
        best_move = None
        for elem in successors:   
            if elem.value == max_val:
                best_move = elem
                break

        return best_move


    def max_value(self, nodeList):  # get the max value of the possible moves
        for node in nodeList:
            print "MiniMax-->MAX: Visited Node :: " + node.Name
            if self.isTerminal(node):
                return self.getUtility(node)

            infinity = float('inf')
            max_value = -infinity

            successors_states = self.getSuccessors(node)  # TODO getSuccessor
            max_value_list = []
            for state in successors_states:
                max_value = max(max_value, self.min_value(state))
                max_value_list.append(max_value)               
        return max_value_list


    def min_value(self, node): # get the min value of the possible moves
        print "MiniMax-->MIN: Visited Node :: " + node.Name
        if self.isTerminal(node):
            return self.getUtility(node)

        infinity = float('inf')
        min_value = infinity

        successor_states = self.getSuccessors(node)  # TODO getSuccessor
        for state in successor_states:
            min_value = min(min_value, self.max_value(state))
        return min_value

    # def getSuccessor in heuristic

    
    def isTerminal(self, node):
        assert node is not None
        return len(node.children) == 0

    def getUtility(self, node):
        assert node is not None
        return node.value

