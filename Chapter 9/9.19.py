#. Randomly generate a 9 × 9 list where the entries are integers between 1 and 9 with no repeat entries in any row or in any column

import random

def generate_board():
    board = [[0]*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            board[i][j] = (i*3 + i//3 + j) % 9 + 1
    for i in range(9):
        random.shuffle(board[i])
    random.shuffle(board)
    return board

board = generate_board()
for row in board:
    print(row)
