#Use the following two lists and the format method to create a list of card names in the format
#card value of suit name (for example, 'Two of Clubs').

import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']


card_names = random.choice(values)
card_names2 = random.choice(suits)
print(card_names + "", "of" + "", card_names2)