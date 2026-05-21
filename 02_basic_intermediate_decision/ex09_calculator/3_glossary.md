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

# 2 - Decimal (in Python called float)

## What it is:  
A decimal number - a number with a dot (.).

- Python uses a dot, not a comma.
- 3.5 is correct, 3,5 is wrong.

**Example:**
`price = 3.50`

# 3 - Text (in Python called string)

## What it is:  
Text inside quotes `" "`.

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

# 4 - Addition (`+`)

## What it does:  
Adds two values.

- Only works correctly with numbers.
- If you add text, Python will join the words instead of doing math.

**Example:**
`total = 5 + 3`

# 5 - Subtraction (`−`)

## What it does:  
Subtracts one value from another.

- You cannot subtract text.
- You cannot subtract using commas (European style). Use dots.

**Example:**
`difference = 10 - 4`

# 6 - Multiplication (`*`)

## What it does:  
Multiplies two values.

- Multiplying text repeats it.

**Example:**
`product = 6 * 2`


# 7 - Division (`/`)

## What it does:  
Divides one value by another.
Always returns a decimal (float).

- Division always returns a decimal (float).
- Be careful with dividing by zero - it causes an error.

**Example:**
`result = 10 / 4   # 2.5`


# 8 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

- `input` always returns text, even if the user types a number.
- If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`

# 9 - f-string (f"")

## What it is:
An f string is a special type of text that allows you to insert variables inside the text.

- Don’t forget the **f** before the quotes.
- Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`

# 10 - { }
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
| { } | Shows the variable’s value inside the f string | `{age}` |

# 11 - Match

## What it is:  
The **match** statement is Python’s version of a **switch**.
It checks a value and compares it against several possible patterns.

Each **case** is one possible option.
When Python finds a matching case, it runs that block of code.

  - **match** → the value you want to test
  - **case** → the options you want to compare against
  - **case _** → the “default” (when nothing matches)

- **match compares exact values** → `"3"` is not the same as `3`.
- **case _ is the default** → use it for “anything else”.
- **match works top to bottom** → the first matching case wins.
- **Spacing and indentation matter** → keep everything aligned.
- **Use match only in Python 3.10+** → older versions do not support it.
- **Avoid unnecessary cases** → keep your structure clean and simple.

**Example:**
  - ***Example 1: Months***
`month = 3`

`match month:`
    `case 1:`
        `print("January")`
    `case 2:`
        `print("February")`
    `case 3:`
        `print("March")`
    `case _:`
        `print("Invalid month")`

  - ***Example 2: Civil status***
`status = "S"`

`match status:`
    `case "S":`
        `print("Single")`
    `case "C":`
        `print("Married")`
    `case "V":`
        `print("Widowed")`
    `case _:`
        `print("Invalid option")`

  - ***Example 3 : Number type***
`number = 0`

`match number:`
    `case 0:`
        `print("Zero")`
    `case 1 | 2 | 3:`
        `print("Small number")`
    `case _:`
        `print("Other number")`