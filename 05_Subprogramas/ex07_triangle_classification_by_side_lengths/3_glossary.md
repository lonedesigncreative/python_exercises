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



# 11 - return

## What it is:  
`return` is a keyword used inside a function in Python.

>> “Send a value back to the place where the function was called.”

When Python reaches a `return`, the function stops immediately and gives back a result.


> [!NOTE]
> ### Basic usage:
>    - `def function_name():`
>     - `return value`

> [!IMPORTANT]
> **## **sqrt** vs **exponentiation** (`**`)**
>
> You can also calculate square roots `using ** 0.5`.
> 
> | **Method** | **Example** | **Result** |
> | :--- | :--- | :--- |
> | math.sqrt | `math.sqrt(25)` | 5.0 |
> | x ** 0.5 | `25 ** 0.5` | 5.0 |
>
> Both work, but:
> `math.sqrt` is **clearer**
> `**0.5` is **shorter**

### Errors to watch out for

- ❌ Negative numbers cause ValueError
  - `math.sqrt(-9)`   # ValueError
> Because square roots of negative numbers are not real numbers.

> [!TIP]
> - **Always import math** → `pi` is not built in
> - **Use radians in trig functions** → `sin`, `cos`, `tan` expect radians
> - **Pi is a float** → not exact, but extremely precise


> [!CAUTION]
> **## Common uses of `sqrt`**
> 
> - Geometry (distances, circle formulas)
> - Physics (energy, velocity, variance)
> - Statistics (standard deviation)
> - Machine learning (Euclidean distance)
>
> **Example:** distance between two points:
>
>    - `import math`
>    - `distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)`

# Summary

| **Concept** | **Meaning** |
| :--- | :--- |
| sqrt |    Square root |
| Requires math module | `import math` |
| Raises ValueError for negatives | No real root |
| Alternative: x**0.5 | Same result |