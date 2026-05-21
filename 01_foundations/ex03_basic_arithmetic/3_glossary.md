# 1 - Addition (`+`)

## What it does:  
Adds two values.

## :warning: **Warning:**
- Only works correctly with numbers.
- If you add text, Python will join the words instead of doing math.

**Example:**
`total = 5 + 3`


# 2 - Subtraction (`−`)

## What it does:  
Subtracts one value from another.

## :warning: **Warning:**
- You cannot subtract text.
- You cannot subtract using commas (European style). Use dots.

**Example:**
`difference = 10 - 4`


# 3 - Multiplication (`*`)

## What it does:  
Multiplies two values.

## :warning: **Warning:**
- Multiplying text repeats it.

**Example:**
`product = 6 * 2`


# 4 - Division (`/`)

## What it does:  
Divides one value by another.
Always returns a decimal (float).

## :warning: **Warning:**
- Division always returns a decimal (float).
- Be careful with dividing by zero - it causes an error.

**Example:**
`result = 10 / 4   # 2.5`


# 5 - Remainder (`%`)
Also called modulo.

## :warning: **Warning:**
- Only works with numbers.
- If you use text, Python gives an error.
- Be careful: % does not give the result of the division - only the remainder.


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

# 6 - Print

## What it is:  
`print` is a command that shows something on the screen.

## :warning: **Warning:**
- **Always use parentheses** → print("Hello")
- Text must be inside quotes `" "`
- Missing quotes or parentheses causes an error.

**Example:**
`print("Hello!")`

This will display:
- *Hello!*

# 7 - Text (in Python called string)

## What it is:  
Text inside quotes `" "`.

## :warning: **Warning:**
- Text must always be inside quotes.
- If you put numbers inside quotes, they become text, not numbers.

**Example:**
`name = "LoneDesign"`

# Summary

| **Concept** | **Meaning** | **Example** |
| :--- | :--- | :--- |
| print | hows something on the screen | print("Hi") |
| integer | Whole number | 10 |
| decimal (float) | Number with decimal | 2.5 |
| text (string) | Words inside quotes | "Hello" |


# 8 - f-string (f"")

## What it is:
An f‑string is a special type of text that allows you to insert variables inside the text.

## :warning: **Warning:**
- Don’t forget the **f** before the quotes.
- Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`

# 9 - { }

## What it means:
The `{ }` are used to show the value of a variable inside the text.

## :warning: **Warning:**
- Inside `{ }` you must put a **variable** or an **expression**.
- If you put text without quotes, it gives an error.
- If you put quotes inside `{ }`, it becomes text again.