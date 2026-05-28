> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `N = int(input("Enter the value of N: "))`
> - Reads a value from the user, converts it to an integer, and stores it in `N`.
>
> 2. `total = 0`
> - Initializes total to `0` to accumulate the sum.
>
> 3. `for i in range(1, N + 1):`
> - Starts a loop with i going from 1 to N (inclusive).
>
> 4. `total += i`
> - Adds the current `i` to `total`.
>
> 5. `print(f"The sum of the first {N} natural numbers is {total}")`
> - Prints a message showing N and the computed sum `total`.