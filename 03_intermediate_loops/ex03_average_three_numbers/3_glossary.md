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

# 2 - Multiplication (`*`)

## What it does:  
Multiplies two values.

> [!CAUTION]
> - Multiplying text repeats it.

**Example:**
`product = 6 * 2`

# 3 - Decimal (in Python called float)

## What it is:  
A decimal number - a number with a dot (.).

> [!CAUTION]
> - Python uses a dot, not a comma.
> - 3.5 is correct, 3,5 is wrong.

**Example:**
`price = 3.50`


**Example:**
`age = 25`

# 4 - Text (in Python called string)

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


# 5 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

> [!CAUTION]
> - `input` always returns text, even if the user types a number.
> - If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`


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

# 8 - Addition (`+`)

## What it does:  
Adds two values.

> [!CAUTION]
> - Only works correctly with numbers.
> - If you add text, Python will join the words instead of doing math.

**Example:**
`total = 5 + 3`


# 9 - Division (`/`)

## What it does:  
Divides one value by another.
Always returns a decimal (float).

> [!CAUTION]
> - Division always returns a decimal (float).
> - Be careful with dividing by zero - it causes an error.

**Example:**
`result = 10 / 4   # 2.5`


# 10 - `round()`

## What it is:  
The round() function rounds a number to the number of decimal places you choose.

  - **round(number)** → rounds to the nearest whole number
  - **round(number, decimals)** → rounds to the number of decimals you specify

> [!CAUTION]
> - **Rounding is not always exact** → floats can have tiny precision errors.
> - **`round()` does not format output** → it changes the number, but does not force decimals to appear.
> - **Use `.2f` for formatting** → if you want fixed decimal places, use formatting instead of round.
> - **Be careful with `input()`** → convert to float before rounding.

**Example:**
`print(round(3.6))`        # 4
`print(round(3.14159, 2))` # 3.14
`print(round(7.89, 1))`    # 7.9


# 11 - For (loop)
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
*1. Loop from 1 to 5*
`for i in range(1, 6):`
    `print(i)`

*2. Loop through a list*
`fruits = ["apple", "banana", "orange"]`

`for fruit in fruits:`
    `print(fruit)`

*3. Loop through each letter in a string*
`for letter in "Python":`
    `print(letter)`

*4. Sum numbers from 1 to 10*
`total = 0`

`for n in range(1, 11):`
    `total += n`

`print(total)`

> [!IMPORTANT]
> #### How the `range()` works:
> The function **range** creates a sequence of numbers.
>   - `range(5)` → 0,1,2,3,4
>   - `range(1, 5)` → 1,2,3,4
>   - `range(1, 10, 2)` → 1,3,5,7,9 (step of 2)