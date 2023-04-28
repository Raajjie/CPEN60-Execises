#. Pascal’s triangle is shown below. On the outside are 1’s and each other number is the sum of the two numbers directly above it. Write a program to generate Pascal’s triangle. Allow the user to specify the number of rows. Be sure that it is nicely formatted, like below.

# Get user input for number of rows
num_rows = int(input("Enter the number of rows: "))

# Initialize the first two rows of the triangle
triangle = [[1], [1, 1]]

# Generate the remaining rows of the triangle
for i in range(2, num_rows):
    # Initialize a new row with the first element set to 1
    row = [1]
    # Compute the middle elements of the row as the sum of the two elements above them
    for j in range(1, i):
        row.append(triangle[i-1][j-1] + triangle[i-1][j])
    # Append a final element of 1 to the row
    row.append(1)
    # Append the row to the triangle
    triangle.append(row)

# Print the triangle
for row in triangle:
    print(' '.join(str(x) for x in row).center(num_rows*6))
