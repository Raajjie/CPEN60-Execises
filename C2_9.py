#The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
#number thereafter is the sum of the two preceding numbers. Write a program that asks the
#user how many Fibonacci numbers to print and then prints that many

n = int(input("How many Fibonacci numbers do you want to print? "))
a, b = 1, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b