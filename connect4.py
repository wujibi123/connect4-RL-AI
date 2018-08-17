import numpy as np
import c4
from os import system

rowcount = 6
colcount = 7



def main():
	board = c4.create_board(rowcount, colcount)
	print (f" {list(range(1, colcount+ 1))} \n{'-'*rowcount*4} \n {str(board)[1:-1]}")
	print(f"Welcome to Connect4! You can choose to place your dot among the {colcount} spots on the board.\nThe first player to connect 4 dots together wins! Press ctrl-d to exit any time")
    
	turn = 0
	while True: #starting the connect 4 game
		if turn % 2 == 0: #player 1 input
			while True:
				p1_input = input("\nPlayer 1, pick your spot!") #ask p1 input
				try:#checking if input is integer
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
			system("clear")
			print (f" {list(range(1, colcount+ 1))} \n{'-'*rowcount*4} \n {str(board)[1:-1]}")

		else: #same procees for player2
			while True:
				p2_input = input("\nPlayer 2, pick your spot!") #ask p2 input
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
			system("clear")
			print (f" {list(range(1, colcount+ 1))} \n{'-'*rowcount*4} \n {str(board)[1:-1]}")

		win = c4.win_ver(board) #check for win

		if win == None:
			turn += 1
		elif win:
			print ("Player 1 won!")
			break
		else:
			print ("Player 2 won!")
			break

if __name__ == "__main__":
	main()