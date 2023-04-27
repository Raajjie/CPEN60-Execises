# The currency of a strange country has coins worth 7 cents and 11 cents. Write a program to
# determine the largest purchase price that cannot be paid using these two coins.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


coin1 = 7
coin2 = 11

gcd_val = gcd(coin1, coin2)

max_purchase_price = coin1 * coin2 - coin1 - coin2 + gcd_val

print(f"The largest purchase price that cannot be paid using {coin1}-cent and {coin2}-cent coins is {max_purchase_price} cents.")
