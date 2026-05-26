> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `try`
> - Starts a try block, where the program places the instructions that may generate errors during execution.
> 
> 2. `num1 = int(input("Enter number 1: "))`
> - Asks the user to enter the first number. The value received as text is converted to an integer and stored in the variable `num1`.
> 
> 3. `num2 = int(input("Enter number 2: "))` 
> - Asks the user to enter the second number, converts the input to an integer, and stores it in the variable `num2`.
> 
> 4. `division = num1 / num2` 
> - Calculates the division of the first number by the second and stores the result in the variable `division`.
>
> 5. `print(f"Division: {division}")` 
> - Displays the text `"Division: "` followed by the value stored in `division`, using an f-string.
>
> 6. `except ZeroDivisionError as error1:`
> - Catches the specific error that occurs when the program attempts to divide by zero. The error is stored in the variable `error1`.
> 
> 7. `print("Division Error: It is not possible to divide by zero.")`
> - Prints a message informing the user that division by zero is not allowed.
> 
> 8. `except ValueError as error2:` 
> - Catches the error that occurs when the conversion to integer fails, such as when the user enters letters instead of numbers. The error is stored in `error2`.
> 
> 9. `print("Value Error: You must enter only integer numbers.")` 
> - Displays a message informing the user that only integer values are accepted.
>
> 10. `except Exception as error:` 
> - Catches any other type of error not handled by the previous except blocks. The error is stored in the variable `error`.
>
> 11. `print(f"An unexpected error occurred: {error}")` 
> - Prints a generic message indicating that an unexpected error occurred and shows the error description.
>
> 12. `finally:` 
> - Starts the finally block, which always runs whether an error occurred or not.
>
> 13. `print("Operation finished")` 
> - Displays the message `"Operation finished"`, indicating that the program has completed its execution.