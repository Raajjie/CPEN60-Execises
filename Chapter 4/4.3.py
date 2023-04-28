#3. Ask the user to enter a temperature in Celsius. The program should print a message based on the temperature:
#• If the temperature is less than -273.15, print that the temperature is invalid because it is below absolute zero.
#• If it is exactly -273.15, print that the temperature is absolute 0.
#• If the temperature is between -273.15 and 0, print that the temperature is below freezing.
#• If it is 0, print that the temperature is at the freezing point.
#• If it is between 0 and 100, print that the temperature is in the normal range.
#• If it is 100, print that the temperature is at the boiling point.
#• If it is above 100, print that the temperature is above the boiling point

celsius = float(input("Enter the temperature in Celsius: "))

# Check for special cases first
if celsius < -273.15:
    print("The temperature is invalid because it is below absolute zero.")
elif celsius == -273.15:
    print("The temperature is absolute 0.")
elif celsius < 0:
    print("The temperature is below freezing.")
elif celsius == 0:
    print("The temperature is at the freezing point.")
elif celsius < 100:
    print("The temperature is in the normal range.")
elif celsius == 100:
    print("The temperature is at the boiling point.")
else:
    print("The temperature is above the boiling point.")

