import math  # To use sqrt

# Ask the user for the catheti
a = float(input("Enter the value of cathetus a: "))
b = float(input("Enter the value of cathetus b: "))

# Calculate the hypotenuse
hypotenuse = math.sqrt(a ** 2 + b ** 2)

# Round to two decimal places
hypotenuse = round(hypotenuse, 2)

# Show the result
print(f"The hypotenuse of the triangle with catheti {a} and {b} is: {hypotenuse}")