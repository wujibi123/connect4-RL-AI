import numpy as np
import c4


rowcount = 6
colcount = 7

gameover = False
turn = 0

board = c4.create_board(rowcount, colcount)

print (f" {list(range(1, colcount+ 1))} \n  ------------------- \n {board}")

print(f"Welcome to Connect4! You can choose to place your dot among the {colcount} spots on the board.\n The first player to connect 4 dots together wins! Enter 'exit' at anytime during the game to quit.")


while not gameover: #starting the connect 4 game
	if turn % 2 == 0: #player 1 input
		while True:
			p1_input = input("Player 1, pick your spot!") #ask p1 input
			try: #checking if input is integer
				p1_input = int(p1_input) 
				p1_input -= 1
				if p1_input >= colcount or p1_input < 0: #checking if input out of range
					print("Please pick a number within the range of the board")
					continue
				else:
					if not c4.is_valid_move(board, p1_input, rowcount): #checking if the column has atleast one empty space
						print ("Please choose a valid move")
						continue
					else:
						break
			except ValueError:
				print ("Please pick an integer")
				continue
		c4.drop_piece(board, p1_input, rowcount, 1)
		print (f" {list(range(1, colcount+ 1))} \n  ------------------- \n {board}")

	else: #same procees for player2
		while True:
			p2_input = input("Player 2, pick your spot!") #ask p2 input
			try:
				p2_input = int(p2_input)
				p2_input -= 1
				if p2_input >= colcount or p2_input < 0:
					print("Please pick a number within the range of the board")
					continue
				else:
					if not c4.is_valid_move(board, p2_input, rowcount):
						print ("Please choose a valid move")
						continue
					else:
						break
			except ValueError:
				print ("Please pick an integer")
				continue
		c4.drop_piece(board, p2_input, rowcount, 2)
		print (f" {list(range(1, colcount+ 1))} \n  ------------------- \n {board}")

	win = c4.win_ver(board) #check for win

	if win == None:
		turn += 1
	elif win:
		print ("Player 1 won!")
		break
	else:
		print ("Player 2 won!")
		break
	
