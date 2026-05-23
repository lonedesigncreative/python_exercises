> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `total = 0`
> - A variable named total is created to store the sum of all numbers entered by the user. It begins at 0, since no values have been added yet.
>
> 1. `number = -1 `
> - The variable number is given an initial value that is not zero. This ensures that the while loop starts correctly.
> 
> 2. `while number != 0:`  
> - This condition means: “Continue repeating the instructions as long as the number is not 0.” When the user enters 0, the loop will stop.
>
> 3. `number = int(input("Enter a number (0 to stop): "))` 
> - The program asks the user to enter a number. If the user enters 0, the loop will end. If the user enters any other number, the loop continues.
> 
> 3. `total = total + number  ` 
> - The number provided by the user is added to the running total.This gradually builds the final sum.
>
> 4. `print(f"Final sum: {total}")` 
> - Once the user enters 0, the loop finishes and the program displays the final total.