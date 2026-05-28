> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `total = 0`
> - Initializes `total` to `0` to accumulate the sum.
>
> 2. `for i in range(20):`
> - Starts a loop that runs 20 times, with `i` from `0` to `19`.
>
> 3. `number = float(input(f"Enter number {i + 1}: "))`
> - Each iteration, asks the user for a number, showing its position (`i + 1`), converts it to `float`, and stores it in `number`.
>
> 4. `total += number`
> - Adds `number` to `total`.
> 
> 5. `average = total / 20`
> - Divides `total` by `20` to get the average and stores it in `average`.
>
> 6. `print(f"Sum = {total}")`
> - Prints the total sum.
>
> 7. `print(f"Average = {average}")`
> - Prints the average.