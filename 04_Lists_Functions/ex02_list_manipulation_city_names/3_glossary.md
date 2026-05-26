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

# 3 - f-string (f"")

## What it is:
An f string is a special type of text that allows you to insert variables inside the text.

> [!CAUTION]
> - Don’t forget the **f** before the quotes.
> - Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`

# 4 - { }

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

# 5 - For (loop)

A **for loop** is used when you want to **repeat a block of code a specific number of times** or **go through each item in a sequence** (like a list, string, or range).

## What it means:
> “For each value in this sequence, do this action.”

> [!CAUTION]
> - **Indentation is required** → everything inside the loop must be indented.
> - **range upper limit is not included** → `range(1, 5)` stops at 4, not 5.
> - **Variable name is temporary** → `i`, `n`, `item` are just loop variables.
> - **Avoid infinite loops** → `for` loops normally don’t go infinite, but wrong ranges can cause issues.
> - **Be careful with input()** → convert values before using them in a range.
> - **Don’t modify the list while looping** → it can break the loop.

**Example:**
*Example 1 - Loop from 1 to 5*
`for i in range(1, 6):`
    `print(i)`

*Example 2 - Loop through a list*
`fruits = ["apple", "banana", "orange"]`

`for fruit in fruits:`
    `print(fruit)`

*Example 3 - Loop through each letter in a string*
`for letter in "Python":`
    `print(letter)`

*Example 4 - Sum numbers from 1 to 10*
`total = 0`

`for n in range(1, 11):`
    `total += n`

`print(total)`

> [!IMPORTANT]
> - #### How the `range()` works:
> The function **range** creates a sequence of numbers.
>   - `range(5)` → 0,1,2,3,4
>   - `range(1, 5)` → 1,2,3,4
>   - `range(1, 10, 2)` → 1,3,5,7,9 (step of 2)

# 6 - [ ]

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



# 7 - Append

## What it means:
`append` is a **list method** in Python.
It is used to **add one new item to the end of a list**.

>> “Put this new element at the end of the list.”


> [!CAUTION]
> - **append adds only one item** → even if that item is a list.
> - **append modifies the original list** → lists are mutable.
> - **append always adds at the end** → never at the beginning or middle.
> - **append returns None** → don’t do `new_list = list.append(x)`.
> - **Use extend for multiple items** → `append([1,2])` ≠ `extend([1,2])`.


> [!WARNING]
> **## What break does NOT do**
> It does **not** add multiple items at once → use **extend** for that.
> It does **not** insert in the middle → use **insert**.
> It does **not** return a new list → it **modifies the existing list**.


> **Example:**
*Example 1 - Add one item to a list*
`fruits = ["apple", "banana"]`
`fruits.append("orange")`

`print(fruits)`   # ["apple", "banana", "orange"]


*Example 2 - Append a number*
`numbers = [1, 2, 3]`
`numbers.append(4)`

`print(numbers)`   # [1, 2, 3, 4]


*Example 3 - Append different types*
`data = []`
`data.append(10)`
`data.append("hello")`
`data.append(True)`

`print(data)`   # [10, "hello", True]


*Example 4 - Append a list (becomes nested)*
`items = [1, 2, 3]`
`items.append([4, 5])`

`print(items)`   # [1, 2, 3, [4, 5]]


# 8 - Insert

## What it is:
`insert` is a **list method** used to **add an item at a specific position** in a list.

>> “Put this element exactly at this index.”

> [!NOTE]
> ### The structure is:
>    - list.insert(index, value)
> **index** → where the item will be placed
> **value** → the item you want to add


> [!CAUTION]
> - **Index shifts the list** → items move to the right.
> - **Insert is slower than append** → because it must shift elements.
> - **Index must be an integer** → no floats or strings.
> - **Negative indexes work** → `insert(-1, x)` inserts before the last item.
> - **Use append for adding at the end** → simpler and faster.


> [!TIP]
> **## Difference between insert and append**
> **append** → always adds at the **end**
> **insert** → adds at a **specific position**


> **Example:**
*Example 1 - Insert at the beginning*
`fruits = ["banana", "orange"]`
`fruits.insert(0, "apple")`

`print(fruits)`   # ["apple", "banana", "orange"]


*Example 2 - Insert in the middle*
`numbers = [1, 2, 4, 5]`
`numbers.insert(2, 3)`

`print(numbers)`   # [1, 2, 3, 4, 5]


# 9 - Index

## What it is:
`index` is a **list method** in Python.
It is used to **find the position (index) of an item inside a list**.

>> “Tell me the position of this element in the list.”

> [!NOTE]
> ### The structure is:
>    - list.index(value)
> It returns the **first position** where the value appears.


> [!CAUTION]
> - **Returns only the first match** → not all positions.
> - **Raises ValueError if not found** → check with `in` first.
> - **Case sensitive for strings** → `"Ana"` ≠ `"ana"`.
> - **Works only on lists** → not on dictionaries or sets.
> - **Index starts at 0** → first item is position 0.


> [!WARNING]
> **## What happens if the item is not found?**
> - Python gives an error:
> `fruits = ["apple", "banana"]`
> `print(fruits.index("kiwi"))`   # ValueError
> 
> - To avoid this, you can check first:
> `if "kiwi" in fruits:`
> `print(fruits.index("kiwi"))`


> [!TIP]
> **## Difference between index and find**
> **index** → used for **lists**
> **find** → used for **strings**


> **Example:**
*Example 1 - Find the index of an item*
`fruits = ["apple", "banana", "orange"]`

`print(fruits.index("banana"))`   # 1


*Example 2 - Find the index of a number*
`numbers = [10, 20, 30, 40]`

`print(numbers.index(30))`   # 2


*Example 3 - If the item appears multiple times*

> [!IMPORTANT]
> - `index` returns only the first occurrence.

`values = [5, 7, 5, 9]`

`print(values.index(5))`   # 0

*Example 4 - Using index inside a loop*
`names = ["Ana", "João", "Maria"]`

`for name in names:`
    `print(name, names.index(name))`


# 10 - Len

## What it is:
`len` is a **built‑in Python function** that returns the **number of items** in a collection.

>> “Tell me how many elements this object has.”

> [!NOTE]
> ### You can use `len` with:
> 1. lists
> 2. strings
> 3. tuples
> 4. dictionaries
> 5. sets


> [!CAUTION]
> - **len works only on collections** → numbers like `10` or ´ don’t have length.
> - **Strings count characters** → including spaces.
> - **Dictionaries count keys** → not values.
> - **Nested lists count only top level** → `len([[1,2],[3,4]])` is 2.
> - **len returns an integer** → you can use it in comparisons.


> [!TIP]
> **## How `len` works**
> `len(object)` returns an **integer** representing how many elements the object contains.
> - **If the object is empty:**
> `print(len([]))`      # 0
> `print(len(""))`      # 0
> `print(len({}))`      # 0


> **Example:**
*Example 1 - Length of a list*
`fruits = ["apple", "banana", "orange"]`
`print(len(fruits))`   # 3


*Example 2 - Length of a string*
`text = "Python"`
`print(len(text))`   # 6


*Example 3 - Length of a dictionary (counts keys)*
`person = {"name": "Ana", "age": 25}`
`print(len(person))`   # 2

# 11 - Pop

## What it is:
`pop` is a **list method** that **removes an item from a list** and **returns the removed item**.

>> “Take out an element from the list and give it back to me.”

> [!NOTE]
> ### You can remove::
> - the **last item** (default)
> - an item at **a specific index**

> [!IMPORTANT]
> **## What pop does**
> - Removes an item
> - Returns the removed item
> - Changes the original list


> [!WARNING]
> **## What pop does NOT do**
> - It does **not** remove multiple items → use **remove** or slicing.
> - It does **not** remove by value → `remove()` does that.
> - It does **not** work on strings or dictionaries → only lists.
> 
> - To avoid this, you can check first:
> `if "kiwi" in fruits:`
> `print(fruits.index("kiwi"))`


> [!CAUTION]
> - **Index must exist** → `pop(10)` on a small list gives an error.
> - **Default is last item** → `pop()` with no index removes the last element.
> - **Returns the removed value** → useful for stacks and undo operations.
> - **Modifies the list** → the original list changes.
> - **Use remove() to delete by value** → `pop()` deletes by position.


> **Example:**
*Example 1 - Pop the last item*
`fruits = ["apple", "banana", "orange"]`
`removed = fruits.pop()`

`print(removed)`   # "orange"
`print(fruits)`    # ["apple", "banana"]


*Example 2 - Pop an item by index*
`numbers = [10, 20, 30, 40]`
`removed = numbers.pop(1)`

`print(removed)`   # 20
`print(numbers)`   # [10, 30, 40]


*Example 3 - Pop the first item*
`items = ["a", "b", "c"]`
`items.pop(0)`

`print(items)`   # ["b", "c"]

*Example 4 - Using pop in a loop*
`stack = [1, 2, 3]`

`while stack:`
    `print(stack.pop())`


# 12 - Enumerate

## What it is:
`enumerate` is a **built‑in Python function** that lets you loop through a list and **automatically get the index and the value at the same time**.

>> “Give me the position AND the item together while looping.”

This avoids writing manual counters like `i = 0`.

> [!NOTE]
> ### Basic structure:
> `for index, value in enumerate(list):`
> `...`
> - **index** → the position (0, 1, 2, …)
> - **value** → the item in the list


> [!IMPORTANT]
> **## Why use enumerate?**
> - Cleaner and easier than using a manual counter
> - Avoids mistakes with index management
> - Makes loops more readable
> - Works with any iterable (lists, tuples, strings, etc.)


> [!CAUTION]
> - **Index starts at 0 unless** you use `start=1`.
> - **Works only in loops** → you can’t get a single index directly.
> - **Unpack correctly** → always use `for i, x in enumerate(...)`.
> - **Don’t confuse with range** → `enumerate` gives both index and value.
> - **Works with any iterable** → not just lists.



> **Example:**
*Example 1 - Loop with index and value*
`fruits = ["apple", "banana", "orange"]`

`for index, fruit in enumerate(fruits):`
    `print(index, fruit)`

> **Output:**
> 0 apple
> 1 banana
> 2 orange


*Example 2 - Start counting from another number*
> [!TIP]
> - Use the `start=` parameter.

`for index, fruit in enumerate(fruits, start=1):`
    `print(index, fruit)`

> **Output:**
> 1 apple
> 2 banana
> 3 orange

*Example 3 - Using enumerate to find positions*
`names = ["Ana", "João", "Maria"]`

`for i, name in enumerate(names):`
    `if name == "Maria":`
        `print("Found at index:", i)`


*Example 4 - Enumerate with a list of numbers*
`numbers = [10, 20, 30]`

`for i, n in enumerate(numbers):`
    `print("Position:", i, "Value:", n)`


# 13 - Range

## What it is:
`range` is a built‑in Python function used to generate a **sequence of numbers**.
It is most commonly used in **for loops**.

>> “Create numbers starting from one value, ending before another value, increasing by a step.”


> [!NOTE]
> ## Three main forms of `range`
> ### 1. range(stop)
> - Starts at **0**, ends at **stop − 1**.
> 
> `**numbers = [1, 2, 3, 4]**`
> `print(i)`
> > **Output:** 0, 1, 2, 3, 4
> 
> ### 2. range(start, stop)
> - Starts at **start**, ends at **stop − 1**.
> 
> `for i in range(2, 6):`
> `print(i)`
> 
> > **Output:** 2, 3, 4, 5
> 
> `print(fruits[-1])`  # orange
> 
> ### 3. range(start, stop, step)
> - Adds a **step** (increment or decrement).
> 
> `for i in range(1, 10, 2):`
> `print(i)`
>
> > **Output:** 1, 3, 5, 7, 9


> [!IMPORTANT]
> ### Important details:
> - `range` **includes the start**
> - `range` **excludes the stop**
> - `range` **can go backwards**
> - `range` **does not create a list**, but a special sequence type
> - Convert to list with `list(range(...))` if needed
> > `print(list(range(5)))`   # [0, 1, 2, 3, 4]
>


> [!CAUTION]
> - **Stop is not included** → `range(1, 5)` gives 1, 2, 3, 4.
> - **Step cannot be zero** → `range(1, 10, 0)` gives an error.
> - **Use negative step to count down** → otherwise it loops forever.
> - **Range works only with integers** → no floats.
> - **Often used in for loops** → but can be converted to a list.



> **Example:**
*Example 1 - Counting backwards*
`for i in range(10, 0, -1):`
    `print(i)`


*Example 2 - Loop from 1 to 10 (inclusive)*
`for i in range(1, 11):`
    `print(i)`


*Example 3 - Loop through even numbers*
`for i in range(0, 21, 2):`
    `print(i)`

# 14 - \n

## What it is:
`\n` is a **newline character** in Python..

>> "Go to the next line."

When Python sees `\n` inside a string, it **breaks the line** and continues printing on the next one.

> [!IMPORTANT]
> ### Important details:
> - `\n` counts as **one character** in a string.
> - It works only **inside quotes**.
> - It is not shown literally → **it creates a line break**.
> - For Windows files, Python still uses `\n` (it converts automatically).


> [!CAUTION]
> - **Don’t forget the backslash** → `/n` does nothing; only `\n` works.
> - **Use triple quotes for big text** → instead of many `\n`.
> - **Escape sequences matter** → `\t` is tab, `\\` is a backslash.
> - **Inside f-strings works normally** → `f"Hello\n{name}"`.
> - **In files, \n creates new lines** → important for writing logs.


> [!TIP]
> ### Where \n is used:
> - **print formatting**
> - **multiline messages**
> - **file writing** (to write lines)
> - **logs and reports**

> **Example:**
*Example 1 - New line in a print*
`print("Hello\nWorld")`

> **Output:**
> `Hello`
> `World`

*Example 2 - Multiple new lines*
`print("Line 1\nLine 2\nLine 3")`


*Example 3 - New line inside variables*
`text = "Name:\nTatiana"`
`print(text)`

*Example 4 - New line inside variables*
`name = "Ana"`
`age = 25`

`print("Name:", name, "\nAge:", age)`