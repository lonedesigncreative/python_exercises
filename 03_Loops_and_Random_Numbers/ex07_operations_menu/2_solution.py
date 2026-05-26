# Repetition structure to keep showing the menu
while True:
    # Build the menu
    print("***** Customer List *****")
    print("1 - Insert Customer")
    print("2 - Update Customer")
    print("3 - Remove Customer")
    print("4 - List Customers")
    print("5 - Exit Program")

    # Ask the user for an option
    option = int(input("Enter an option: "))

    # Selective decision structure
    match option:
        case 1: print("You selected option 1")
        case 2: print("You selected option 2")
        case 3: print("You selected option 3")
        case 4: print("You selected option 4")
        case 5: break

        case _: print("Invalid option")
