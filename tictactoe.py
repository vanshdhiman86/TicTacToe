board = [" " for x in range(10)]
ghhjhvhvhvkhhv
def insert_letter(letter, pos):
	board[pos] = letter

def spaceisfree(pos):
	return board[pos] == " "

def printBoard(board):
	print("   |   |   ")
	print(" " + board[1] + " | " + board[2] + " | " + board[3] )
	print("   |   |   ")
	print("------------")
	print("   |   |   ")
	print(" " + board[4] + " | " + board[5] + " | " + board[6] )
	print("   |   |   ")
	print("------------")
	print("   |   |   ")
	print(" " + board[7] + " | " + board[8] + " | " + board[9] )
	print("   |   |   ")
	print("------------")

def isBoardfull(board):
	if board.count(" ") > 1:
		return False
	else:
		return True

def isWinner(b, l):
	return (b[1] == l and b[2] == l and b[3] == l) or (b[4] == l and b[5] == l and b[6] == l) or (b[7] == l and b[8] == l and b[9] == l) or (b[1] == l and b[4] == l and b[7] == l) or (b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l) or (b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l)

def playerMove():
	run = True
	while run:
		move = input("please select the position to enter the X between 1 to 9 ")
		try:
			move = int(move)
			if  move > 0 and move < 10:
				if spaceisfree(move):
					run = False
					insert_letter("X", move)
				else:
					print("Sorry, this space is occupied")
			else:
				print("please, enter number between 1 to 9")
			
		except:
			print("please enter a number")

def computerMoves():
	posssibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
	move = 0

	for let in ["O" , "X"]:
		for i in posssibleMoves:
			boardcopy = board[:]
			boardcopy[i] = let
			if isWinner(boardcopy, let):
				move = i
				return move

	cornersOpen = []
	for i in posssibleMoves:
		if i in [1, 3, 7, 9]:
			cornersOpen.append(i)

	if len(cornersOpen) > 0:
		move = selectRandom(cornersOpen)
		return move

	if 5 in posssibleMoves:
		move = 5
		return move

	edgesOpen = []
	for i in posssibleMoves:
		if i in [2,4,6,8]:
			edgesOpen.append(i)

	if len(edgesOpen) > 0:
		move = selectRandom(edgesOpen)
		return move

def selectRandom(li):
	import random
	ln = len(li)
	r = random.randrange(ln)
	return li[r]

def main():
	print("Welcome to the Game")
	printBoard(board)

	while not(isBoardfull(board)):
		if not(isWinner(board, "O")):
			playerMove()
			printBoard(board)
		else:
			print("Sorry, you loose!")
			break

		if not(isWinner(board, "X")):
			move = computerMoves()
			if move == None:
				print(" ")
			else:
				insert_letter("O", move)
				print("Computer placed O at position", move, "!")
				printBoard(board)
		else:
			print("You Win")
			break


	if isBoardfull(board):
		print("Tie Game")
x="y"
while x == "y":
	board = [" " for x in range(10)]
	print("---------------------")
	main()
	x = input("Do you want to play again (y/n) ").lower()
