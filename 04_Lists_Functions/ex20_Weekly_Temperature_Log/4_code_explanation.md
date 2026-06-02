> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `temps = [22, 25, 19, 28, 30, 24, 21]`
> - Creates a list named `temps` with seven temperature values.
> 
> 2. `print("Max:", max(temps))`
> - Prints the highest temperature.
> 
> 3. `print("Min:", min(temps))` 
> - Prints the lowest temperature.
> 
> 4. `avg = sum(temps) / len(temps)` 
> - Calculates the average temperature.
>
> 5. `print("Average:", avg)`
> - Prints the average temperature.
> 
> 6. `for i, t in enumerate(temps):`
> - Starts a loop with both index `i` and value `t`.
> 
> 7. `if t > avg:` 
> - Checks if the temperature is above average.
> 
> 8. `print("Above average on day:", i)` 
> - Prints the index of the day where the temperature was above average.