# Program that converts a numeric grade (1–3) into a textual description using match/case

grade = int(input("Enter a grade: "))

match grade:
    case 1:
        print("Poor")
    case 2:
        print("Average")
    case 3:
        print("Good")
    case _:
        print("Invalid grade. Please enter a grade between 1 and 3.")