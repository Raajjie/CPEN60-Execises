numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))
position = int(input("Enter position of digit to find: "))

quotient = numerator // denominator
remainder = numerator % denominator

for i in range(position):
    remainder *= 10
    digit = remainder // denominator
    remainder %= denominator

print(digit)