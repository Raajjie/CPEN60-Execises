#Write a program that uses a boolean flag variable in determining whether two lists have any
#items in common.

list1 = [1, 2, 3, 4, 5]
list2 = ["a,b,c,d,e,f"]
common_items = False

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            common_items = True
            break

if common_items:
    print("The two lists have common items.")
else:
    print("The two lists do not have any common items.")
