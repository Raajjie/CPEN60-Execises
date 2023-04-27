#(a) Write a program that uses a while loop (not a for loop) to read through a string and print
#the characters of the string one-by-one on separate lines.
#(b) Modify the program above to print out every second character of the string.

s = input("Enter a word: ")
n = len(s)
i = 0

#A
while i < n:
    print(s[i])
    i += 1

#B
s = input("Enter a word: ")
n = len(s)
i = 0

while i < n:
    print(s[i])
    i += 2