> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `cities = []`
> - Creates an empty list named cities. This list will store city names as text (strings).
> 
> 2. `cities.append("New York")`
> `cities.append("Tokyo")`
> `cities.append("Paris")`
> `cities.append("London")`  
> - Each append() call adds a new city to the end of the list After these four lines, cities is: ["New York", "Tokyo", "Paris", "London"].
> 
> 3. `print(f"Original list: {cities}")` 
> - Prints the text "Original list:" followed by the current contents of the cities list.
> 
> 4. `cities.insert(2, "Dubai")` 
> - Inserts "Dubai" at index 2. The element that was at index 2 ("Paris") and the ones after it are shifted to the right. Now the list becomes: ["New York", "Tokyo", "Dubai", "Paris", "London"].
> 
> 5. `print(f"List after insert: {cities}")` 
> - Shows the list after the insertion so you can see the updated order.
>
> 6. `cities[1] = "Los Angeles"`
> - Accesses the element at index 1 and replaces it with "Los Angeles". Before: index 1 was "Tokyo". After: the list is now ["New York", "Los Angeles", "Dubai", "Paris", "London"].
> 
> 7. `print(f"List after modifying index 1: {cities}")`  
> - Prints the list after changing the value at index 1.
> 
> 8. `cities.pop(3)` 
> - Removes the element at index 3 from the list. That element is "Paris". After removal, the list becomes: ["New York", "Los Angeles", "Dubai", "London"].
> 
> 9. `print(f"List after removing index 3: {cities}")` 
> - Shows the list after the removal so you can confirm the change.
> 
> 10. `print(f"Number of elements in the list: {len(cities)}"` 
> - len(cities) returns the number of items in the list. Here, the result is 4. The line prints that number with a descriptive message.
>
> 11. `print("\nLoop using a normal FOR:")`
> - Prints a title for the next section. \n adds a blank line before the text to separate it visually.
> 
> 12. `for i in range(len(cities)):`
> `print(f"Index {i} : {cities[i]}")`    
> - range(len(cities)) generates all valid indices of the list (from 0 to len(cities) - 1). for i in range(len(cities)): loops over each index i. Inside the loop, cities[i] gets the city at that index. The print shows both the index and the corresponding city.
> 
> 13. `print("\nLoop using enumerate():")` 
> - Prints another title for the second loop, again with a blank line before it.
> 
> 14. `for index, value in enumerate(cities):` 
> `print(f"Index {index} : {value}")`
> - enumerate(cities) returns pairs (index, value) for each element in the list. index is the position, value is the city name. The loop goes through all cities and prints both index and value in a clear format.