# 1 - Print

## What it is:  
`print` is a command that shows something on the screen.

> [!CAUTION]
> - **Always use parentheses** → print("Hello")
> - Text must be inside quotes `" "`
> - Missing quotes or parentheses causes an error.

**Example:**
`print("Python!")`

This will display:
- *Python!*

# 2 - Text (in Python called string)

## What it is:  
Text inside quotes `" "`.

> [!CAUTION]
> - Text must always be inside quotes.
> - If you put numbers inside quotes, they become text, not numbers.

**Example:**
`name = "LoneDesign"`

# Summary

| **Concept** | **Meaning** | **Example** |
| :--- | :--- | :--- |
| print | hows something on the screen | print("Hi") |
| integer | Whole number | 10 |
| decimal (float) | Number with decimal | 2.5 |
| text (string) | Words inside quotes | "Hello" |


# 2 - f-string (f"")

## What it is:
An f string is a special type of text that allows you to insert variables inside the text.

> [!CAUTION]
> - Don’t forget the **f** before the quotes.
> - Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`


# 3 - { }
## What it means:
The `{ }` are used to show the value of a variable inside the text.

> [!CAUTION]
> - Inside `{ }` you must put a **variable** or an **expression**.
> - If you put text without quotes, it gives an error.
> - If you put quotes inside `{ }`, it becomes text again.

**Example:**
`age = 25`
`print(f"You are {age} years old")`

Python replaces {age} with the value of the variable.

# Summary

| **Concept** | **Meaning** | **Example** |
| :---: | :--- | :---: |
| input | Asks the user to type something | `input("Your name: ")` |
| f-string | Text that can show variables | `f"Hello {name}"` |
| { } | Shows the variable’s value inside the f string | `{age}` |


# 4 - [ ]

## What it means:
In Python, **square brackets** `[]` are used for **three main things**:
  1. Creating lists
  2. Accessing elements by index
  3. Slicing lists or strings

> [!IMPORTANT]


> ### 1. [] to create a list
> - A **list** is a collection of items.
> 
> `numbers = [1, 2, 3, 4]`
> `fruits = ["apple", "banana", "orange"]`
> `mixed = [10, "hello", True]`
> 
> ### 2. [] to access an element (indexing)
> - Indexes start at **0**.
> 
> `fruits = ["apple", "banana", "orange"]`
> 
> `print(fruits[0])`   # apple
> `print(fruits[1])`   # banana
> `print(fruits[2])`   # orange
> 
> - Negative indexes count from the end:
> 
> `print(fruits[-1])`  # orange
> 
> ### 3. [] to slice (get a part of a list or string)
> 
> `numbers = [10, 20, 30, 40, 50]`
> 
> `print(numbers[1:4])`   # [20, 30, 40]
> `print(numbers[:3])`    # [10, 20, 30]
> `print(numbers[2:])`    # [30, 40, 50]
> 
> - Works with **strings** too:
> 
> `text = "Python"`
> `print(text[0:3])`   # Pyt

> [!NOTE]
> ### 4. Other uses of []
> **4.1 - Empty list**
> `empty = []`
>
> **4.2 - List inside a list (nested list)**
> `matrix = [[1, 2], [3, 4]]`
> 
> > **4.3 - Adding items**
> `fruits.append("kiwi")`

> [!CAUTION]
> - **Index starts at 0** → `fruits[0]` is the first item.
> - **Index out of range error** → `fruits[10]` gives an error.
> - **Lists are mutable** → you can change items inside them.
> - **Slicing creates a copy** → modifying the slice doesn’t change the original list.
> - **Use [] for lists, not ()** → parentheses are for tuples.


# 5 - True

## What it is:  
In Python, **True** is a **Boolean value**.
It represents something that is **correct**, **valid**, or **logically true**.

> [!NOTE]
> **Python has only two Boolean values:**
> **True**
> **False**
>
> **These values are used in:**
    > **if statements**
    > **while loops**
    > **comparisons**
    > **logical operations**

> [!CAUTION]
> - **Capital letter required** → write `True`, not `true`.
> - **Do not confuse with strings** → `"True"` is not the same as `True`.
> - **Comparisons return True or False** → e.g., `5 == 5` gives True.
> - **While True needs break** → otherwise it becomes an infinite loop.
> - **True is not the same as 1** → they compare equal, but they are different types.

> [!IMPORTANT]
> - **True starts with a capital T** → `true` (lowercase) does not work in Python.
> - **True is a Boolean, not a string** → `"True"` is text, not a Boolean.
> - **True equals 1 in numeric context** → (but you normally don’t use it this way)
>> **Example:** `print(True == 1)`   # True

**Example:**
  - ***Example 1 - True as a value***
`is_sunny = True`
`print(is_sunny)`

  - ***Example 2 - True from a comparison***
`print(5 > 2)`   # True

  - ***Example 3 - True in an if statement***
`age = 20`

`if age >= 18:`
    `print("Adult")`   # This runs because the condition is True

  - ***Example 4 - True in a while loop***
`while True:`      
    `print("Looping...")`
    `break`


# 6 - Sort()

## What it is:  
`sort` is a **list method** in Python that **sorts the list in place** — meaning it **modifies the original list**.

>> “Rearrange the items in this list in order.”

By default, it sorts:
- num**b**ers → from smallest to largest
- **strings** → alphabetical ordern`


> [!NOTE]
> ### Basic structure:
>    - `list.sort()`


> [!IMPORTANT]
> **## Difference between **sort** and **sorted****
> 
> | **Feature** | **sort** | **sorted** |
> | :--- | :--- | :--- |
> | Modifies original list | ✔ Yes | ❌ No |
> | Returns a new list | ❌ No | ✔ Yes |
> | Works only on lists | ✔ Yes | ❌ No (works on any iterable) |
>
> **Example:**
> `numbers = [3, 1, 2]`
> `new_list = sorted(numbers)`
> 
> `print(numbers)`   # [3, 1, 2]
> `print(new_list)`  # [1, 2, 3]



> [!TIP]
> **## Parameters**
> - **✔ `reverse=True`**
>   - Sorts in descending order.
> - **`✔ key=...`**
>   - Defines the rule for sorting.
> 
> - Common keys:
> - **key=len** → sort by length
> - **key=str.lower** → case‑insensitive sort
> - **key=lambda** → custom rules


> [!CAUTION]
> - **sort modifies the list** → use `sorted()` if you need the original.
> - **Items must be comparable** → cannot mix numbers and strings.
> - **Sorting strings is alphabetical** → not by length unless you use `key=len`.
> - **sort returns None** → don’t do `new = list.sort()`.
> - **Stable sort** → items with same key keep original order.


**Example:**
*Example 1 - Sort numbers*
`numbers = [5, 2, 9, 1]`
`numbers.sort()`

`print(numbers)`   # [1, 2, 5, 9]

*Example 2 - Sort strings alphabetically*
`names = ["Ana", "João", "Maria"]`
`names.sort()`

`print(names)`   # ['Ana', 'João', 'Maria']

*Example 3 - Sort in reverse order*
`numbers = [5, 2, 9, 1]`
`numbers.sort(reverse=True)`

`print(numbers)`   # [9, 5, 2, 1]

*Example 4 - Sort by length using key=len*
`words = ["Python", "is", "amazing"]`
`words.sort(key=len)`

`print(words)`   # ['is', 'Python', 'amazing']

*Example 5 - Sort a list of lists by length*
`data = [[1, 2], [1], [1, 2, 3]]`
`data.sort(key=len)`

`print(data)`   # [[1], [1, 2], [1, 2, 3]]


# 7 - Reverse()

## What it is:  
`reverse` is a **list method** in Python that **reverses the order of the items in the list**.

>> “Flip the list backwards.”

By default, it sorts:
- num**b**ers → from smallest to largest
- **strings** → alphabetical ordern`


> [!NOTE]
> ### Basic structure:
>    - `list.reverse()`


> [!WARNING]
> It **modifies the original list**
> It **does NOT sort**
> It **does NOT return a new list** (returns `None`)

>
> **Example:**
> `numbers = [3, 1, 2]`
> `new_list = sorted(numbers)`
> 
> `print(numbers)`   # [3, 1, 2]
> `print(new_list)`  # [1, 2, 3]


> [!IMPORTANT]
> **## Difference between **reverse** and **sorted(reverse=True)****
> 
> | **Feature** | **reverse** | **sorted(reverse=True)** |
> | :--- | :--- | :--- |
> | Changes original list | ✔ Yes | ❌ No |
> | Sorts the list | ❌ No | ✔ Yes |
> | Only flips order | ✔ Yes | ❌ No  |
> | Returns a new list | ❌ No  | ✔ Yes |
>
> **Example:**
> `numbers = [3, 1, 2]`
>
> `numbers.reverse()`
> `print(numbers)`   # [2, 1, 3]  (just flipped)
>
> `print(sorted(numbers, reverse=True))`  # [3, 2, 1] (sorted)



> [!TIP]
> **## Reverse without modifying the list**
> - If you want a **reversed copy**, use slicing:
>   - `new_list = numbers[::-1]`
> 
> - Or use::
> - `reversed_list = list(reversed(numbers))`


> [!CAUTION]
> - **reverse modifies the list** → use slicing if you need the original.
> - **reverse returns None** → don’t do `new = list.reverse()`.
> - **reverse does NOT sort** → it only flips the order.
> - **Works only on lists** → not on strings or tuples.
> - **Use reversed()** for other iterables → strings, tuples, etc.


**Example:**
*Example 1 - Reverse a list of numbers*
`numbers = [1, 2, 3, 4]`
`numbers.reverse()`

`print(numbers)`   # [4, 3, 2, 1]

*Example 2 - Reverse a list of strings*
`words = ["Python", "is", "cool"]`
`words.reverse()`

`print(words)`   # ['cool', 'is', 'Python']