# Program that converts a numeric grade (1–3) into a textual description using match/case

grade = int(input("Enter a grade: "))

match grade:
    case 1:
        print("Poor")
    case 2:
        print("Average")
    case 3:
        print("Good")
    # If the grade is not 1, 2, or 3, we can use a wildcard case to handle invalid input
    case _:
        print("Invalid grade. Please enter a grade between 1 and 3.")