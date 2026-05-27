> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `operation = input("Choose the operation (+, -, *, /): ")`
> - Reads the operation symbol typed by the user and stores it as text in `operation`.
> 
> 2. `n1 = float(input("Enter the first value: "))`  
> - Reads the first numeric value, converts it to a floating‑point number, and stores it in `n1`.
> 
> 3. `n2 = float(input("Enter the second value: "))` 
> - Reads the second numeric value, converts it to a floating‑point number, and stores it in `n2`.
> 
> 4. `if operation == "+":` 
> - Checks if the user chose the addition operation.
>
> 5. `result = n1 + n2`
> - Adds `n1` and `n2` and stores the sum in `result`.
> 
> 6. `print(f"Result: {result}")`  
> - Prints the result of the addition.
> 
> 7. `elif operation == "-":` 
> - Checks if the user chose the subtraction operation.
> 
> 8. `print(f"Result: {result}")` 
> - Prints the result of the subtraction.
>
> 7. `elif operation == "*":`
> - Checks if the user chose the multiplication operation.
> 
> 8. `result = n1 * n2`  
> - Multiplies `n1` by `n2` and stores the product in `result`.
> 
> 9. `print(f"Result: {result}")` 
> - Prints the result of the multiplication.
> 
> 10. `elif operation == "/":` 
> - Checks if the user chose the division operation.
>
> 11. ` if n2 == 0:` 
> - Checks if the second value is zero, to avoid division by zero.
>
> 12. `print("Error: division by zero is not allowed!")`
> - Prints an error message if the user tried to divide by zero.
> 
> 13. `else:`
>  `result = n1 / n2`
> - If `n2` is not zero, divides `n1` by `n2` and stores the quotient in `result`.
> 
> 14. `print(f"Result: {result}")` 
> - Prints the result of the division.
>
> 15. `else:`
> - Runs if the user did not choose any of the valid operation symbols.
> 
> 16. `print("Invalid operation.")` 
> - Prints a message indicating that the chosen operation is invalid.