# Import the module for generating random numbers
import random as rd

generated_number = rd.randint(1, 10)

# Declare variable
number = 0

while number != generated_number:
    number = int(input("Enter a number: "))
    
    if number != generated_number:
        print("Try again!")

print(f"You guessed the number! It was: {generated_number}")