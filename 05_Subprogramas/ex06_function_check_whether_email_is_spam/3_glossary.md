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


# 3 - `If`

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


# 4 - `Else`

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


# 5 - def

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


# 6 - endswith

## What it is:  
`endswith` is a string method in Python that checks whether a string ends with a specific sequence of characters.

>> “Does this text finish with this ending?.”

It returns:
- **True** → if the string ends with the given substring
- **False** → if it does not


> [!NOTE]
> ### Basic structure:
>    - `string.endswith(substring)`


> [!IMPORTANT]
> **## What `endswith` is used for**
> - **Check file extensions**
> - **Validate input**
> - **Filter lists of strings**
> - **Work with URLs or emails**
>
> **Example:**
> `email = "user@example.com"`
> `print(email.endswith(".com"))`   # True


> [!TIP]
> **## `endswith` vs `startswith`**
> | **Method** | **What it checks** |
> | :--- | :--- |
> | endswith | Ending of the string |
> | startswith | Beginning of the string |


> [!CAUTION]
> - **Case‑sensitive** → `"Hello".endswith("LO")` is False.
> - **Works only on strings** → not lists or numbers.
> - **Substring must be a string or tuple** → no integers.
> - **Optional start/end slice** → lets you check part of the string.


**Example:**
*Example 1 - Simple check*
`text = "hello world"`
`print(text.endswith("world"))`   # True

*Example 2 - Case‑sensitive*
`print("Python".endswith("on"))`   # True
`print("Python".endswith("On"))`   # False

*Example 4 - Check multiple possible endings*
- You can pass a **tuple** of endings:
`file = "photo.png"`
`print(file.endswith((".png", ".jpg")))`   # True

*Example 2 - Using start and end positions*
`text = "programming"`
`print(text.endswith("gram", 0, 7))`   # True

> **Explanation:** checks only `"program"`.