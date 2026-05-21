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
