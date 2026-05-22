> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `value1 = float(input("Enter the first number: "))`
> - Get the first number from the user, which can be a floating-point number to allow for decimal values
> 
> 2. `value2 = float(input("Enter the second number: "))`
> - Get the second number from the user, which can also be a floating-point number to allow for decimal values
>
> 3. `operator = input("Enter the operation (+, -, *, /): ")`
> - Get the second number from the user, which can also be a floating-point number to allow for decimal values
> 
> 4. `match operator:`  
> - The match/case structure is used to determine which arithmetic operation to perform based on the operator entered by the user
> 
> 5. `case "+":` 
> - If the operator is "+", the program will execute the code block that performs addition and prints the result
> 
> 6. `print(f"Result of the addition: {value1 + value2}")` 
> - Perform addition and display the result if the user chose the "+" operator, providing feedback on the operation performed and the outcome.
> 
> 7. `case "-":` 
> - If the operator is "-", the program will execute the code block that performs subtraction and prints the result
> 
> 8. `print(f"Result of the subtraction: {value1 - value2}")` 
> - Perform subtraction and display the result if the user chose the "-" operator, providing feedback on the operation performed and the outcome.
>
> 9. `case "*":` 
> - If the operator is "*", the program will execute the code block that performs multiplication and prints the result
>
> 10. `print(f"Result of the multiplication: {value1 * value2}")` 
> - Perform multiplication and display the result if the user chose the "*" operator, providing feedback on the operation performed and the outcome.
>
> 11. `case "/":` 
> - If the operator is "/", the program will execute the code block that performs division and prints the result. It is important to note that if value2 is zero, this will raise a ZeroDivisionError, so in a more robust implementation, you might want to add error handling for that case.
> 
> 12. `print(f"Result of the division: {value1 / value2}"):` 
> - Perform division and display the result if the user chose the "/" operator, providing feedback on the operation performed and the outcome. Note that this does not handle division by zero, which could be an improvement to consider.
>
> 13. `case _:` 
> - If the operator entered by the user does not match any of the cases (+, -, *, /), the program will execute the default case and print "Invalid operator." indicating that the input is not a valid operator for the arithmetic operations supported by the program
> 
> 14. `print("Invalid operator.")` 
> - Provide feedback to the user if they entered an operator that is not recognized, ensuring that the program handles invalid input gracefully and informs the user of the issue.