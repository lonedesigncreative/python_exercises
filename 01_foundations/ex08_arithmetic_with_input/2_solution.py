# Program that performs arithmetic operations on two integers

# Declaration of 2 variables to store the user input
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
remainder = num1 % num2

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Remainder: {remainder}")

"""

EXPLANATION:

# Program that performs arithmetic operations on two integers

# Declaration of 2 variables to store the user input
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Perform arithmetic operations 
addition = num1 + num2 # Calculate the sum of num1 and num2 and store the result in the variable addition. This will perform the addition operation and give us the total of the two numbers.
subtraction = num1 - num2 # Calculate the difference between num1 and num2 and store the result in the variable subtraction. This will perform the subtraction operation and give us the result of num1 minus num2.
multiplication = num1 * num2 # Calculate the product of num1 and num2 and store the result in the variable multiplication. This will perform the multiplication operation and give us the result of num1 multiplied by num2.
division = num1 / num2 # Calculate the quotient of num1 divided by num2 and store the result in the variable division. This will perform the division operation and give us the result of num1 divided by num2. It is important to note that if num2 is zero, this will raise a ZeroDivisionError, so in a more robust implementation, you might want to add error handling for that case.
remainder = num1 % num2 # Calculate the remainder of num1 divided by num2 using the modulus operator (%) and store the result in the variable remainder. This will give us the value that is left over after dividing num1 by num2.

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Remainder: {remainder}")

"""