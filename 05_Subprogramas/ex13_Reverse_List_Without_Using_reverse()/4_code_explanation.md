> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `def invert(lst):`
> - Defines a function named `invert` with one parameter `lst`.
> 
> 2. `new_list = []`
> - Creates an empty list to store the reversed elements.
> 
> 3. `for item in lst:` 
> - Starts a loop through each element in the original list.
> 
> 4. `new_list.insert(0, item)` 
> - Inserts each element at the beginning of the new list.
>
> 5. `return new_list`
> - Returns the reversed list.
> 
> 6. `print(invert([1, 2, 3, 4, 5]))`
> - Calls the function with a list of numbers and prints the result.
> 
> 7. `print(invert(['a', 'b', 'c']))` 
> - Calls the function with a list of letters and prints the result.