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



# 3 - [ ]

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

# 4 - def

## What it is:  
`def` is a Python keyword used to define a function.

>> “Create a reusable block of code with a name.”

A function lets you:
- organize code
- avoid repetition
- receive inputs
- return outputs

> [!NOTE]
> ### Basic structure:
>    - `def function_name(parameters):`
>    - `code_block`
> **Example:**
>    - `def greet():`
>      - `print("Hello!")`


> [!IMPORTANT]
> **## What def does**
> - Creates a function
> - Gives it a name
> - Defines parameters
> - Defines the code that runs when the function is called

> [!TIP]
> **## Why functions are useful**
> - Avoid repeating code
> - Make programs easier to read
> - Allow modular programming
> - Allow reuse in different parts of the program

> [!CAUTION]
> - **Indentation is required** → code inside the function must be indented.
> - **Functions must be called** → defining is not enough.
> - **Return ends the function** → anything after return is ignored.
> - **Parameters must match** → wrong number of arguments gives error.
> - **Functions create their own scope** → variables inside are local.

**Example:**
*Example 1 - Function with no parameters*
`def say_hello():`
  `print("Hello, John!")`

Call it:
> say_hello()

*Example 2 - Function with one parameter*
`def greet(name):`
  `print("Hello", name)`

Call it:
> greet("Ana")


# 5 - Len

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


# 6 - Sum

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