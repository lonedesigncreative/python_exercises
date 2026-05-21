# Program that checks if a number is greater than or equal to 5

number = float(input("Enter a number: "))

if number >= 5:
    print("The number is greater than or equal to 5.")
else:
    print("The number is below 5.")

print("End of program.")


"""
EXPLANATION:

# Program that checks if a number is greater than or equal to 5 # This program prompts the user to enter a number and then checks if that number is greater than or equal to 5. It uses a simple if-else decision structure to determine the appropriate message to display based on the user's input.

number = float(input("Enter a number: ")) # Get input from the user for a number, which will be used to check if it is greater than or equal to 5. The input is converted to a floating-point number to allow for decimal values, and it represents the value that the user wants to evaluate against the specified threshold (greater than or equal to 5).

if number >= 5: # Check if the number entered by the user is greater than or equal to 5 using the greater than or equal to operator (>=). If this condition is true, it means that the number is either 5 or any value greater than 5, and the program will execute the code block that prints "The number is greater than or equal to 5." If this condition is false (i.e., the number is less than 5), the program will execute the code block in the else statement, which will print "The number is below 5."
    print("The number is greater than or equal to 5.") # Print a message to the user indicating that the number they entered is greater than or equal to 5, confirming that it meets the specified condition. This message will only be displayed if the condition in the if statement is met (i.e., number >= 5).
else: # If the number entered by the user does not satisfy the condition of being greater than or equal to 5, the program will execute this code block, which prints a message to the user indicating that the number is below 5. This message serves as feedback to inform the user that their input does not meet the criteria specified in the if statement.
    print("The number is below 5.")

print("End of program.")

"""