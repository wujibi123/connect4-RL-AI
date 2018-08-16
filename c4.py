import numpy as np
from mygrad import sliding_window_view

def create_board(rowcount, colcount):
    return np.zeros((rowcount, colcount))

def is_valid_move(board, col, rowcount):
    if board[0][col] == 0: #checks for the top space of specified column.
        return True
    else:
        return False

def get_next_open_row(board, col, rowcount): #determines the row in which the piece will be placed
    for i in range(rowcount):
        if board[i][col] != 0:
            return i - 1
    return rowcount - 1


def drop_piece(board, col, rowcount, piece): #updates the board based on get_next_open_row
    row = get_next_open_row(board, col, rowcount)
    board[row][col] = piece
    return None 

d1_filter = np.zeros((4, 4))#A 4x4 identity matrix(an array with ones across the main diagonal and zeros everywhere else)
for i in range(4):
    d1_filter[i][i] = 1

d2_filter = np.zeros((4, 4))#a transposed identity matrix(ones across the other diagonal)
for i in range(4):
    d2_filter[-1*(i+1)][i] = 1


def win_ver(board):
    h = sliding_window_view(board, (1, 4), (1,1)).reshape(-1, 4)#gets size (1, 4) windows(horizontal).
    for i in h:#compare the windows to see if they have 4 ones or 4 twos
        c = list(i)
        if c == [1, 1, 1, 1]:
            return True #True = player1 wins
        if c == [2, 2, 2, 2]:
            return False #False = player2 wins
    
    v = sliding_window_view(board, (4, 1), (1,1)).reshape(-1, 4)#gets size (4, 1) windows(vertical).
    for i in v:
        c = list(i)
        if c == [1, 1, 1, 1]:
            return True #True = player1 wins
        if c == [2, 2, 2, 2]:
            return False #False = player2 wins

    d1 = np.sum(sliding_window_view(board, (4, 4), (1,1)).reshape(-1, 4, 4) * d1_filter, axis = 1, dtype=int)
    #gets size (4, 4) windows(potential diagonal win). 
    #Apply identity matrix inorder to keep main diagonal. 
    #then flatten into shape(1, 4) arrays.
    for i in d1:
        c = list(i)
        if c == [1, 1, 1, 1]:
            return True #True = player1 wins
        if c == [2, 2, 2, 2]:
            return False #False = player2 wins
    
    d2 = np.sum(sliding_window_view(board, (4, 4), (1,1)).reshape(-1, 4, 4) * d2_filter, axis = 1, dtype=int)
    #same process using the second filter.
    for i in d2:
        c = list(i)
        if c == [1, 1, 1, 1]:
            return True #True = player1 wins
        if c == [2, 2, 2, 2]:
            return False #False = player2 wins
