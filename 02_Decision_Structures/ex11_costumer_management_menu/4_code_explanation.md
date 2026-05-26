> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `print("***** Customer List *****") `
> - Display the customer management menu options to the user
> 
> 2. `print("1 – Add Customer")`  
> - Option 1 allows the user to add a new customer to the system
> 
> 3. `print("2 – Edit Customer")` 
> - Option 2 allows the user to edit the details of an existing customer in the system
> 
> 4. `print("3 – Delete Customer")` 
> - Option 3 allows the user to delete a customer from the system
> 
> 5. `print("4 – Exit Program")` 
> - Option 4 allows the user to exit the customer management program
> 
> 6. `option = int(input("Enter your option: "))` 
> - Get the user's choice for the menu option they want to select
>
> 7. `match option:` 
> - Decision structure using match/case to determine which menu option the user selected and execute the corresponding code block
>
> 8. `case 1:` 
> - If the user selects option 1, the program will execute the code block that adds a customer to the system
> 
> 9. `print("You selected option 1")` 
> - Provide feedback to the user that they have selected the option to add a customer, which could lead to further prompts for customer details in a more complete implementation of the program.
>
> 10. `case 2:` 
> - If the user selects option 2, the program will execute the code block that edits a customer in the system
> 
> 11. `print("You selected option 2")` 
> - Provide feedback to the user that they have selected the option to edit a customer, which could lead to further prompts for selecting a customer and editing their details in a more complete implementation of the program.
>
> 12. `case 3:` 
> - If the user selects option 3, the program will execute the code block that deletes a customer from the system 
> 
> 13. `print("You selected option 3")` 
> - Provide feedback to the user that they have selected the option to delete a customer, which could lead to further prompts for selecting a customer to delete in a more complete implementation of the program.
>
> 14. `case 4:` 
> - If the user selects option 4, the program will execute the code block that exits the program
> 
> 15. `print("You selected option 4")` 
> - Provide feedback to the user that they have selected the option to exit the program, which could lead to the termination of the program in a more complete implementation.
>
> 16. `case _:` 
> - If the user selects an option that is not 1, 2, 3, or 4, the program will execute the default case and print an error message indicating that the option is invalid
> 
> 17. `print("Invalid option.")` 
> - Provide feedback to the user that they have entered an invalid option, prompting them to enter a valid option from the menu. This helps ensure that the program can handle unexpected input gracefully.