#11. Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm, and asks them how many hours into the future they want to go. Print out what the hour will be that many hours into the future, printing am or pm as appropriate

hour = int(input("Enter hour:"))
mer = input("Enter am or pm:")
hif = int(input("Enter the number of hours into the future:"))

if mer == "pm":
    hour+= 12
hour += hif
hour %= 24

if hour == 0:
    print("12", end="")
else:
    print(str(hour%12), end="")
print(""+("am" if hour < 12 else "pm"))
