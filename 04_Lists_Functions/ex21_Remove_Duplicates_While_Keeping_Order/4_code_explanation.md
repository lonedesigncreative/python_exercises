> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`
> - Creates a list named `lst` with repeated values.
> 
> 2. `unique = []`
> - Creates an empty list to store unique values.
> 
> 3. `for item in lst:` 
> - Starts a loop that goes through each element in the list.
> 
> 4. `if item not in unique:` 
> - Checks if the element is not already in the `unique` list.
>
> 5. `unique.append(item)`
> - Adds the element to the `unique` list.
> 
> 6. `removed = len(lst) - len(unique)`
> - Calculates how many elements were removed.
> 
> 7. `print("Without duplicates:", unique)` 
> - Prints the cleaned list.
> 
> 8. `print("Removed elements:", removed)` 
> - Prints the number of removed elements.