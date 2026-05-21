# Program that asks the user for 3 decimal grades and displays the average

grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))

average = (grade1 + grade2 + grade3) / 3

print(f"The average of the three grades is: {average}")

"""

EXPLANATION:

# Program that asks the user for 3 decimal grades and displays the average

grade1 = float(input("Enter the first grade: ")) # Get input from the user for the first grade, which will be stored in the variable grade1. The input function prompts the user to enter a value, and the float function converts that input into a decimal number (floating-point number) data type.
grade2 = float(input("Enter the second grade: ")) # Get input from the user for the second grade, which will be stored in the variable grade2. Similar to grade1, the input function prompts the user to enter a value, and the float function converts that input into a decimal number (floating-point number) data type.
grade3 = float(input("Enter the third grade: ")) # Get input from the user for the third grade, which will be stored in the variable grade3. Again, the input function prompts the user to enter a value, and the float function converts that input into a decimal number (floating-point number) data type.

average = (grade1 + grade2 + grade3) / 3 # Calculate the average by adding grade1, grade2, and grade3 together and then dividing the sum by 3 (the number of grades). The result is stored in the variable average.

print(f"The average of the three grades is: {average}")

"""