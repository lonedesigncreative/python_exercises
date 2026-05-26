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


# 2 - Integer

## What it is:  
An integer is a whole number, without decimals.

> [!CAUTION]
>- An integer cannot have decimals.
> - **Do NOT use a comma** → Python will think it’s two values.

**Example:**
`age = 25`


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


# 6 - { }
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


# 7 - While (loop)
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



# 8 - Break

## What it is:  
The `break` statement is used to **stop a loop immediately**.
When Python finds a `break`, it** exits the loop**, even if the loop condition is still True.

> [!NOTE]
> **It works in both:**
> **`for` loops**
> **`while` loops**

>> “Stop the loop right now.”

> [!CAUTION]
> - **Use break only when necessary** → too many breaks make code harder to read.
> - **Break exits only the current loop** → not nested loops above it.
> - **Avoid infinite loops** → if using `while True`, make sure a break exists.
> - **Break stops immediately** → code after break inside the loop will not run.
> - **Use continue for skipping** → not break.

> [!WARNING]
> **## What break does NOT do**
> It does **not** skip to the next iteration (that is **continue**).
> It does **not** restart the loop.
> It does **not** exit the entire program — only the loop.

**Example:**
  - ***Example 1 - Stop a `for` loop early***
`for i in range(1, 10):`
    `if i == 5:`
        `break`
    `print(i)`

> **Output:**
> *`1, 2, 3, 4`*
> (The loop stops when i reaches 5.)

  - ***Example 2 - Stop a `while` loop when a condition happens***
`i = 1`

`while i <= 10:`
    `if i == 7:`
        `break`
    `print(i)`
    `i += 1`

  - ***Example 3 - Stop asking for input when the user types “exit”***
`while True:`
    `text = input("Type something: ")`
    `if text == "exit":`
        `break`
    `print("You typed:", text)`


# 9 - True

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


# 10 - try

## What it is:  
`try` is part of Python’s **error‑handling system**.

>> “Try to run this code, and if something goes wrong, handle the error instead of crashing.”

- `try` is always used together with **except**, and sometimes **else** and **finally**.


> [!NOTE]
> ### Basic structure:
>    - `try:`
>    - code that might cause an error
>    - `except:`
>    - code that runs if an error happens


> [!IMPORTANT]
> **## What each part does**
> - **try** → runs code that might fail
> - **except** → handles the error
> - **else** → runs if no error happens
> - **finally** → always runs (cleanup, closing files, etc.)


> [!TIP]
> **## Why try/except is useful**
> - Prevents your program from crashing
> - Lets you show friendly error messages
> - Helps validate user input
> - Useful for files, conversions, APIs, databases, etc.
>
> **Example:**
>`try:`
>   `age = int(input("Enter your age: "))`
>`except ValueError:`
>    `print("Please enter a number")`
> 

> [!CAUTION]
> - **Don’t use bare except** → always catch specific errors when possible
> - **Code inside try should be minimal** → easier to debug
> - **finally always runs** → even if there is an error
> - **except must match the error** → wrong type won’t catch
> - **Avoid hiding bugs** → don’t catch everything blindly

**Example:**
*Example 1 - Basic try/except*
`try:`
    `x = 10 / 0`
`except:`
    `print("An error happened")`

**Output:**
- `An error happened`

*Example 2 - Catch a specific error*
`try:`
    `number = int("abc")`
`except ValueError:`
    `print("Not a valid number")`

*Example 3 - Using else (runs only if no error)*
`try:`
    x = 5 + 5`
`except:`
    `print("Error")`
`else:`
    `print("Everything worked")`

*Example 4 - Using finally (always runs)*
`try:`
    `file = open("data.txt")`
`except FileNotFoundError:`
    `print("File not found")`
`finally:`
    `print("Done")`


# 11 - ValueError

## When it happens:  
A **ValueError** happens when:

>> “The value you gave is the right type, but it is an invalid value for that operation.”

In other words:
- Python **expected** a certain **kind of value**
- You gave something that **cannot be used**, even though the type is correct


> [!NOTE]
> ### Basic structure:
>    - `try:`
>    - code that might cause an error
>    - `except:`
>    - code that runs if an error happens


> [!IMPORTANT]
> **## ValueError vs TypeError**
> 
> | **ValueError** | **Meaning** |
> | :--- | :--- | :--- |
> | ValueError | Type is correct, value is invalid |
> | TypeError | Type is wrong |
>
> **Example:**
> `int("abc") `    # ValueError (string OK, value invalid)
> `int(["abc"])`   # TypeError (list is wrong type)


> [!TIP]
> **## How to handle a ValueError**
> - Use try/except:
>
> `try:`
>   `age = int(input("Enter your age: "))`
> `except ValueError:`
>    `print("Please enter a number")`
> 


> [!CAUTION]
> - **Always validate user input** → especially numbers
> - **Use try/except** to avoid program crashes
> - **Check if values exist before removing**
> - **Statistics functions need valid data**
> - **Conversions must match the format**


> [!WARNING]
> **## When ValueError happens**
> - Wrong number format
> - Invalid value for a function
> - Removing something that doesn’t exist
> - Empty lists in statistics
> - Wrong format in date/time parsing
> - Wrong format in type conversions


**Example that cause ValueError:**
*Example 1 - Converting text to number*
`int("abc")`   # ❌ ValueError

> Because `"abc"` is a string, but **not a valid number**.

*Example 2 - Converting float text to int*
`int("3.5")`   # ❌ ValueError

> `"3.5"` is a number, but **not an integer**.

*Example 3 - Removing an item that does not exist*
`numbers = [1, 2, 3]`
`numbers.remove(5)`   # ❌ ValueError

*Example 4 - Using invalid values in functions*
`from math import sqrt`
`sqrt(-1)`   # ❌ ValueError

> `sqrt()` cannot calculate the square root of a negative number.

*Example 5 - Using statistics functions incorrectly*
`from statistics import mean`
`mean([])`   # ❌ ValueError (empty list)
