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


# 3 - Subtraction (`−`)

## What it does:  
Subtracts one value from another.

> [!CAUTION]
> - You cannot subtract text.
> - You cannot subtract using commas (European style). Use dots.

**Example:**
`difference = 10 - 4`


# 4 - Division (`/`)

## What it does:  
Divides one value by another.
Always returns a decimal (float).

> [!CAUTION]
> - Division always returns a decimal (float).
> - Be careful with dividing by zero - it causes an error.

**Example:**
`result = 10 / 4   # 2.5`


# 5 - f-string (f"")

## What it is:
An f string is a special type of text that allows you to insert variables inside the text.

> [!CAUTION]
> - Don’t forget the **f** before the quotes.
> - Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`


# 6 - { }
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


# 7 - `If`

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


# 8 - `Else`

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


# 9 - `<`

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


# 10 - def

## What it is:  
`def` is a Python keyword used to define a function.

>> “Create a reusable block of code with a name.”

A function lets you:
- organize code
- avoid repetition
- receive inputs
- return outputs

> [!NOTE]
> ### Basic structure:
>    - `def function_name(parameters):`
>    - `code_block`
> **Example:**
>    - `def greet():`
>      - `print("Hello!")`


> [!IMPORTANT]
> **## What def does**
> - Creates a function
> - Gives it a name
> - Defines parameters
> - Defines the code that runs when the function is called

> [!TIP]
> **## Why functions are useful**
> - Avoid repeating code
> - Make programs easier to read
> - Allow modular programming
> - Allow reuse in different parts of the program

> [!CAUTION]
> - **Indentation is required** → code inside the function must be indented.
> - **Functions must be called** → defining is not enough.
> - **Return ends the function** → anything after return is ignored.
> - **Parameters must match** → wrong number of arguments gives error.
> - **Functions create their own scope** → variables inside are local.

**Example:**
*Example 1 - Function with no parameters*
`def say_hello():`
  `print("Hello, John!")`

Call it:
> say_hello()

*Example 2 - Function with one parameter*
`def greet(name):`
  `print("Hello", name)`

Call it:
> greet("Ana")