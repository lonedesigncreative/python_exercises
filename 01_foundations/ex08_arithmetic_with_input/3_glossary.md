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

# 2 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

> [!CAUTION]
> - `input` always returns text, even if the user types a number.
> - If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`

# 3 - Integer

## What it is:  
An integer is a whole number, without decimals.

> [!CAUTION]
> - An integer cannot have decimals.
> - **Do NOT use a comma** → Python will think it’s two values.

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


# 5 - f-string (f"")

## What it is:
An f‑string is a special type of text that allows you to insert variables inside the text.

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
| { } | Shows the variable’s value inside the f‑string | `{age}` |

# 7 - Addition (`+`)

## What it does:  
Adds two values.

> [!CAUTION]
> - Only works correctly with numbers.
> - If you add text, Python will join the words instead of doing math.

**Example:**
`total = 5 + 3`


# 8 - Subtraction (`−`)

## What it does:  
Subtracts one value from another.

> [!CAUTION]
> - You cannot subtract text.
> - You cannot subtract using commas (European style). Use dots.

**Example:**
`difference = 10 - 4`


# 9 - Multiplication (`*`)

## What it does:  
Multiplies two values.

> [!CAUTION]
> - Multiplying text repeats it.

**Example:**
`product = 6 * 2`


# 10 - Division (`/`)

## What it does:  
Divides one value by another.
Always returns a decimal (float).

> [!CAUTION]
> - Division always returns a decimal (float).
> - Be careful with dividing by zero - it causes an error.

**Example:**
`result = 10 / 4   # 2.5`


# 11 - Remainder (`%`)
Also called modulo.

> [!CAUTION]
> - Only works with numbers.
> - If you use text, Python gives an error.
> - **Be careful:** % does not give the result of the division - only the remainder.


## What it does:  
Returns the remainder of a division.

**Example:**
`rest = 10 % 3`   # remainder is 1


# Summary

| **Operator** | **Meaning** | **Example** | **Result** |
| :---: | :--- | :---: | :---: |
| + | Addition | 5 + 3 | 8 |
| - | Subtraction | 10 - 4 | 6 |
| * | Multiplication | 6 * 2 | 12 |
| / | Division | 10 / 4 | 2.5 |
| % | Remainder | 10 % 3 | 1 |