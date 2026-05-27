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

# 2 - Integer

## What it is:  
An integer is a whole number, without decimals.

> [!CAUTION]
> - An integer cannot have decimals.
> - **Do NOT use a comma** → Python will think it’s two values.

**Example:**
`age = 25`


# 3 - Decimal (in Python called float)

## What it is:  
A decimal number - a number with a dot (.).

> [!CAUTION]
> - Python uses a dot, not a comma.
> - 3.5 is correct, 3,5 is wrong.

**Example:**
`price = 3.50`


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


# 5 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

> [!CAUTION]
> - `input` always returns text, even if the user types a number.
> - If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`


# 6 - Division (`/`)

## What it does:  
Divides one value by another.
Always returns a decimal (float).

> [!CAUTION]
> - Division always returns a decimal (float).
> - Be careful with dividing by zero - it causes an error.

**Example:**
`result = 10 / 4   # 2.5`


# 7 - `<`

## What it is:  
The `<` operator means **less than**.
It checks if a value is **strictly smaller** than another value.

  - If the left value is smaller → True
  - If it is equal or bigger → False

> [!CAUTION]
> - **< is different from <=** → `<` does NOT include equality.
> - **Compare only numbers** → avoid comparing text with numbers.
> - **Convert input() first** → input is text, so convert before comparing.
> - **Spacing matters** → write `a < 10`, not `a<10abc`.

**Example:**
`age = 15`
`print(age < 18)`   # True

`score = 70`
`print(score < 50)` # False


# 8 - `<=`

## What it is:  
The `<=`  operator means **less than or equal to**.
It checks if a value is **smaller** or **the same** as another value.

> [!CAUTION]
> - **`<=` includes equality** → different from `<`, which does not.
> - **Compare only numbers** → avoid comparing text with numbers.
> - **Convert `input()` first** → input is text, so convert before comparing.
> - **Spacing matters** → write `a <= 10`, not `a<=10abc`.

**Example:**
`age = 12`
`print(age <= 12)`   # True

`temperature = 18`
`print(temperature <= 15)`   # False


# 9 - `**`

## In Python:  
In Python, `**` has **two completely different meanings**, depending on where it is used:

  1. Exponentiation operator → mathematical power
  2. Dictionary unpacking → expand key value pairs

## 1. `**` as exponentiation (power)
This is the most common use.

>> “Raise a number to a power.”

**Example:**
`print(2 ** 3)`   # 8

> [!TIP]
> **Meaning:**
> 2³ = 8
> base = 2
> exponent = 3

**More examples:**
`5 ** 2`   # 25
`9 ** 0.5` # 3 (square root)
`3 ** 3`   # 27


## 2. `**` for dictionary unpacking

>> “Expand a dictionary into key=value pairs.”

> [!NOTE]
> Used inside:
> - function calls
> - dictionary creation

**Example: passing dictionary values to a function**
`def greet(name, age):`
    `print(name, age)`

`data = {"name": "Ana", "age": 25}`

`greet(**data)`

*This is the same as:*
`greet(name="Ana", age=25)`

**Example: merging dictionaries**
`a = {"x": 1}`
`b = {"y": 2}`

`c = {**a, **b}`
`print(c)`   # {'x': 1, 'y': 2}


> [!CAUTION]
> - **`**` is NOT multiplication** → multiplication is `*`
> - **`**` is NOT bold text in Python** → that’s only in Markdown
> - **Unpacking requires dictionaries** → lists use `*` instead
> - **Exponentiation is right associative** → `2 ** 3 ** 2 = 2 ** 9 = 512`

# Summary

| **Use** | **Meaning** | **Example** |
| :--- | :--- | :--- |
| Exponentiation| Raise to a power | `2 ** 3 → 8` |
| Dictionary unpacking | Expand key value pairs | `{**a, **b}` |


# 10 - f-string (f"")

## What it is:
An f string is a special type of text that allows you to insert variables inside the text.

> [!CAUTION]
> - Don’t forget the **f** before the quotes.
> - Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`


# 8 - { }
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
| { } | Shows the variable’s value inside the f string | `{age}` |


# 11 - `round()`

## What it is:  
The round() function rounds a number to the number of decimal places you choose.

  - **round(number)** → rounds to the nearest whole number
  - **round(number, decimals)** → rounds to the number of decimals you specify

> [!CAUTION]
> - **Rounding is not always exact** → floats can have tiny precision errors.
> - **`round()` does not format output** → it changes the number, but does not force decimals to appear.
> - **Use `.2f` for formatting** → if you want fixed decimal places, use formatting instead of round.
> - **Be careful with `input()`** → convert to float before rounding.

**Example:**
`print(round(3.6))`        # 4
`print(round(3.14159, 2))` # 3.14
`print(round(7.89, 1))`    # 7.9



# 12 - `If`

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


# 13 - `Elif`

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


# 14 - `Else`

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
- **Be careful with `input()`** → convert values before comparing in the `if`.

**Example:**
`age = 16`

`if age >= 18:`
    `print("You can enter")`
`else:`
    `print("You cannot enter")`