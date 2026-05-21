# Program that calculates the area of a right triangle

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculation of the result
area = (base * height) / 2

print(f"The area of the right triangle is: {area}")

"""

EXPLANATION:

# Program that calculates the area of a right triangle

base = float(input("Enter the base of the triangle: ")) # Get input from the user for the base of the triangle, which will be stored in the variable base. The input function prompts the user to enter a value, and the float function converts that input into a decimal number (floating-point number) data type, allowing for more precise measurements of the triangle's base.
height = float(input("Enter the height of the triangle: ")) # Get input from the user for the height of the triangle, which will be stored in the variable height. Similar to base, the input function prompts the user to enter a value, and the float function converts that input into a decimal number (floating-point number) data type, allowing for more precise measurements of the triangle's height.

# Calculation of the result
area = (base * height) / 2 # Calculate the area of the right triangle using the formula (base * height) / 2. This formula is derived from the fact that the area of a triangle is equal to half the product of its base and height. The result is stored in the variable area.

print(f"The area of the right triangle is: {area}")

"""
