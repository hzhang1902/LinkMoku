import AIEngine
import os
import time
import Evals_Heuristics as eh
"""game engine, I/O"""

hometeamName = "ggboys"
guestteamName = raw_input("Who am I playing againt?\n")

def scanFile():
	scanFile = [f for f in os.listdir('.') if os.path.isfile(f)]
	return scanFile

def readMove():
	f = open("move_file","r")
	text = f.read()
	f.close()
	unparsedMoves = text.split(" ")
	player = 0
	if(unparsedMoves[0] == hometeamName):
		player = 1
	if(unparsedMoves[0] == guestteamName):
		player = 2
	x = letter2Int(unparsedMoves[1])
	y = int(unparsedMoves[2]) - 1
	move = eh.Stone(x, y, player)
	print move
	return move

def writeMove(colum, row):
	x = Int2Letter(colum)
	y = str(row + 1)
	f = open("move_file", "w")
	f.write(hometeamName+" "+ x + " "+ y)
	f.close()

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
	files = scanFile()
	for f in files:
		if f == "end_game":
			return
		if f == guestteamName + ".go":
			time.sleep(2)
			print "===========waited for 2 secs ================"
			rungame()
		if f == hometeamName + ".go":
			readMove()
			writeMove(0, 0)
			readMove()

rungame()
