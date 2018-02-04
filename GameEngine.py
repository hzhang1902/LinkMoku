import AIEngine
import os
import time
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
	x = unparsedMoves[1]
	y = unparsedMoves[2]

	print x
	print y

def writeMove(colum, row):
	f = open("move_file", "w")
	f.write(hometeamName+" "+ colum + " "+ row)
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
			writeMove("C", "9")
			number = letter2Int("K")
			letter = Int2Letter(13)
			print number
			print letter
rungame()


