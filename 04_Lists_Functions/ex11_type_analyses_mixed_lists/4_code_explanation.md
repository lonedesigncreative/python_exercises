> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Lists"`
> - Creates a list named `nums` containing integers, floats, strings, and a boolean.
> 
> 2. `ints = floats = strings = booleans = 0`
> - Initializes four counters (`ints`, `floats`, `strings`, `booleans`) all with value `0`.
> 
> 3. `for item in nums:` 
> - Starts a loop that goes through each element in `nums`, assigning each to `item`.
> 
> 4. `if type(item) == int:` 
> - Checks if the type of `item` is `int`.
>
> 5. `ints += 1`
> - If true, increases the `ints` counter by `1`.
> 
> 6. `elif type(item) == float:`
> - If the previous condition was false, checks if `item` is of type `float`.
> 
> 7. `floats += 1` 
> - If true, increases the `floats` counter by `1`.
> 
> 8. `elif type(item) == str:` 
> - If previous conditions were false, checks if `item` is of type `str`.
>
> 9. `strings += 1`
> - If true, increases the `strings` counter by `1`.
> 
> 10. `elif type(item) == bool:`
> - If previous conditions were false, checks if `item` is of type `bool`.
> 
> 11. `booleans += 1` 
> - If true, increases the `booleans` counter by `1`.
> 
> 12. `print(ints, floats, strings, booleans)` 
> - Prints the four counters in one line.
>
> 13. `int_values = [x for x in nums if type(x) == int]` 
> - Creates a new list `int_values` containing only the elements of `nums` whose type is `int`.
>
> 11. `average_ints = sum(int_values) / len(int_values)` 
> - Calculates the average of the integers in `int_values` and stores it in `average_ints`.
> 
> 12. `print(average_ints)` 
> - Prints the value of `average_ints`.
>
> 13. `print(int_values)` 
> - Prints the list `int_values`.