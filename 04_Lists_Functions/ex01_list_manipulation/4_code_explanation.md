> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `numbers = []`
> - This creates a new empty list called numbers. It will be used to store integer values.
> 
> 2. `numbers.append(4)`
> `numbers.append(6)`
> `numbers.append(2)`
> `numbers.append(9)`  
> - Each append() call adds a new element to the end of the list. After these four lines, numbers is: [4, 6, 2, 9].
> 
> 3. `print(f"Original list: {numbers}")` 
> - Prints the text "Original list:" followed by the current contents of the list. Output: Original list: [4, 6, 2, 9].
> 
> 4. `numbers.insert(1, 100)` 
> - insert(1, 100) adds the value 100 at index 1. The existing elements from index 1 onwards are shifted to the right. Now the list is: [4, 100, 6, 2, 9].
> 
> 5. `print(f"List after insert: {numbers}")` 
> - Prints the list after the insertion. Output: List after insert: [4, 100, 6, 2, 9].
>
> 6. `numbers[2] = 31`
> - Accesses the element at index 2 and replaces it with 31. Before: index 2 was 6. After: it becomes 31. List now: [4, 100, 31, 2, 9].
> 
> 7. `print(f"List after modifying index 2: {numbers}")`  
> - Prints the list after changing index 2. Output: List after modifying index 2: [4, 100, 31, 2, 9].
> 
> 8. `numbers.pop(1)` 
> - pop(1) removes the element at index 1 from the list. That element (100) is removed, and the remaining elements shift left. List now: [4, 31, 2, 9].
> 
> 9. `print(f"List after removing index 1: {numbers}")` 
> - Prints the list after removing index 1. Output: List after removing index 1: [4, 31, 2, 9].
> 
> 10. `print(f"Number of elements in the list: {len(numbers)}")` 
> - len(numbers) returns the number of items in the list. Here, the length is 4. Output: Number of elements in the list: 4.
>
> 11. `for value in numbers:`
`print(f"Index {numbers.index(value)} : {value}")`
> - This for loop iterates over each value in numbers. numbers.index(value) finds the first index where that value appears in the list. Then it prints the index and the value. ⚠️ Note: if the list had duplicate values, index() would always return the index of the first occurrence, which can be misleading.
> 
> 12. `for index, value in enumerate(numbers, 5):`
> `print(f"Index {index} : {value}")`    
> - enumerate(numbers, 5) loops over the list and returns pairs: (index, value). The index starts at 5 instead of 0 because of the second argument. On each iteration, index is the counter, and value is the list element. It prints both in the format: Index <index> : <value>.