#2. Write a program to fill the screen horizontally and vertically with your name. [Hint: add the option end='' into the print function to fill the screen horizontally.]

import shutil

# Get name from user
name = input("Enter your name:")

columns, rows = shutil.get_terminal_size()

# Fill screen with name
for i in range(rows):
    for j in range(columns):
        print(name, end='')
    print()
