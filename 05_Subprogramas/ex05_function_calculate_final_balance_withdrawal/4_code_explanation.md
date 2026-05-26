> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `def Calculate_Balance(balance, withdraw):`
> - Defines a function named `Calculate_Balance` that takes two parameters: `balance` (the current account balance) and `withdraw` (the amount the user wants to withdraw).
> 
> 2. `if balance < withdraw:`
> - Checks whether the withdrawal amount is greater than the current balance. If this condition is true, the code inside this `if` block will run.
> 
> 3. `print("You cannot withdraw an amount greater than your balance")` 
> - Displays a message informing the user that they cannot withdraw more money than the available balance.
> 
> 4. `else:` 
> - Defines the alternative path that will run when the condition in the if statement is false (i.e., when the balance is sufficient).
>
> 5. `final_balance = balance - withdraw` 
> - Calculates the new balance by subtracting the withdrawal amount from the current balance and stores the result in the variable `final_balance`.
>
> 6. `print(f"Balance after withdrawal: {final_balance}")` 
> - Prints a message showing the balance remaining after the withdrawal, using an f-string to include the value of final_balance.
>
> 7. `Calculate_Balance(1200, 1500)` 
> - Calls the `Calculate_Balance` function with a balance of 1200 and a withdrawal amount of 1500, triggering the insufficient balance message.
>
> 8. `Calculate_Balance(2000, 1700)` 
> - Calls the `Calculate_Balance` function again, this time with a balance of 2000 and a withdrawal amount of 1700, so it calculates and prints the final balance.