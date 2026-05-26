# Variable to accumulate the sum of the numbers
total = 0
number = -1  

# Repeat while the user does not enter 0
while number != 0:
    number = int(input("Enter a number (0 to stop): "))

    total = total + number

print(f"Final sum: {total}")