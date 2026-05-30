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


# 3 - `==`

## What it is:  
The `==` operator checks if two values are exactly the same.
It returns True when the values are equal and False when they are different.

  - `==` → compares values
  - It does not assign values (that’s =)

> [!CAUTION]
> - **== is not =**
>   - = assigns a value; == compares values.
> - **Compare compatible types**
>     - avoid comparing numbers with text ("10" == 10 is False).
> - **Becareful with `input()`**
>     - input returns text, so convert before comparing (`int(input())`).
> - **Case sensitivity matters**
>     - `"Ana" == "ana"` is False because the letters are different.
> - **Spacing matters** —
>   - write `a == 10`, not `a==10abc`.

**Example:**
`age = 18`
`print(age == 18)`   # True

`score = 50`
`print(score == 60)` # False


# 4 - `If`

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


# 4 - `Else`

## What it is:  
The **else** block runs **when the if condition is false**.
It is the “backup” or “alternative” action.

  - **if** = what happens when the condition is true
  - **else** = what happens when the condition is false

> [!CAUTION]
> - **Else must come after an if** → you cannot use `else` alone.
> - **Indentation is required** → the code inside `else` must be indented.
> - **Else has no condition** → it runs automatically when the `if` is false.
> - **Avoid unnecessary else** → use it only when you really need an alternative action.
- **Be careful with `input()`** → convert values before comparing in the `if`.

**Example:**
`age = 16`

`if age >= 18:`
    `print("You can enter")`
`else:`
    `print("You cannot enter")`


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



# 6 - return

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


# 7 - or

## What it is:  
`or` is a **logical operator** in Python.

>> “If **at least ONE condition is true**, the result is true.””

It is used inside **if statements**, **while loops**, and any expression that checks conditions.


> [!NOTE]
> **## Truth table for `or`**
> 
> | **A** | **B** | **A or B** |
> | :--- | :--- | :--- |
> | False | False | False |
> | True | False | True |
> | False | True | True |
> | True | True | True |
>
> **So:**
> 
> Only **False or False** gives **False**
> Everything else gives **True**


> [!IMPORTANT]
> **## Non‑boolean behavior**
> 
> Python’s `or` does **not** always return True/False.
> It returns the **first truthy value**.
>
> **Examples:**
> `print("" or "Hello")`     # Hello
> `print(0 or 5)`            # 5
> `print([] or [1, 2])`      # [1, 2]
>
> - This is extremely useful in **default values**.


### Using `or` for default values

- `name = user_input or "Guest"`
  
  - If `user_input` is empty, None, or False → `"Guest"` is used.


> [!CAUTION]
> ## Common mistakes:
> - **Do NOT use `or` to compare multiple values incorrectly**
>   - **Wrong:**
>     - `if color == "blue" or "red":`
>   - This always evaluates to True.
>     - Correct:
>     - if color == "blue" or color == "red":
>
> - **Remember that `or` returns values, not booleans**, when used outside conditions
> - **Be careful with empty strings, 0, and None** → they are considered False in Python


**Example:**
*Example 1 - Simple condition*
`age = 16`
`has_permission = True`

`if age >= 18 or has_permission:`
    `print("You can enter")`

> [!IMPORTANT]
> - Even though `age >= 18` is *False*,
> - `has_permission` is *True* → so the whole expression is **True**.

*Example 2 - Checking multiple possibilities*
`color = "blue"`

`if color == "blue" or color == "red":`
    `print("Valid color")`

*Example 3 - Using or with booleans*
`a = True`
`b = False`

`print(a or b)`   # True


# Summary

| **Concept** | **Meaning** |
| :--- | :--- |
| or | True if at least one condition is true |
| Returns first truthy value | 	`"Hello" or ""` → `"Hello"` |
| Used in conditions | `if a or b:` |
| Common in default values | `x = value or default` |