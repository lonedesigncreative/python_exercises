> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `import statistics as st`
> - Imports the statistics module and assigns it the alias st, allowing you to use functions like st.mean().
> 
> 2. `temperatures = [18.5, 20.0, 19.3, 21.7, 22.1, 17.8, 16.9, 23.4, 24.0, 19.8]`
> - Creates a list named temperatures containing ten floating‑point temperature values.
> 
> 3. `maximum = max(temperatures)` 
> - Finds the highest temperature in the list and stores it in the variable maximum.
> 
> 4. `minimum = min(temperatures)` 
> - Finds the lowest temperature in the list and stores it in the variable minimum.
> 
> 5. `total = sum(temperatures)`
> - Adds all the temperature values together and stores the result in total.
>
> 6. `count = len(temperatures)`
> - Counts how many temperature readings exist in the list and stores that number in count.
> 
> 7. `average_traditional = total / count`
> - Calculates the average temperature manually by dividing the total sum by the number of readings.
>
> 8. `average_st = st.mean(temperatures)`
> - Calculates the average temperature using the mean() function from the statistics module.
> 
> 9. `print(f"Minimum value: {minimum}")`
> - Displays the lowest temperature.
> 
> 10. `print(f"Maximum value: {maximum}")` 
> - Displays the highest temperature.
> 
> 11. `print(f"Sum: {total}")` 
> - Displays the sum of all temperatures.
> 
> 12. `print(f"Count: {count}")`
> - Displays how many temperature values were recorded.
>
> 13. `print(f"Traditional average: {average_traditional}")`
> - Displays the average calculated manually.
> 
> 14. `print(f"Average using statistics: {average_st}")`
> - Displays the average calculated using the statistics module.