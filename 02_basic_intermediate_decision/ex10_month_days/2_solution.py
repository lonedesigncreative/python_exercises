# Program that identifies the number of days in a month using match/case

month = int(input("Enter a month number (1 to 12): "))

# Decision structure using match/case
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("This month has 31 days.") 
    case 4 | 6 | 9 | 11:
        print("This month has 30 days.")
    case 2:
        print("February has 28 or 29 days.")
    case _:
        print("Invalid month.")

"""

EXPLANATION:

# Program that identifies the number of days in a month using match/case

month = int(input("Enter a month number (1 to 12): ")) # Get input from the user for the month number, which should be an integer between 1 and 12 representing the months of the year (January to December)

# Decision structure using match/case
match month: # The match/case structure is used to determine the number of days in the month based on the month number entered by the user
    case 1 | 3 | 5 | 7 | 8 | 10 | 12: # If the month number is 1, 3, 5, 7, 8, 10, or 12, the program will execute the code block that prints "This month has 31 days." because these months have 31 days in the calendar
        print("This month has 31 days.") 
    case 4 | 6 | 9 | 11: # If the month number is 4, 6, 9, or 11, the program will execute the code block that prints "This month has 30 days." because these months have 30 days in the calendar
        print("This month has 30 days.")
    case 2: # If the month number is 2, the program will execute the code block that prints "February has 28 or 29 days." because February can have either 28 or 29 days depending on whether it is a leap year or not
        print("February has 28 or 29 days.")
    case _: #" If the month number entered by the user does not match any of the cases (1 to 12), the program will execute the default case and print "Invalid month." indicating that the input is not a valid month number
        print("Invalid month.")

"""
