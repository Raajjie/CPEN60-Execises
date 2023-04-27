# Ask the user to enter the numerator and denominator of a fraction, and the digit they want to
# know. For instance, if the user enters a numerator of 1 and a denominator of 7 and wants to
# know the 4th digit, your program should print out 8, because 1
# 7 = .142856... and 8 is the 4th
# digit. One way to do this is to mimic the long division process you may have learned in grade
# school. It can be done in about five lines using the // operator at one point in the program.

numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))
position = int(input("Enter position of digit to find: "))

quotient = numerator // denominator
remainder = numerator % denominator

for i in range(position):
    remainder *= 10
    digit = remainder // denominator
    remainder %= denominator

print(digit)