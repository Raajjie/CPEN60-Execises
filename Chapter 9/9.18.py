#18. Randomly generate a 6 × 6 list that has exactly 12 ones placed in random locations in the list. The rest of the entries should be zeroes.

import random

lst = [[0]*6 for i in range(6)]

for i in range(12):
    while True:
        row = random.randint(0, 5)
        col = random.randint(0, 5)
        if lst[row][col] == 0:
            lst[row][col] = 1
            break

for row in lst:
    print(row)
