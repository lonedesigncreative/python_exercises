name = input("Please enter your name: ")

print(f"Welcome {name}!")

"""

EXPLANATION:

# Program that asks the user for their name and displays a welcome message

name = input("Please enter your name: ") # Get input from the user for their name, which will be stored in the variable name. The input function prompts the user to enter their name and waits for the user to type it in and press Enter. The value entered by the user will be treated as a string and assigned to the variable name.

print(f"Welcome {name}!") # Print a welcome message that includes the name entered by the user. The f-string (formatted string) allows us to embed the value of the variable name directly into the string, so if the user enters "Alice", the output will be "Welcome Alice!" This provides a personalized greeting to the user based on their input.

"""
