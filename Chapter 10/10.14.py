#14. write a program to find the smallest positive integer that satisfies the following property: If you take the leftmost digit and move it all the way to the right, the number thus obtained is exactly 3.5 times larger than the original number. For instance, if we start with 2958 and move the 2 all the way to the right, we get 9582, which is roughly 3.2 times the original number
def find_number():
    num = 1
    while True:
        str_num = str(num)
        left_digit = str_num[0]
        new_num = int(str_num[1:] + left_digit)
        if new_num == 3.5 * num:
            return num
        num += 1

result = find_number()
print("The smallest positive integer that satisfies the given property is:",result)


print("When the first digit is put to the right, it becomes", result*3.5 ,"which is exactly 3.5 larger than the original number.")
