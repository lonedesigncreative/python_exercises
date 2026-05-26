> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `numbers = [14, 89, 23, 67, 45, 92, 31, 58]`
> - Creates a list called numbers containing eight integer values.
> 
> 2. `numbers.sort(reverse=True)`
> - Sorts the list in place in descending order (from largest to smallest) because reverse=True is used.
> 
> 3. `print(numbers)` 
> - Prints the entire sorted list, so you can see the numbers from the largest to the smallest.
> 
> 4. `print(f"2nd largest value in the list: {numbers[-2]}")` 
> - Uses negative indexing to access numbers[-2], which is the second element from the end of the list. Because the list is sorted in descending order, this position corresponds to the second largest value, and it is printed in the message.