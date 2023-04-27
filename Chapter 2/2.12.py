# Use a for loop to print a triangle like the one below. Allow the user to specify how high the
# triangle should be.


height = int(input("Enter height of triangle: "))

for i in range(1, height+1):
    print('*' * i)
    