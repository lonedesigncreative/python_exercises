# 1 - Print

## What it is:  
`print` is a command that shows something on the screen.

> [!CAUTION]
- Always use parentheses → print("Hello")
- Text must be inside quotes `" "`
- Missing quotes or parentheses causes an error.

**Example:**
`print("Python!")`

This will display:
- *Python!*

# 2 - Integer

## What it is:  
An integer is a whole number, without decimals.

> [!CAUTION]
- An integer cannot have decimals.
- **Do NOT use a comma** → Python will think it’s two values.

**Example:**
`age = 25`

# 3 - Text (in Python called string)

## What it is:  
Text inside quotes `" "`.

> [!CAUTION]
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

# 4 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

> [!CAUTION]
- `input` always returns text, even if the user types a number.
- If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`


# 7 - Match

## What it is:  
The **match** statement is Python’s version of a **switch**.
It checks a value and compares it against several possible patterns.

Each **case** is one possible option.
When Python finds a matching case, it runs that block of code.

  - **match** → the value you want to test
  - **case** → the options you want to compare against
  - **case _** → the “default” (when nothing matches)

:warning: **Warning:**
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