#15. Write a program to determine how many zeroes 1000! ends with.
def count_zeroes(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

num_zeroes = count_zeroes(1000)
print(num_zeroes)
