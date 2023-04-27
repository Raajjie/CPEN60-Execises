#Write a program that asks the user to enter a word. Rearrange all the letters of the word
#in alphabetical order and print out the resulting word. For example, abracadabra should
#become aaaaabbcdrr

enter_word = input("Enter a Word: ")
sorted_word = ''.join(sorted(enter_word))
print("Sorted word:", sorted_word)