# Write a program that repeatedly asks the user to enter a birthday in the format month/day
# (like 12/25 or 2/14). The user indicates they are done entering birthdays by entering done.
# The program should return a count of how many of those birthdays are in February and how
# many are on the 25th of some month (any month).

feb_count = 0
feb_25_count = 0

while True:
    birthday = input("Enter birthday month/day: ")
    if birthday.lower() == "done":
        break

    month, day = birthday.split("/")
    if month == "2":
        feb_count += 1
    if day == "25":
        feb_25_count += 1

print(f"There are {feb_count} birthdays in February.")
print(f"There are {feb_25_count} birthdays on the 25th of some month.")