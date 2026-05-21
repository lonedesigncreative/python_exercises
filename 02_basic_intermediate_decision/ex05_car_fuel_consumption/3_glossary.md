# 1 - Print

## What it is:  
`print` is a command that shows something on the screen.

> [!CAUTION]
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

> [!CAUTION]
- `input` always returns text, even if the user types a number.
- If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`

# 3 - Float

## What it is:
A `float` is a decimal number in Python -> a number with a **dot** instead of a comma.

> [!CAUTION]
- **Floats use a dot, not a comma** → Python only accepts decimals with a dot.
- **Floats can lose precision** → some decimal values are not stored exactly.
- **`input()` returns text, not float** → you must convert the input before using it as a decimal.
- Converting float to int removes decimals

**Example:**
`price = 3.5`

- It is used when you need decimals, like money, measurements, or averages.

# 4 - Text (in Python called string)

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

# 5 - `<=`

## What it is:  
The `<=`  operator means **less than or equal to**.
It checks if a value is **smaller** or **the same** as another value.

> [!CAUTION]
- **`<=` includes equality** → different from `<`, which does not.
- **Compare only numbers** → avoid comparing text with numbers.
- **Convert `input()` first** → input is text, so convert before comparing.
- **Spacing matters** → write `a <= 10`, not `a<=10abc`.

**Example:**
`age = 12`
`print(age <= 12)`   # True

`temperature = 18`
`print(temperature <= 15)`   # False


# 6 - `If`

## What it is:  
An **if** statement checks a condition.
If the condition is **true**, the code inside **runs**.
If the condition is **false**, Python **skips it**.

> [!CAUTION]
- **Indentation is required** → the code inside the `if` must be indented.
- **If without else does nothing when false** → the program continues normally.
- **Condition must be valid** → avoid writing text or invalid expressions inside the `if`.
- **B****e careful with spacing** → `if age >= 18`: works, but `ifage>=18`: is invalid.

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

# 8 - `Elif`

## What it is:  
**elif** means **“else if”**.
It is used when you want to check another condition after the first `if`.

  - `if` → first condition
  - `elif` → second condition (only checked if the first is false)
  - `else` → runs when all previous conditions are false

> [!CAUTION]
- **Elif must come after an if** → you cannot start with `elif`.
- **Order matters** → Python checks conditions from top to bottom.
- **Only one block runs** → once one condition is true, the rest are skipped.
- **Indentation is required** → keep the structure clean.

**Example:**
`score = 75`

`if score >= 90:`
    `print("Excellent")`
`elif score >= 70:`
    `print("Good")`
`else:`
    `print("Needs improvement")`

# 9 - f-string (f"")

## What it is:
An f‑string is a special type of text that allows you to insert variables inside the text.

> [!CAUTION]
- Don’t forget the **f** before the quotes.
- Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`

# 10 - { }

## What it means:
The `{ }` are used to show the value of a variable inside the text.

> [!CAUTION]
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


# 11 - Division (`/`)

## What it does:  
Divides one value by another.
Always returns a decimal (float).

> [!CAUTION]
- Division always returns a decimal (float).
- Be careful with dividing by zero - it causes an error.

# 12 - Multiplication (`*`)

## What it does:  
Multiplies two values.

- Multiplying text repeats it.

**Example:**
`product = 6 * 2`

# 13 - .2f

## What it means:
`.2f` is a formatting code that tells Python to show a number with exactly **2 decimal places**.
**The .2 means:** keep 2 decimals
**The f means:** format as a float (decimal number)
It is typically used within an f-string.

> [!CAUTION]
- **Use only inside f‑strings** → the `._f` format only works inside `{ }` in an f‑string.
- **Works only with numbers** → you can only format integers or floats.
- **It rounds the value** → the number is rounded to the number of decimals you choose.
- **The dot defines decimal places** → `.1f`, `.2f`, `.3f` decide how many decimals appear.
- **Always shows fixed decimals** → even if the number has no decimals, it will display the exact amount you set.

**Example:**
`price = 3.456`
`print(f"{price:.2f}")`

# Summary

| **Format** | **Meaning** | **What it does** | **Example** | **Output**
| :---: | :--- | :---: | :---: | :---: |
| .0f | 0 decimal places | Rounds and shows no decimals | `f"{3.456:.0f}"` | 3
| .1f | 1 decimal place | Shows exactly 1 decimal | `f"{3.456:.1f}"` | 3.5
| .2f | 2 decimal places | Shows exactly 2 decimals (most common) | `f"{3.456:.4f}"` | 3.4560
| .3f | 3 decimal places | Shows exactly 3 decimals | `f"{3.456:.3f}"` | 3.456
| .4f | 4 decimal places | Shows exactly 4 decimals | `f"{3.456:.4f}"` | 3.4560