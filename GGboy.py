import AIEngine as aie
import os
import time
import Evals_Heuristics as eh
"""game engine, I/O"""

hometeamName = "GGboy"
# initialize an empty board
a_board = eh.initialize_board()
# initialize engine
minimax_engine = aie.Minimax(a_board)

# scan the file
def scanFile():
	scanFile = [f for f in os.listdir('.') if os.path.isfile(f)]
	# return a list fo scanned file
	return scanFile

def readMove():
	f = open("move_file","r")
	text = f.read()
	f.close()
	unparsedMoves = text.split(" ")
	player = 0
	if(unparsedMoves[0] == hometeamName):
		player = 1
	else:
		player = 2
	x = letter2Int(unparsedMoves[1])
	y = int(unparsedMoves[2]) - 1
	a_board[x][y] = player


def writeMove(colum, row):
	x = Int2Letter(colum)
	y = str(row + 1)
	f = open("move_file", "w")
	f.write(hometeamName+" "+ x + " "+ y)
	f.close()
	a_board[colum][row] = 1

def letter2Int(letter):
	letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
	i = 0
	for l in letters:
		if(letter == l):
			return i
		i += 1

def Int2Letter(number):
	letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
	i = 0
	for l in letters:
		if(i == number):
			return l
		i += 1


def rungame():
	# checker for the first move
	gameround = 1
	while True:
		files = scanFile()
		for f in files:
			if f == "end_game":
				return
			if f == hometeamName + ".go":
				if gameround == 1:
					writeMove(7, 7)
					gameround += 1
					time.sleep(0.3)
					continue
				else:
					readMove()
					# decide next step and return the new_board
					next_move = minimax_engine.minimax_decision(a_board, 1)
					# get next step's stone by comparing the new_board and the old_board
					next_stone = eh.get_step(a_board, next_move)
					writeMove(next_stone.x, next_stone.y)
					time.sleep(0.3)
					continue

rungame()
