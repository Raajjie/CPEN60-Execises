#  Use a for loop to print an upside down triangle like the one below. Allow the user to specify
# how high the triangle should be

height = int(input("Enter height of triangle: "))

for i in range(height, 0, -1):
    print('*' * i)