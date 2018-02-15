# LinkMoku
Team: Haofan Zhang, Ziyang Yu, Yaofeng Wang

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

## To run the code
1. Install Python 2.7
2. Go to source code directory with command line
3. Run with "python GGboy.py"

## Evaluation function
```
X1: The number single stones which is not connected with any 
of my other stones, and also not neighboring any other of the 
opponent's stones

X2: The number of lines which there are 2 of my stones connected 
and no opponent's stone blocks the line from expanding

X3: The number of lines which there are 3 of my stones connected 
and no opponent's stone blocks the line from expanding

X4: same thing but with 4 stones

X5: same thing but with 5 stones


Y1: The number single stones which are not connected with any 
of my other stones, but are neighbors at least one of the 
opponent's stones, but are also not completely surrounded 
by opponent's stones

Y2: The number of lines which there are 2 of my stones connected 
and but blocked at one side by opponent's stone 

Y3: same thing but with 3 stones

Y4: same thing but with 4 stones

Y5: same thing but with 5 stones

O1-O5: same as X1-X5 but in opponent's perspective

P1-P5: same as Y1-Y5 but in opponent's perspective

E(board) = 3 * (y1 + 10*x2 + 100*x3 + 500*x4) + 10000*x5 + (x1 + 10*y2 + 100*y3 + 500*y4 + 10000*y5)
- 2 * (3 * (p1 + 10*o2 + 100*o3 + 500*o4) + 10000*o5 + (o1 + 10*p2 + 100*p3 + 500*p4 + 10000*p5))
```

Details:

1. The reason to give more point for the opponent's links is to
reduce the possibility of the program being over aggressive
and try to accomplish something great for itself without 
looking at the risk. But I also don't want it to be too 
passive and defend all the time even if it is winning.

2. Also 2*x3 > y4 but < x4, as y4 is not a win, opponent can 
still block it because it's closed on one end. But 3/3 open 
is a win condition, so the program will try to make more x3s
and give up chances on y4. But x4 is also a win condition, 
and is easier to achieve, so if we can do x4, why bother 
doing 3/3?

3. Assigning more points for y1 and p1, which seems to be odd 
given they are closed, is to incentify the program to 
influence the main combat area more in early game rather 
than escaping from the opponent to keep an open x1. 

## Heuristics
1. Avoid expanding all possibilities which the new stone is 
more than 4 manhattan distance away from any other stones
This is because they will not affect anyone trying to do a 
5-link, so why bother?
2. Always go for H 8 when possible, it's just experience
3. We planned to favor 3/3, 4/3 and 4/4, but we just don't
have enough time. It will be super strategic if we did so, 
pretty unfortunate.

## Results
We started by creating half finished games
and let it decide which step to take, and 
see if it differs from us human. It is very sharp at 
interpreting the board itself, often finds out a diagonal of 
possibility we overlooked. I made it play against itself, and 
was pretty surprised to see that even though player2 with 
the first move was very aggressive and forced player1 to 
always defend and unable to develop effective attacks, player1
wins because player2 didn't have enough time to check out 
unlinked connections which could potentially be an open 4 or 5.

Therefore the strengths and weaknesses are pretty clear:
It will not overlook any diagonals or connections, but given 
the short time (<10s), it is only able to think 1-3 steps 
further, which is no better, if not worse than human players.
This specific one cannot see anything with a space between 
the links, because writing such board parser is time consuming 
af. I would say it will be relatively easy for a human player 
to beat it if he/she knows about these weaknesses and plans 
a 3/3, 4/3 or 4/4 attack.
