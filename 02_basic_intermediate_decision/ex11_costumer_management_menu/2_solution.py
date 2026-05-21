# Customer Management Menu using match/case

print("***** Customer List *****")
print("1 – Add Customer")
print("2 – Edit Customer")
print("3 – Delete Customer")
print("4 – Exit Program")

option = int(input("Enter your option: "))

match option:
    case 1:
        print("You selected option 1")
    case 2:
        print("You selected option 2")
    case 3:
        print("You selected option 3")
    case 4:
        print("You selected option 4")
    case _:
        print("Invalid option.")

"""
EXPLANATION:

# Customer Management Menu using match/case

print("***** Customer List *****") # Display the customer management menu options to the user
print("1 – Add Customer") # Option 1 allows the user to add a new customer to the system
print("2 – Edit Customer") # Option 2 allows the user to edit the details of an existing customer in the system
print("3 – Delete Customer") # Option 3 allows the user to delete a customer from the system
print("4 – Exit Program") # Option 4 allows the user to exit the customer management program

option = int(input("Enter your option: ")) # Get the user's choice for the menu option they want to select

match option: # Decision structure using match/case to determine which menu option the user selected and execute the corresponding code block
    case 1: # If the user selects option 1, the program will execute the code block that adds a customer to the system
        print("You selected option 1")
    case 2: # If the user selects option 2, the program will execute the code block that edits a customer in the system
        print("You selected option 2")
    case 3: # If the user selects option 3, the program will execute the code block that deletes a customer from the system 
        print("You selected option 3")
    case 4: # If the user selects option 4, the program will execute the code block that exits the program
        print("You selected option 4")
    case _: # If the user selects an option that is not 1, 2, 3, or 4, the program will execute the default case and print an error message indicating that the option is invalid
        print("Invalid option.")

"""