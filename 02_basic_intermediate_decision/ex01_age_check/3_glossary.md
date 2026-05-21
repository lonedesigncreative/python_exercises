# 1 - `>=`

## What it is:  
`>=` means greater than or equal to.
It checks if a value is bigger or the same as another value.

## :warning: **Warning:**
- **Compare only numbers** → do not compare text with numbers.
- **Convert input() first** → input is text, so convert to `int()` or `float()` before using `>=`.
- **Be clear about the boundary** → `>=` includes equality; `>` does not.

**Example:**
`age = 18`
`print(age >= 18)`   # True


# 2 - `If`

## What it is:  
An **if** statement checks a condition.
If the condition is **true**, the code inside **runs**.
If the condition is **false**, Python **skips it**.

## :warning: **Warning:**
- **Indentation is required** → the code inside the `if` must be indented.
- **If without else does nothing when false** → the program continues normally.
- **Condition must be valid** → avoid writing text or invalid expressions inside the `if`.
- **B****e careful with spacing** → `if age >= 18`: works, but `ifage>=18`: is invalid.

**Example:**
`score = 90`
`if score >= 80:`
   `print("Great job")`

# 3 - Print

## What it is:  
`print` is a command that shows something on the screen.

## :warning: **Warning:**
- **Always use parentheses** → print("Hello")
- Text must be inside quotes `" "`
- Missing quotes or parentheses causes an error.

**Example:**
`print("Python!")`

This will display:
- *Python!*

# 4 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

## :warning: **Warning:**
- `input` always returns text, even if the user types a number.
- If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`

# 5 - Integer

## What it is:  
An integer is a whole number, without decimals.

## :warning: **Warning:**
- An integer cannot have decimals.
- **Do NOT use a comma** → Python will think it’s two values.

**Example:**
`age = 25`

# 6 - Text (in Python called string)

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
