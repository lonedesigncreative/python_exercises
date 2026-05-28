> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `N = int(input("Enter a number to calculate the factorial: "))`
> - Reads an integer from the user and stores it in `N`.
>
> 2. `factorial = 1`
> - Initializes `factorial` to `1`.
>
> 3. `for i in range(1, N + 1):`
> - Starts a loop with `i` from `1` to `N`.
>
> 4. `factorial *= i`
> - Multiplies `factorial` by `i` and stores the result back in `factorial`.
>
> 5. `print(f"{N}! = {factorial}")`
> - Prints the factorial in the format “N! = value”.