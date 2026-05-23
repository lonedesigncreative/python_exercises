# 1 - Print

## What it is:  
`print` is a command that shows something on the screen.

> [!CAUTION]
> - Always use parentheses → print("Hello")
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


# 2 - `!=`

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

# 4 - Integer

## What it is:  
An integer is a whole number, without decimals.

> [!CAUTION]
>- An integer cannot have decimals.
> - **Do NOT use a comma** → Python will think it’s two values.

**Example:**
`age = 25`

# 2 - Input

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

> [!CAUTION] 
> “Keep doing this while the condition is true.”

> [!TIP]
>  - When the condition becomes **False**, the loop stops.

> [!IMPORTANT]
## How it works:
- The condition is checked first.
- If True, the loop runs.
- If False, the loop stops.

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