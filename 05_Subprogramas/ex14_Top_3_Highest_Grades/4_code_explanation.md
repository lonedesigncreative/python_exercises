> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `grades = [14, 8, 17, 12, 9, 18, 11, 16, 7, 13]`
> - Creates a list named `grades` with ten values.
> 
> 2. `grades.sort(reverse=True)`
> - Sorts the list in descending order.
> 
> 3. `top3 = grades[:3]` 
> - Stores the first three elements (the highest grades) in `top3`.
> 
> 4. `fails = len([g for g in grades if g < 10])` 
> - Counts how many grades are below 10.
>
> 5. `print("Top 3:", top3)`
> - Prints the top three grades.
> 
> 6. `print("Fails:", fails)`
> - prints the number of failing grades.