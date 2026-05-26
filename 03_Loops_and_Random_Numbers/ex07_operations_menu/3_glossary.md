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


# 3 - Integer

## What it is:  
An integer is a whole number, without decimals.

> [!CAUTION]
>- An integer cannot have decimals.
> - **Do NOT use a comma** → Python will think it’s two values.

**Example:**
`age = 25`

# 4 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

> [!CAUTION]
> - `input` always returns text, even if the user types a number.
> - If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`


# 5 - While (loop)
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

# 6 - Match

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

# 7 - Break

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

# 8 - True

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