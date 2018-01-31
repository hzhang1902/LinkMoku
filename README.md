# cs4341_Proj_1

This is a minimax algorithm with alpha-beta pruning 
to play a game of Gomoku.

The game is played on a 15x15 board and have two players.
Each player places a stone on board each turn of their color, 
and whoever have 5 consecutive stones horizontally, vertically 
or diagonally wins the game.

Each player has 10 seconds each step to explore the search 
tree and decide where to put their stones, which is 
insufficient to come up with an optimal solution. However, by 
applying heuristics, the process will be greatly shortened, 
so how good the heuristic functions are is the deterministic 
factor of how good a player is.
#### Evaluation functions on each node
X1: The number of lines which there's 1 my stone and

E = X1 + 2X2 + 3X3 + 1000X4