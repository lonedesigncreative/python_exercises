# 1 - def

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


# 2 - [ ]

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


# 3 - return

## What it is:  
`return` is a keyword used inside a function in Python.

>> “Send a value back to the place where the function was called.”

When Python reaches a `return`, the function stops immediately and gives back a result.

> [!NOTE]
> ### Basic usage:
>    - `def function_name():`
>     - `return value`

> [!IMPORTANT]
> **## **Important: `return` ends the function****
>
> Anything after `return` is **ignored**.
>
> `def test():`
>     `return 10`
>     `print("This will NOT run")`

## `return` vs `print`

| **Concept** | **What it does** |
| :--- | :--- |
| return | Sends a value back to the caller |
| print | Shows text on the screen |

### **Example:**
`def f():`
    `return 5`

`print(f())`   # prints 5

> [!NOTE]
> `return` gives the value.
> `print` only displays it.

> [!TIP]
> ### Functions can return any type:
>
>   - **Number**
>     - `def get_number():`
>       - `return 42`
>
> 
> 
>   - **String**
>     - `def greet():`
>       - `return "Hello"`
>
> 
> 
>   - **List**
>     - `def numbers():`
>       - `return [1, 2, 3]`
>
>
> 
>   - **Boolean**
>     - `def is_adult(age):`
>       - `return age >= 18`
>
>**------------------------------------**
>
> ### Functions can return multiple values (as a tuple):
>
> `def stats(a, b):`
>     `return a + b, a * b`
>
> `s, m = stats(3, 4)`
> `print(s, m)`   # 7 12
>
> 
>
>  ### return without a value:
>
> `def empty():`
>     `return`
>
> - This returns `**None**`.
>
> **------------------------------------**
>
> ### If a function has no return
>
> Python automatically returns **None**.
>
> `def hello():`
>   `print("Hi")`
> 
> `x = hello()`
> `print(x)`   # None

# Summary

| **Feature** | **Meaning** |
| :--- | :--- |
| return | Sends a value back |
| Ends the function | Code after return is ignored |
| Can return any type | numbers, strings, lists, booleans |
| No return → None | default behavior |


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


# 5 - List

## What it is:
A list in Python is an **ordered**, **mutable**, and **indexable** collection that can store **multiple values**, even of different types.

>> “A list is a container that holds several items in order, and you can change them.”

> [!NOTE]
> ## How to create a list
>
> `numbers = [1, 2, 3]`
> `names = ["Hannah", "John", "Mariah"]`
> `mixed = [10, "Python", True, 3.5]`

## Characteristics of a list

> | **Feature** | **Meaning** |
> | :--- | :--- |
> | Ordered | Keeps the order of items |
> | Mutable | You can change, add, or remove items |
> | Indexed | Each item has a position |
> | Allows duplicates | Repeated values are allowed |
> | Allows mixed types | Numbers, strings, booleans, etc. |



> [!IMPORTANT]
> ### 1. Accessing items (indexing)
> 
> `fruits = ["apple", "banana", "orange"]`
>
> `print(fruits[0])`   # apple
> `print(fruits[1])`   # banana
> `print(fruits[-1])`  # orange (last item)
>
> 
> ### 2. Changing items
> 
> `fruits[1] = "kiwi"`
> `print(fruits)`   # ["apple", "kiwi", "orange"]
>
> 
> ### 3. Adding items
> 
> - **3.1 - *append()* — add at the end**
> `fruits.append("grape")`
>
> - **3.2 - *insert()* — add at a specific position**
> `fruits.insert(1, "pear")`
>
> - **3.3 - `extend()` — add multiple items**
> `fruits.extend(["melon", "mango"])`
>
>
> ### 4. Removing items
> 
> **4.1 - *remove()* — remove by value**
> `fruits.remove("apple")`
>
> **4.2 - *pop()* — remove by index**
> `fruits.pop(0)`
> 
> > **4.3 - *clear()* — remove all items**
> `fruits.clear()`


> [!TIP]
> ### Checking if something is inside the list
>
> `if "banana" in fruits:`
>   `print("Banana is here!")`
>
>  Uses the **`in`** operator.
>
> ### Looping through a list
>
> `for item in fruits:`
>   `print(item)`


## Useful list methods
| **Method** | **Meaning** | **Example** | 
| :--- | :--- | :--- |
| append | 	Add at the end | list.append(x) |
| insert | 	Add at a position | list.insert(i, x) |
| pop | Remove by index | list.pop(i) |
| remove | Remove by value | list.remove(x) |
| sort | Sort ascending | list.sort() |
| reverse | Reverse order | list.reverse() |
| extend | Add multiple items | list.extend([...]) |


> [!CAUTION]
> ## Common mistakes
> 
> - **Index out of range** → accessing a position that doesn’t exist
> - **append vs extend confusion**
>   - `append` adds **one item**
>   - `extend` adds **multiple items**
> - **Lists are mutabl**e → changes affect the original list
> - **remove() fails if the value doesn’t exist**


## Summary:

> | **Concept** | **Meaning** |
> | :--- | :--- |
> | list | 	Ordered and mutable collection |
> | Mixed types allowed | `[1, "Ana", True]` |
> | Indexed | `list[0]` |
> | Mutable | Items can be changed |
> | Many methods | append, pop, remove, sort… |


# 6 - Set

## What it is:
A **set** in Python is an **unordered**, **mutable**, and **unique‑element** collection.

>> “A set is a bag of items where duplicates are not allowed, and order does not matter.”

> [!NOTE]
> ## How to create a set
>
> `numbers = {1, 2, 3}`
> `words = {"apple", "banana", "orange"}`
> `mixed = {1, "Python", True}`
>
> ### Empty set
>
> `empty = set()`   # correct
> `empty2 = {}`     # this is a dictionary, not a set


## Characteristics of a set

> | **Feature** | **Meaning** |
> | :--- | :--- |
> | Unordered | Items have no fixed position |
> | Unique elements | No duplicates allowed |
> | Mutable | You can add/remove items |
> | Fast membership test | `x in set` is very fast |
> | No indexing | You cannot do `set[0]` |


## Why sets are useful
- Removing duplicates
- Checking membership quickly
- Mathematical operations (union, intersection…)
- Comparing groups of items

> [!IMPORTANT]
>
> ## Mathematical operations
> Sets support operations similar to math sets.
> 
> ### 1. Union — combine items
> 
> `a = {1, 2}`
> `b = {2, 3}` 
> `print(a | b)`   # {1, 2, 3}
> 
> ### 2. Intersection — common items
>
> `print(a & b)`   # {2}
>
> ### 3. Difference — items in A but not B
>
> `print(a - b)`   # {1}
>
> ### 4. Symmetric difference — items not shared
>
> `print(a ^ b)`   # {1, 3}


> [!TIP]
> ### 1. Adding items
>
> - **1.1 - *add()***
> 
> `fruits = {"apple", "banana"}`
> `fruits.add("orange")` 
>
> 
> ### 2. Removing items
>
> - **2.1 - *remove()* — errors if item doesn’t exist**
> `fruits.remove("apple")`
>
> - **2.2 - *discard()* — safe remove**
> `fruits.discard("pear")`   # no error
>
> - **2.3 - *pop()* — removes a random item**
> `fruits.pop()`
>
> - **2.4 - `clear()` — empty the set**
> `fruits.clear()`


## Checking membership

`if "banana" in fruits:`
    `print("Banana is here!")`

Uses the **`in`** operator.


## Removing duplicates using a set
`nums = [1, 2, 2, 3, 3, 3]`
`unique = set(nums)`

`print(unique)`   # {1, 2, 3}



> [!CAUTION]
> ## Common mistakes
> 
> - **Sets are unordered** → you cannot index them
>   - ❌ `myset[0]`
> 
> - **Duplicates disappear automatically**
>   - `{1, 1, 1}` → `{1}`
> 
> - **Curly braces `{}` create a dictionary**, not a set
>   - Use set() for empty sets
> 
> - **Lists cannot be inside sets** (they are not hashable)
>   - ❌ * {[1,2,3]}*   
>   - ✔ * {(1,2,3)}*  (tuples are allowed)

## Summary:

> | **Concept** | **Meaning** |
> | :--- | :--- |
> | set | Unordered collection of unique items |
> | No duplicates | `{1,1,2}` → `{1,2}` |
> | No indexing | Cannot use `[0]` |
> | Fast membership | 	`"a" in set` |
> | Supports math operations | union, intersection, difference |