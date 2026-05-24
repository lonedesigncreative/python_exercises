> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `while True:`
> - This creates an infinite loop. The program will keep repeating the menu until a break statement stops the loop.
>
> 1. `  print("***** Customer List *****")`
> - Displays the title of the menu on the screen.
> 
> 2. `print("1 - Insert Customer")`
> `print("2 - Update Customer")`
> `print("3 - Remove Customer")`
> `print("4 - List Customers")`
> `print("5 - Exit Program")`
> - These lines print each menu option. The user will choose one of these numbers to perform an action.
>
> 3. ` option = int(input("Enter an option: "))` 
> - Shows a prompt asking the user to type a number. input() reads the user’s text. int() converts that text into an integer. The result is stored in the variable option.
> 
> 3. `match option:` 
> - Starts a match/case structure (Python’s modern version of switch‑case). It checks the value of option and executes the matching case.
>
> 4. `case 1: print("You selected option 1")`
> - If the user typed 1, this message is printed.
>
> 5. `case 2: print("You selected option 2")`
> - If the user typed 2, this message is printed.
> 6. `case 3: print("You selected option 3")`
> - If the user typed 3, this message is printed.
> 7. `case 4: print("You selected option 4")`
> - If the user typed 4, this message is printed.
> 8. `case 5: break`
> - If the user typed 5, the program executes break. break immediately exits the while loop, ending the menu and the program.
> 
> 9. `case 1: print("You selected option 1")`
> - If the user typed 1, this message is printed.
>
> 10. `case _: print("Invalid option")`
> - The underscore _ is the default case. It runs when the user enters any value that is not 1, 2, 3, 4, or 5. It prints an error message saying the option is invalid.