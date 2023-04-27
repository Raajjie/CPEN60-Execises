# Write a program that asks the user to enter a fraction in the form of a string like '1/2' or
# '8/24'. The program should reduce the fraction to lowest terms and print out the result.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


fraction = input("Enter a fraction like '1/2' or '8/24': ")

numerator, denominator = fraction.split("/")
numerator = int(numerator)
denominator = int(denominator)

gcd_val = gcd(numerator, denominator)
reduced_numerator = numerator // gcd_val
reduced_denominator = denominator // gcd_val

print(f"The fraction {fraction} reduces to {reduced_numerator}/{reduced_denominator}.")
