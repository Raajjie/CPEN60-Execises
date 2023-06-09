#20. Write a program that asks the user to enter a date in the format mm/dd/yy and converts it to a more verbose format. For example, 02/04/77 should get converted into February 4, 1977.

def convert_date(date):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    mm, dd, yy = date.split("/")
    month = months[int(mm)-1]
    year = "20" + yy if int(yy) <= 23 else "19" + yy
    return f"{month} {dd}, {year}"

date = input("Enter a date in the format mm/dd/yy: ")
verbose_date = convert_date(date)
print(verbose_date)
