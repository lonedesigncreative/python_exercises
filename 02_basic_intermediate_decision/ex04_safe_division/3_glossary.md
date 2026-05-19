# 1 - Print

## What it is:  
`print` is a command that shows something on the screen.

- **Always use parentheses** → print("Hello")
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

# 4 - Text (in Python called string)

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


# 7 - Division (`/`)

## What it does:  
Divides one value by another.
Always returns a decimal (float).

- Division always returns a decimal (float).
- Be careful with dividing by zero - it causes an error.

**Example:**
`result = 10 / 4   # 2.5`

# 8 - `If`

## What it is:  
An **if** statement checks a condition.
If the condition is **true**, the code inside **runs**.
If the condition is **false**, Python **skips it**.

- **Indentation is required** → the code inside the `if` must be indented.
- **If without else does nothing when false** → the program continues normally.
- **Condition must be valid** → avoid writing text or invalid expressions inside the `if`.
- **B****e careful with spacing** → `if age >= 18`: works, but `ifage>=18`: is invalid.

**Example:**
`score = 90`
`if score >= 80:`
   `print("Great job")`

# 9 - `Else`

## What it is:  
The **else** block runs **when the if condition is false**.
It is the “backup” or “alternative” action.

**if** = what happens when the condition is true
**else** = what happens when the condition is false

- **Else must come after an if** → you cannot use `else` alone.
- **Indentation is required** → the code inside `else` must be indented.
- **Else has no condition** → it runs automatically when the `if` is false.
- **Avoid unnecessary else** → use it only when you really need an alternative action.
- **Be careful with `input()`** → convert values before comparing in the `if`.

**Example:**
`age = 16`

`if age >= 18:`
    `print("You can enter")`
`else:`
    `print("You cannot enter")`

# 10 - `round()`

## What it is:  
The round() function rounds a number to the number of decimal places you choose.

  - **round(number)** → rounds to the nearest whole number
  - **round(number, decimals)** → rounds to the number of decimals you specify


- **Rounding is not always exact** → floats can have tiny precision errors.
- **`round()` does not format output** → it changes the number, but does not force decimals to appear.
- **Use `.2f` for formatting** → if you want fixed decimal places, use formatting instead of round.
- **Be careful with `input()`** → convert to float before rounding.

**Example:**
`print(round(3.6))`        # 4
`print(round(3.14159, 2))` # 3.14
`print(round(7.89, 1))`    # 7.9

# 11 - `>`

## What it is:  
The `>` operator means **greater than**.
It checks if a value is **strictly bigger** than another value.

  - If the left value is bigger → True
  - If it is equal or smaller → False

- **> is different from `>=`** → `>` does NOT include equality.
- **Compare only numbers** → avoid comparing text with numbers.
- **Convert `input()` first** → input is text, so convert before comparing.
- **Spacing matters** → write `a > 10`, not `a>10something`.

**Example:**
`age = 20`
`print(age > 18)`   # True

`score = 50`
`print(score > 60)` # False
