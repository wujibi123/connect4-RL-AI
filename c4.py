import numpy as np
from mygrad import sliding_window_view

def create_board(rowcount, colcount):
    return np.zeros((rowcount, colcount))

def is_valid_move(board, col, rowcount):
    if board[0][col] == 0:
        return True
    else:
        return False

def get_next_open_row(board, col, rowcount):
    for i in range(rowcount):
        if board[i][col] != 0:
            return i - 1
    return rowcount - 1


def drop_piece(board, col, rowcount, piece):
    row = get_next_open_row(board, col, rowcount)
    board[row][col] = piece
    return None

d1_filter = np.zeros((4, 4))
for i in range(4):
    d1_filter[i][i] = 1

d2_filter = np.zeros((4, 4))
for i in range(4):
    d2_filter[-1*(i+1)][i] = 1


def win_ver(board):
    h = sliding_window_view(board, (1, 4), (1,1)).reshape(-1, 4)
    for i in h:
        c = list(i)
        if c == [1, 1, 1, 1]:
            return True #True = player1 wins
        if c == [2, 2, 2, 2]:
            return False #False = player2 wins
    
    v = sliding_window_view(board, (4, 1), (1,1)).reshape(-1, 4)
    for i in v:
        c = list(i)
        if c == [1, 1, 1, 1]:
            return True #True = player1 wins
        if c == [2, 2, 2, 2]:
            return False #False = player2 wins

    d1 = np.sum(sliding_window_view(board, (4, 4), (1,1)).reshape(-1, 4, 4) * d1_filter, axis = 1, dtype=int)
    for i in d1:
        c = list(i)
        if c == [1, 1, 1, 1]:
            return True #True = player1 wins
        if c == [2, 2, 2, 2]:
            return False #False = player2 wins
    
    d2 = np.sum(sliding_window_view(board, (4, 4), (1,1)).reshape(-1, 4, 4) * d2_filter, axis = 1, dtype=int)
    for i in d2:
        c = list(i)
        if c == [1, 1, 1, 1]:
            return True #True = player1 wins
        if c == [2, 2, 2, 2]:
            return False #False = player2 wins

if __name__ == "__main__":
    print("Running c4")