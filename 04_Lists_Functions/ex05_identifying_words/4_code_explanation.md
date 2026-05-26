> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `words_list = ["New York", "Tokyo", "Paris", "London", "Dubai", "Los Angeles"]`
> - Creates a list called words_list containing six famous city names, each stored as a string.
> 
> 2. `shortest_word = min(words_list, key=len)`
> - Uses the min() function to find the shortest string in words_list. The argument key=len tells Python to compare the elements by their length in characters, not alphabetically. The shortest city name is stored in the variable shortest_word.
> 
> 3. `longest_word = max(words_list, key=len)` 
> - Uses the max() function to find the longest string in words_list. Again, key=len makes the comparison based on the number of characters. The longest city name is stored in the variable longest_word.
> 
> 4. `print(f"Shortest word: {shortest_word}")` 
> - Prints a message showing which city is the shortest, inserting the value of shortest_word into the f‑string.
> 
> 5. `print(f"Longest word: {longest_word}")`
> - Prints a message showing which city is the longest, inserting the value of longest_word into the f‑string.