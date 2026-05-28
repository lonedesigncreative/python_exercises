> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `total = 0`
> - Initializes the variable `total` with value `0` to accumulate the sum.
>
> 2. `for i in range(4):`
> - Starts a loop that repeats 4 times, with `i` taking values `0`, `1`, `2`, and `3`.
> 
> 3. `number = float(input("Enter a number: "))`
> Each iteration, reads a number from the user, converts it to `float`, and stores it in `number`.
>
> 4. `total += number`
> Adds the current number to `total` and stores the new sum back in `total`.
>
> 5. `average = round(total / 4, 2)`
> Divides `total` by `4` to get the average, rounds it to 2 decimal places, and stores it in `average`.
>
> 6. `print(f"The average is: {average}")`
> - Prints a message showing the value of `average`.