#10. Write a multiplication game program for kids. The program should give the player ten randomly generated multiplication questions to do. After each, the program should tell them whether they got it right or wrong and what the correct answer is

from random import randint

ques = 0

for i in range (10):
    num1=randint (1,20)
    num2=randint (1,20)
    num3= num1*num2

    ques += 1

    print("QUESTION",ques,':', num1,'x',num2,)

    ans = int(input("ANSWER:"))
    if ans == num3:
        print("Right!")
    else:
        print("Wrong. The answer is", num3)
