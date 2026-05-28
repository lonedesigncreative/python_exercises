> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `letter = input("Enter the letter S, C or V: ").upper()`
> - Reads a letter from the user, converts it to uppercase, and stores it in `letter`.
>
> 2. `match letter:`
> - Starts a `match` block to compare `letter` with several cases.
> 
> 3. `case "S":`
> `print("Single")`
> - If `letter` is `"S"`, prints `"Single"`.
>
> 4. `case "M":`
> `print("Married")`
> - If `letter` is `"M"`, prints `"Married"`.
>
> 5. `case "W":`
> `print("Widowed")`
> - If `letter` is `"W"`, prints `"Widowed"`.
>
> 6. `case _:`
> `print("Invalid marital status!")`
> - If `letter` is none of `"S"`, `"M"`, or `"W"`, prints `"Invalid marital status!"`.