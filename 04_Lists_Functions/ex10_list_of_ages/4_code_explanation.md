> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `ages = [25, 15, 19, 22, 37, 78, 46, 2, 67]`
> - Creates a list named `ages` with several integer values.
> 
> 2. `minors = 0`
> - Initializes a counter `minors` with value `0`.
> 
> 3. `for age in ages:` 
> - Starts a loop that goes through each element in `ages`, assigning each value to `age`.
> 
> 4. `if age < 18:` 
> - Checks if the current `age` is less than `18`.
>
> 5. `minors += 1`
> - If the condition is true, increases `minors` by `1`.
> 
> 6. `print(minors)`
> - Prints the total number of ages that are less than `18`.
> 
> 7. `ages.sort(reverse=True)` 
> - Sorts the `ages` list in descending order.
> 
> 8. `print(ages)` 
> - Prints the sorted `ages` list.
>
> 9. `user_age = int(input("Enter an age: "))`
> - Reads a value from the user, converts it to an integer, and stores it in `user_age`.
> 
> 10. `if user_age in ages:`
> - Checks whether `user_age` is present in the `ages` list.
> 
> 11. `print("The age is in the list")` 
> - Prints this message if the age is found in the list.
> 
> 12. `else:` 
> - Defines the alternative path if the age is not found.
>
> 13. `print("There is no one with that age in the list")` 
> - Prints this message if `user_age` is not in the list.