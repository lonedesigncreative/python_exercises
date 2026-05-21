# Program that identifies the largest of three integers

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Compare the three values
if num1 >= num2 and num1 >= num3:
    print("Number 1 is the largest.")
elif num2 >= num1 and num2 >= num3:
    print("Number 2 is the largest.")
else:
    print("Number 3 is the largest.")

print("Number 3 is the largest.")


"""
EXPLANATION:

# Program that identifies the largest of three integers

num1 = int(input("Enter the first integer: ")) # Get input from the user for the first integer, which will be used to compare with the other two integers to determine which one is the largest
num2 = int(input("Enter the second integer: ")) # Get input from the user for the second integer, which will be used to compare with the first and third integers to determine which one is the largest
num3 = int(input("Enter the third integer: ")) # Get input from the user for the third integer, which will be used to compare with the first and second integers to determine which one is the largest

# Compare the three values
if num1 >= num2 and num1 >= num3: # If num1 is greater than or equal to both num2 and num3, then num1 is the largest number among the three integers entered by the user, and the program will execute the code block that prints "Number 1 is the largest."    
    print("Number 1 is the largest.")
elif num2 >= num1 and num2 >= num3: # If num2 is greater than or equal to both num1 and num3, then num2 is the largest number among the three integers entered by the user, and the program will execute the code block that prints "Number 2 is the largest."
    print("Number 2 is the largest.")
else: # If neither num1 nor num2 is the largest, then num3 must be the largest number among the three integers entered by the user, and the program will execute the code block that prints "Number 3 is the largest."
    print("Number 3 is the largest.")

print("Number 3 is the largest.")

"""