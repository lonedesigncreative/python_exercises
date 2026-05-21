# Program that performs an arithmetic operation chosen by the user using match/case

# Get input from the user
value1 = float(input("Enter the first number: "))
value2 = float(input("Enter the second number: "))
operator = input("Enter the operation (+, -, *, /): ")


match operator:
    case "+": 
        print(f"Result of the addition: {value1 + value2}")
    case "-":
        print(f"Result of the subtraction: {value1 - value2}")
    case "*":
        print(f"Result of the multiplication: {value1 * value2}")
    case "/":
        print(f"Result of the division: {value1 / value2}")
    case _:
        print("Invalid operator.")

"""
EXPLANATION:

# Program that performs an arithmetic operation chosen by the user using match/case

# Get input from the user
value1 = float(input("Enter the first number: ")) # Get the first number from the user, which can be a floating-point number to allow for decimal values
value2 = float(input("Enter the second number: ")) # Get the second number from the user, which can also be a floating-point number to allow for decimal values
operator = input("Enter the operation (+, -, *, /): ") # Get the operator from the user, which should be one of the following: + for addition, - for subtraction, * for multiplication, or / for division

# Decision structure using match/case
match operator: # The match/case structure is used to determine which arithmetic operation to perform based on the operator entered by the user
    case "+": # If the operator is "+", the program will execute the code block that performs addition and prints the result
        print(f"Result of the addition: {value1 + value2}")
    case "-": # If the operator is "-", the program will execute the code block that performs subtraction and prints the result
        print(f"Result of the subtraction: {value1 - value2}")
    case "*": # If the operator is "*", the program will execute the code block that performs multiplication and prints the result
        print(f"Result of the multiplication: {value1 * value2}")
    case "/": # If the operator is "/", the program will execute the code block that performs division and prints the result. It is important to note that if value2 is zero, this will raise a ZeroDivisionError, so in a more robust implementation, you might want to add error handling for that case.
        print(f"Result of the division: {value1 / value2}")
    case _: # If the operator entered by the user does not match any of the cases (+, -, *, /), the program will execute the default case and print "Invalid operator." indicating that the input is not a valid operator for the arithmetic operations supported by the program
        print("Invalid operator.")

"""

