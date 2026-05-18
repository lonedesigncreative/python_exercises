# 1 - Print

## What it is:  
`print` is a command that shows something on the screen.

- Always use parentheses → print("Hello")
- Text must be inside quotes `" "`
- Missing quotes or parentheses causes an error.

**Example:**
`print("Python!")`

This will display:
- *Python!*

# 2 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

- `input` always returns text, even if the user types a number.
- If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`

# 3 - Float

## What it is:
A `float` is a decimal number in Python -> a number with a **dot** instead of a comma.

- **Floats use a dot, not a comma** -> Python only accepts decimals with a dot.
- **Floats can lose precision** -> some decimal values are not stored exactly.
- **`input()` returns text, not float** -> you must convert the input before using it as a decimal.
- Converting float to int removes decimals

**Example:**
`price = 3.5`

- It is used when you need decimals, like money, measurements, or averages.

# 4 - Multiplication (`*`)

## What it does:  
Multiplies two values.

- Multiplying text repeats it.

**Example:**
`product = 6 * 2`

# 5 - f-string (f"")

## What it is:
An f‑string is a special type of text that allows you to insert variables inside the text.

- Don’t forget the **f** before the quotes.
- Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`

# 6 - { }

## What it means:
The `{ }` are used to show the value of a variable inside the text.

- Inside `{ }` you must put a **variable** or an **expression**.
- If you put text without quotes, it gives an error.
- If you put quotes inside `{ }`, it becomes text again.

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