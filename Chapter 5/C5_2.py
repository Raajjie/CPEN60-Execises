#Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
#4 and how many end in a 9.

count = 0
count_2 = 0

for i in range(1,101):
    if (i**2) % 10 == 4:
        count = count + 1
    if (i**2) % 10 == 9:
        count_2 = count_2 + 1
print(count)
print(count_2)