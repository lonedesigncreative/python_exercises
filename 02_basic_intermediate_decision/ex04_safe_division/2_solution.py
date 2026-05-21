# Program that divides two numbers safely

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 > 0:
    result = num1 / num2
    print(f"The result of the division is: {result}")
else:
    print("You cannot divide by a value that is less than or equal to 0.")


"""
EXPLANATION:

# Program that divides two numbers safely

num1 = float(input("Enter the first number: ")) # Get input from the user for the first number, which will be used as the numerator in the division operation. The input is converted to a floating-point number to allow for decimal values, and it represents the dividend in the division process.
num2 = float(input("Enter the second number: ")) # Get input from the user for the second number, which will be used as the denominator in the division operation. The input is converted to a floating-point number to allow for decimal values, and it represents the divisor in the division process. It is important to ensure that this number is not zero or negative to avoid invalid division operations.

if num2 > 0: # Check if the second number (denominator) is greater than 0 to ensure that we do not attempt to divide by zero or a negative number, which would be invalid for division. If this condition is true, the program will execute the code block that performs the division and prints the result.
    result = num1 / num2 # Perform the division operation by dividing num1 (the numerator) by num2 (the denominator) and store the result in the variable 'result'. This calculation will yield the quotient of the two numbers, and it is safe to perform because we have already checked that num2 is greater than 0.
    print(f"The result of the division is: {result}") # Print the result of the division operation to the user. The output will display the quotient of num1 and num2, and it is formatted as a string to provide a clear message indicating that this is the result of the division. If num2 is not greater than 0, the program will execute the code block in the else statement, which will print a message indicating that division by zero or a negative number is not allowed.
else: # If the second number (denominator) is not greater than 0 (i.e., it is zero or negative), the program will execute this code block, which prints a message to the user indicating that division by zero or a negative number is not allowed. This is important for preventing runtime errors and ensuring that the program behaves predictably when given invalid input for the denominator.
    print("You cannot divide by a value that is less than or equal to 0.")

"""