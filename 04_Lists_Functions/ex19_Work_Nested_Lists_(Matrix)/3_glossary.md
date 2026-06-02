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


# 2 - Decimal (in Python called float)

## What it is:  
A decimal number - a number with a dot (.).

> [!CAUTION]
> - Python uses a dot, not a comma.
> - 3.5 is correct, 3,5 is wrong.

**Example:**
`price = 3.50`



# 3 - Text (in Python called string)

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


# 4 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

> [!CAUTION]
> - `input` always returns text, even if the user types a number.
> - If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`

# 5 - f-string (f"")

## What it is:
An f string is a special type of text that allows you to insert variables inside the text.

> [!CAUTION]
> - Don’t forget the **f** before the quotes.
> - Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`


# 6 - f-string (f"")

## What it is:
An f string is a special type of text that allows you to insert variables inside the text.

> [!CAUTION]
> - Don’t forget the **f** before the quotes.
> - Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`


# 7 - { }
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


# 8 - `If`

## What it is:  
An **if** statement checks a condition.
If the condition is **true**, the code inside **runs**.
If the condition is **false**, Python **skips it**.

> [!CAUTION]
> - **Indentation is required** → the code inside the `if` must be indented.
> - **If without else does nothing when false** → the program continues normally.
> - **Condition must be valid** → avoid writing text or invalid expressions inside the `if`.
> - **B****e careful with spacing** → `if age >= 18`: works, but `ifage>=18`: is invalid.

**Example:**
`score = 90`
`if score >= 80:`
   `print("Great job")`



# 9 - While (loop)
A **while loop** repeats a block of code **as long as the condition is True**.

>> “Keep doing this while the condition is true.”

> [!TIP]
>  - When the condition becomes **False**, the loop stops.

> [!IMPORTANT]
> ## How it works:
> - The condition is checked first.
> - If True, the loop runs.
> - If False, the loop stops.

> [!CAUTION]
> - **Avoid infinite loops** → always update the variable inside the loop.
> - **Condition must eventually become False** → otherwise the loop never ends.
> - **Indentation is required** → everything inside the loop must be indented.
> - **Be careful with `input()`** → convert values before comparing.
> - **Use while when repetitions are unknown** → if you know the exact number, `for` is usually better.

**Example:**
*Example 1 - Count from 1 to 5*
`i = 1`

`while i <= 5:`
    `print(i)`
    `i += 1`

*Example 2 - Ask for a password until correct*
`password = ""`

`while password != "1234":`
    `password = input("Enter password: ")`

`print("Access granted")`

*Example 3 - Countdown*
`n = 5`

`while n > 0:`
    `print(n)`
    `n -= 1`


# 10 - `!=`

## What it is:  
The **!=** operator means **not equal to**.
It checks if **two values are different**.

- If the values are different → True
- If the values are the same → False

> [!CAUTION]
> - **!= is comparison, not assignment** → don’t confuse with `=`.
> - **Compare compatible types** → `"10" != 10` is True because one is text and the other is a number.
> - **Be careful with input()** → convert before comparing (`int(input())`).
> - **Case sensitivity matters** → `"Ana" != "ana"` is True.
> - **Spacing matters** → write a `!= 5`, `not a!=5abc`.

**Example:**
`age = 18`
`print(age != 20)`   # True

`name = "Ana"`
`print(name != "Ana")`   # False


# 11 - [ ]

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


# 12 – Append

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


# 13 - Len

## What it is:
`len` is a **built in Python function** that returns the **number of items** in a collection.

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


# 14 - Sum

## What it is:  
`sum` is a **built in Python function** that adds **all the numbers in an iterable** (like a list, tuple, or set) and returns the **total**.

>> “Add all these values and give me the result.”

> [!NOTE]
> ### Basic structure:
>    - `sum(iterable)`
> **or**
>    - `sum(iterable, start_value)`

> [!TIP]
> **## Common uses**
> **Total of a list**
> **Sum of even/odd numbers**
> **Sum of values in a loop**
> **Sum of dictionary values** (using `.values()`)
> - **Example:**
> `scores = {"Ana": 10, "João": 15, "Maria": 20}`
> `print(sum(scores.values()))`   # 45

> [!CAUTION]
> - **Iterable must contain numbers** → otherwise it errors.
> - **Start value must be a number** → `sum(list, "a")` is invalid.
> - **Large lists are fine** → sum is optimized.
> - **Use sum, not manual loops** → cleaner and faster.
> - **Works only with iterables** → not with single numbers.

> [!WARNING]
> **## What break does NOT do**
> It **cannot** add strings
> It **cannot** add lists
> It **cannot** add mixed types (e.g., number + string)
>   - `sum(["a", "b"])   # ❌ error`

**Example:**
*Example 1 - Sum of a list of numbers*
`numbers = [1, 2, 3, 4]`
`print(sum(numbers))`   # 10

*Example 2 - Sum of a tuple*
`values = (10, 20, 30)`
`print(sum(values))`   # 60



# 15 - Min()

## What it is:  
`min` is a built in Python function that returns the smallest value in an iterable (list, tuple, set, etc.) or among multiple values.

>> “Give me the smallest element.”

> [!NOTE]
> ### Basic structure:
> **Using an iterable**
>    - `min(iterable)`
> **Using multiple values**
>    - `min(value1, value2, value3)`

> [!IMPORTANT]
> **## How `min` works**
> - With **numbers** → returns the lowest number
> - With **strings** → returns the first alphabetically
> - With **mixed types** → ❌ error
> - With **empty iterables** → ❌ error

> [!TIP]
> **## Using `min` with dictionaries**
> You can get the smallest key:
>   - `data = {"a": 10, "c": 5, "b": 7}`
>     `print(min(data))`   # "a"
> Or the smallest **value**:
>   - `print(min(data.values()))` # 5

> [!CAUTION]
> - **Iterable cannot be empty** → `min([])` gives an error.
> - **Types must be comparable** → numbers + strings = error.
> - **Strings use alphabetical order** → `"Ana"` < `"Maria"`.
> - **Use min(values) for dict values** → keys and values behave differently.
> - **min returns the value, not the index** → use `index()` if you need the position.


**Example:**
*Example 1 - Smallest number in a list*
`numbers = [5, 2, 9, 1]`
`print(min(numbers))`   # 1

*Example 2 - Smallest number in a tuple*
`values = (10, 3, 7)`
`print(min(values))`   # 3

*Example 3 - Smallest of multiple arguments*
`print(min(8, 4, 6))`   # 4



# 16 - Max()

## What it is:  
`max` is a **built in Python function** that returns the **largest value** in an iterable (list, tuple, set, etc.) or among multiple values.

>> “Give me the biggest element.”

> [!NOTE]
> ### Basic structure:
> **Using an iterable**
>    - `max(iterable)`
> **Using multiple values**
>    - `max(value1, value2, value3)`

> [!IMPORTANT]
> **## How `max` works**
> - With **numbers** → returns the highest number
> - With **strings** → returns the last alphabetically
> - With **mixed types** → ❌ error
> - With **empty iterables** → ❌ error

> [!TIP]
> **## Using `max` with dictionaries**
> Smallest key alphabetically:
>   - `data = {"a": 10, "c": 5, "b": 7}`
>     `print(max(data))`   # "c"
> Largest **value**:
>   - `print(min(data.values()))` # 10

> [!CAUTION]
> - **Iterable cannot be empty** → `max([])` gives an error.
> - **Types must be comparable** → numbers + strings = error.
> - **Strings use alphabetical order** → `"Maria"` < `"Ana"`.
> - **Use max(values) for dict values** → keys and values behave differently.
> - **max returns the value, not the index** → use `index()` if you need the position.


**Example:**
*Example 1 - Largest number in a list*
`numbers = [5, 2, 9, 1]`
`print(max(numbers))`   # 9

*Example 2 - Largest number in a tuple*
`values = (10, 3, 7)`
`print(max(values))`   # 10

*Example 3 - Smallest of multiple arguments*
`print(max(8, 4, 6))`   # 8