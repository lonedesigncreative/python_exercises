# Program that asks the user for 3 decimal grades and displays the average

grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))

average = (grade1 + grade2 + grade3) / 3

print(f"The average of the three grades is: {average}")