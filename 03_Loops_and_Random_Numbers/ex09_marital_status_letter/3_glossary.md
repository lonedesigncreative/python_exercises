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


# 3 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

> [!CAUTION]
> - `input` always returns text, even if the user types a number.
> - If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`



# 4 - Match

## What it is:  
The **match** statement is Python’s version of a **switch**.
It checks a value and compares it against several possible patterns.

Each **case** is one possible option.
When Python finds a matching case, it runs that block of code.

  - **match** → the value you want to test
  - **case** → the options you want to compare against
  - **case _** → the “default” (when nothing matches)

> [!CAUTION]
> - **match compares exact values** → `"3"` is not the same as `3`.
> - **case _ is the default** → use it for “anything else”.
> - **match works top to bottom** → the first matching case wins.
> - **Spacing and indentation matter** → keep everything aligned.
> - **Use match only in Python 3.10+** → older versions do not support it.
> - **Avoid unnecessary cases** → keep your structure clean and simple.

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

# 5 - Upper()

## What it is:  
`upper` is a **string method** in Python that converts all letters in a string to **uppercase**.

>> “Turn all characters into CAPITAL LETTERS.””

> [!WARNING]
> - It **does not change numbers or symbols**, only letters.

> [!NOTE]
> **Basic Structure:**
> `string.upper()`


> [!TIP]
> **## Why `upper` is useful**
> - Normalize text
> - Case‑insensitive comparisons
> - Formatting output
> - Preparing data for search
>
> **Example:**
> `if user_input.upper() == "YES":`
> `print("Confirmed")`


> [!IMPORTANT]
> **## **Method** vs **lower****
> 
> | **Class** | **What it does** |
> | :--- | :--- | :--- |
> | upper | Converts to UPPERCASE |
> | lower | Converts to lowercase |



> [!CAUTION]
> - **Strings are immutable** → `upper()` returns a new string
> - **Does not change numbers** → `"123".upper()` stays `"123"`
> - **Does not change special character**s → `"@#%".upper()` stays `"@#%"`
> - **Useful with `.strip()` and .`replace()`** for cleaning text



**Example:**
*Example 1 - Simple usage*
`text = "hello"`
`print(text.upper())`   # HELLO


*Example 2 - Mixed text*
`print("Python 3.10!".upper())`   # PYTHON 3.10!


*Example 3 - Using with variables*
`name = "Python"`
`print(name.upper())`   # PYTHON