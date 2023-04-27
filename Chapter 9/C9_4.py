# Write a program that asks the user to enter a password. If the user enters the right password,
#the program should tell them they are logged in to the system. Otherwise, the program
#should ask them to reenter the password. The user should only get five tries to enter the
#password, after which point the program should tell them that they are kicked off of the
#system.

correct_password = input("Create your password: ")
x = correct_password
attempts = 5

while attempts > 0:
    password = input("Enter password: ")
    if password == x:
        print("You are logged in to the system.")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("You are kicked off of the system.")
        else:
            print("Incorrect password. You have", attempts, "attempts left.")







