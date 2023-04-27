# Write a program that repeatedly asks the user to enter a height in the format feet’inches" (like
# 5'11" or 6'3". The user indicates they are done entering heights by entering done. The
# program should return a count of how many 4-footers, 5-footers, 6-footers, and 7-footers
# were entered.

four_footers = 0
five_footers = 0
six_footers = 0
seven_footers = 0

while True:
    height = input("Enter a height in feet'inches\" (e.g. 5'11\") or enter 'done' to finish: ")
    if height == "done":
        break


    feet, inches = height.split("'")
    feet = int(feet)
    inches = int(inches[:-1])

    if feet == 4:
        four_footers += 1
    elif feet == 5:
        five_footers += 1
    elif feet == 6:
        six_footers += 1
    elif feet == 7:
        seven_footers += 1

print(f"Number of 4-footers: {four_footers}")
print(f"Number of 5-footers: {five_footers}")
print(f"Number of 6-footers: {six_footers}")
print(f"Number of 7-footers: {seven_footers}")
