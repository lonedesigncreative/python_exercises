# Program that checks whether an integer is even or odd

number = int(input("Enter an integer number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


"""
EXPLANATION:

# Program that checks whether an integer is even or odd

number = int(input("Enter an integer number: ")) # Get input from the user for an integer number, which will be used to determine whether it is even or odd based on the remainder when divided by 2

if number % 2 == 0: # Check if the number is even by using the modulus operator (%) to find the remainder when the number is divided by 2. If the remainder is 0, it means the number is even, and the program will execute the code block that prints "The number is even."
    print("The number is even.")
else: # If the number is not even (i.e., the remainder when divided by 2 is not 0), then it must be odd, and the program will execute the code block that prints "The number is odd."
    print("The number is odd.")

"""