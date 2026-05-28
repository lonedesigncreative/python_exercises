> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `a = int(input("Enter the first number: "))`
> - Reads an integer from the user and stores it in `a`.
>
> 2. `b = int(input("Enter the second number: "))`
> - Reads another integer and stores it in `b`.
>
> 3. `if a > b:`
> - Checks if `a` is greater than `b`.
>
> 4. `a, b = b, a`
> - If so, swaps the values of `a` and `b` so that `a` becomes the smaller number.
>
> 5. `for i in range(a, b + 1):`
> - Starts a loop with `i` from `a` to `b` (inclusive).
>
> 6. `print(i)`
> - Prints each value of `i` in the interval.