# Write a text-based version of the game Memory. The game should generate a 5 × 5 board (see
# the exercise from Chapter 8). Initially the program should display the board as a 5 × 5 grid of
# asterisks. The user then enters the coordinates of a cell. The program should display the grid
# with the character at those coordinates now displayed. The user then enters coordinates of
# another cell. The program should now display the grid with the previous character and the
# new character displayed. If the two characters match, then they should permanently replace
# the asterisks in those locations. Otherwise, when the user enters the next set of coordinates,
# those characters should be replaced by asterisks. The game continues this way until the player
# matches everything or runs out of turns. You can decide how many turns they player gets

import random

# Set up the board
board = []
for i in range(5):
    row = ['*'] * 5
    board.append(row)

# Populate the board with random characters
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
random.shuffle(characters)
for i in range(5):
    for j in range(5):
        board[i][j] = characters.pop()

# Set up the game parameters
turns = 10
matched = set()

# Define a function to print the board
def print_board():
    for i in range(5):
        for j in range(5):
            if (i, j) in matched:
                print(board[i][j], end=' ')
            else:
                print('*', end=' ')
        print()

# Play the game
while turns > 0 and len(matched) < 10:
    print(f'Turns left: {turns}')
    print_board()
    try:
        x1 = int(input('Enter x coordinate of first cell: '))
        y1 = int(input('Enter y coordinate of first cell: '))
        x2 = int(input('Enter x coordinate of second cell: '))
        y2 = int(input('Enter y coordinate of second cell: '))
        if board[x1][y1] == board[x2][y2]:
            matched.add((x1, y1))
            matched.add((x2, y2))
            print('Match found!')
        else:
            print('No match found')
            board[x1][y1] = '*'
            board[x2][y2] = '*'
    except (ValueError, IndexError):
        print('Invalid coordinates. Try again.')
    turns -= 1

# Print the final board
print_board()

# Determine the outcome of the game
if len(matched) == 10:
    print('Congratulations! You matched everything!')
else:
    print('Game over. You ran out of turns.')
