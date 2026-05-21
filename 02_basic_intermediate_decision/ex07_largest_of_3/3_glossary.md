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

# 2 - Integer

## What it is:  
An integer is a whole number, without decimals.

> [!CAUTION]
> - An integer cannot have decimals.
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

# 5 - `>=`

## What it is:  
`>=` means greater than or equal to.
It checks if a value is bigger or the same as another value.

> [!CAUTION]
> - **Compare only numbers** -> do not compare text with numbers.
> - **Convert input() first** -> input is text, so convert to `int()` or `float()` before using `>=`.
> - **Be clear about the boundary** -> `>=` includes equality; `>` does not.

**Example:**
`age = 18`
`print(age >= 18)`   # True


# 6 - `If`

## What it is:  
An **if** statement checks a condition.
If the condition is **true**, the code inside **runs**.
If the condition is **false**, Python **skips it**.

> [!CAUTION]
> - **Indentation is required** → the code inside the `if` must be indented.
> - **If without else does nothing when false** → the program continues normally.
> - **Condition must be valid** → avoid writing text or invalid expressions inside the `if`.
> - **B****e careful with spacing** → `if age >= 18`: works, but `ifage>=18`: is invalid.

**Example:**
`score = 90`
`if score >= 80:`
   `print("Great job")`

# 7 - `Else`

## What it is:  
The **else** block runs **when the if condition is false**.
It is the “backup” or “alternative” action.

  - **if** = what happens when the condition is true
  - **else** = what happens when the condition is false

> [!CAUTION]
> - **Else must come after an if** → you cannot use `else` alone.
> - **Indentation is required** → the code inside `else` must be indented.
> - **Else has no condition** → it runs automatically when the `if` is false.
> - **Avoid unnecessary else** → use it only when you really need an alternative action.
> - **Be careful with `input()`** → convert values before comparing in the `if`.

**Example:**
`age = 16`

`if age >= 18:`
    `print("You can enter")`
`else:`
    `print("You cannot enter")`

# 8 - Logical `and`

## What it is:  
The logical and operator checks two conditions at the same time.
It only returns True when both conditions are True.

  - **If one condition is False** → the whole expression becomes False
  - **If both are True** → the expression is True

> [!CAUTION]
> - **Else must come after an if** → you cannot use `else` alone.
> - **Indentation is required** → the code inside `else` must be indented.
> - **Else has no condition** → it runs automatically when the `if` is false.
> - **Avoid unnecessary else** → use it only when you really need an alternative action.
> - **Be careful with `input()`** → convert values before comparing in the `if`.

**Example:**
***Both conditions True***
`age = 20`
`if age >= 18 and age <= 30:`
    `print("Age is in the range")`

***Both conditions False***
`score = 85`
`if score >= 80 and score <= 100:`
    `print("Valid score")`

***Checking two requirements***
`temperature = 28`
`if temperature >= 20 and temperature <= 30:`
    `print("Comfortable temperature")`

# 9 - `Elif`

## What it is:  
**elif** means **“else if”**.
It is used when you want to check another condition after the first `if`.

  - `if` → first condition
  - `elif` → second condition (only checked if the first is false)
  - `else` → runs when all previous conditions are false

> [!CAUTION]
> - **Elif must come after an if** → you cannot start with `elif`.
> - **Order matters** → Python checks conditions from top to bottom.
> - **Only one block runs** → once one condition is true, the rest are skipped.
> - **Indentation is required** → keep the structure clean.

**Example:**
`score = 75`

`if score >= 90:`
    `print("Excellent")`
`elif score >= 70:`
    `print("Good")`
`else:`
    `print("Needs improvement")`