> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `hours = int(input("Enter the hours: "))`
> - Reads a value from the user, converts it to an integer, and stores it in the variable `hours`.
> 
> 2. `double_value = 2 * number`  
> - Reads another value from the user, converts it to an integer, and stores it in the variable `minutes`.
>
> 3. `seconds = int(input("Enter the seconds: "))` 
> - Reads a third value from the user, converts it to an integer, and stores it in the variable `seconds`.
> 
> 4. `total_seconds = hours * 3600 + minutes * 60 + seconds`
> - Converts hours to seconds by multiplying by `3600`, minutes to seconds by multiplying by `60`, adds those to the existing `seconds`, and stores the total in `total_seconds`.
> 
> 5. `print(f"The total in seconds is: {total_seconds}")`  
> - Prints a formatted string showing the total number of seconds, inserting the value of `total_seconds` into the message.