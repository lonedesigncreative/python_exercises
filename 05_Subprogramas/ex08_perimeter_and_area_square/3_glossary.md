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

# 2 - Multiplication (`*`)

## What it does:  
Multiplies two values.

> [!CAUTION]
> - Multiplying text repeats it.

**Example:**
`product = 6 * 2`


# 3 - def

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


# 4 - return

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