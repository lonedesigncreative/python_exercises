# Ask the user for a letter
letter = input("Enter the letter S, M or W: ").upper()

# Match the letter with the marital status
match letter:
    case "S":
        print("Single")
    case "M":
        print("Married")
    case "W":
        print("Widowed")
    case _:
        print("Invalid marital status!")