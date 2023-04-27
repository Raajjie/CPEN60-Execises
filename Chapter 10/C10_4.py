#Write a program that takes a list of ten prices and ten products, applies an 11% discount to
#each of the prices displays the output like below, right-justified and nicely formatted.
#Apples $ 2.45
#Oranges $ 18.02
#...
#Pears $120.03

prices = [2.45, 18.02, 5.99, 12.50, 23.99, 7.25, 35.75, 9.99, 49.99, 120.03]
products = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Bottled Milk', 'Piattos', 'Toblerone', 'Oreo', 'Cheese', 'Pears']

discounted_prices = [price * 0.89 for price in prices]

for i in range(len(products)):
    print(f"{products[i]:<12}    $ {discounted_prices[i]:>7.2f}")
