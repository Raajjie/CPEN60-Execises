#A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
#items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
#program that asks the user how many items they are buying and prints the total cost.
print("Our store currently has a promo")
print("We charges 12$ per item if you buy less than 10 items")
print("If you buy between 10 and 99 items, we charge only 10$ ")
print("And if you buy 100 or more items, the cost is only 7$ per item")

items = int(input("How many items do you want to buy? "))

if items < 10:
    print("Total cost is:",items*12,"$")

elif items == 10 and items <= 99:
    print("Total cost is :",items*10,"$")

elif items >= 100:
    print("Total cost is :",items*7,"$")