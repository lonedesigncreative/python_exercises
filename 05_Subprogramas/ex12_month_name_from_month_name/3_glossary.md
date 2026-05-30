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


# 3 - <=

## What it is:
`<=` is a `comparison operator` in Python.

>> “Less than or equal to.”

It compares two values and returns **True** or **False**.

> [!NOTE]
> ## Basic meaning:
> 
> `a <= b`
> 
> This expression is **True** when:
> - `a` is less than `b`, **OR**
> - `a` is equal to `b`
> Otherwise, it is **False**.



> [!IMPORTANT]
> - Works with **numbers**, **strings**, and other comparable types
> - Strings are compared **alphabetically**
> - You cannot compare incompatible types
>   - `"a" <= 3` → error


## Comparison table

| **Expression** | **Result** |
| :--- | :--- |
| 3 <= 5 | True |
| 5 <= 5 | True |
| 7 <= 2 | False |
| "a" <= "b" | True (alphabetical order) |


> [!CAUTION]
> ## Common mistakes
> - **Confusing `<=` with `<`**
>   - `<` → strictly less
>   - `<=` → less OR equal
>
> - **Comparing different types  **
>   - ❌ `"10" <= 5 ` 
>   - ✔ Convert first: `int("10") <= 5`
> 
> - **Using `<=` with lists** 
> *Lists cannot be compared this way.*


> **Example:**
*Example 1 - Basic comparison*
`print(5 <= 10)`   # True
`print(10 <= 10)`  # True
`print(12 <= 10)`  # False

*Example 2 - Using inside an if*
`age = 17`

`if age <= 18:`
    `print("Minor")`

*Example 3 - With variables*
`x = 3`
`y = 7`

`if x + 2 <= y:`
    `print("Condition is true")`


# Summary

| **Operator** | **Meaning** | **Example** |
| :--- | :--- | :--- |
| <= | Less than or equal to | `x <= 10` |
| < | Strictly less than | `x < 10` |
| >= | Greater or equal | `x >= 10` |
| > | Strictly greater | `x > 10` |


# 4 - Subtraction (`−`)

## What it does:  
Subtracts one value from another.

> [!CAUTION]
> - You cannot subtract text.
> - You cannot subtract using commas (European style). Use dots.

**Example:**
`difference = 10 - 4`


# 5 - [ ]

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


# 6 - `If`

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


# 5 - def

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


# 7 - return

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