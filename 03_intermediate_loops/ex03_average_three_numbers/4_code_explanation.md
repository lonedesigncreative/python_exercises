> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `sum = 0`
> - Initialize the sum variable, which will be used to accumulate the total of the three numbers entered by the user
> 
> 2. `for value in range(1, 4):`  
> - From 1 to 3 inclusive
>
> 3. `number = float(input(f"Enter number {value}: "))` 
> - Get input from the user
> 
> 3. `sum = sum + number` 
> - Add the number to the sum
>
> 4. `average = sum / 3` 
> - Calculate the average and print the result
>
> 5. `print(f"The average of the three numbers is: {round(average, 2)}")` 
> - Print the average rounded to 2 decimal places for better readability