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


# 2 - Decimal (in Python called float)

## What it is:  
A decimal number - a number with a dot (.).

> [!CAUTION]
> - Python uses a dot, not a comma.
> - 3.5 is correct, 3,5 is wrong.

**Example:**
`price = 3.50`



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


# 5 - Addition (`+`)

## What it does:  
Adds two values.

> [!CAUTION]
> - Only works correctly with numbers.
> - If you add text, Python will join the words instead of doing math.

**Example:**
`total = 5 + 3`



# 6 - `**`

## In Python:  
In Python, `**` has **two completely different meanings**, depending on where it is used:

  1. Exponentiation operator → mathematical power
  2. Dictionary unpacking → expand key‑value pairs


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
> - **Exponentiation is right‑associative** → `2 ** 3 ** 2 = 2 ** 9 = 512`


# Summary

| **Use** | **Meaning** | **Example** |
| :--- | :--- | :--- |
| Exponentiation| Raise to a power | `2 ** 3 → 8` |
| Dictionary unpacking | Expand key‑value pairs | `{**a, **b}` |


# 7 - f-string (f"")

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


# 8 – import

## What it means:
The import statement is used to bring code from another module or library into your Python program.

>> Use functions, tools, or code that were created somewhere else.

> [!TIP]
> Python has many built in modules (like math, random, datetime) and you can also import your own files.

> [!CAUTION]
> - **Module name must exist** → if the file or library doesn’t exist, Python gives an error.
> - **Avoid name conflicts** → don’t use the same name for variables and modules.
> - **Use aliases to simplify** → like import numpy as np.
> - **Import only what you need** → keeps your code clean and faster.
> - **Your file must be in the same folder** → when importing your own modules.
> - **Do not overuse from module import *** → it can cause confusion.

**Example:**
***Example 1 - Import a whole module***
`import math`
`print(math.sqrt(25))`   # 5.0

***Example 2 - Import only one function***
`from math import sqrt`
`print(sqrt(16))`   # 4.0

***Example 3 - Import with an alias (nickname)***
`import random as r`
`print(r.randint(1, 10))`

***Example 4 - Import multiple functions***
`from math import sin, cos, pi`
`print(sin(pi/2))`   # 1.0

***Example 5 - Import your own file***
`import utils` # import utils


# 9 - `round()`

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


# 10 - math

## What it is:  
`math` is a Python module that provides mathematical functions for working with numbers.

>> “A toolbox with advanced math operations that Python does not have by default.”


> [!NOTE]
> ### To use it::
>    - `import math`


> [!IMPORTANT]
> **## `math` vs `statistics`**
> 
> | **Module** | **Purpose** |
> | :--- | :--- |
> | math | Pure mathematics (roots, logs, trig) |
> | statistics | Averages, medians, variance |



> [!TIP]
> **## Why the math module is useful**
> - More precise than basic operators
> - Has functions not available by default
> - Essential for statistics, geometry, physics, finance
> - Works well with loops, conditions, and data analysis


> [!CAUTION]
> - **sqrt of negative numbers gives ValueError**
> - **Trigonometry uses radians**
> - **math.pow returns float**
> - **Import required** → functions are not built‑in


**Example - Most useful functions:**
*Example 1 - Square root : math.sqrt*
`import math`
`print(math.sqrt(25))`   # 5.0


*Example 2 - Power : math.pow*
`print(math.pow(2, 3))`   # 8.0

*Example 3 - Exponential : math.exp*
`print(math.exp(1))`   # 2.718...


*Example 4 - Logarithm : math.log*
`print(math.log(10))`        # natural log
`print(math.log10(1000))`    # base 10

*Example 5 - Trigonometry : sin, cos, tan*
`print(math.sin(0))`
`print(math.cos(0))`
`print(math.tan(0))`

> [!WARNING]
> These use **radians**, not degrees.
> To convert degrees → radians:
>
> `math.radians(90)`   # 1.5707...

*Example 6 - Constants : π and e*
`print(math.pi)`   # 3.14159...
`print(math.e)`    # 2.71828...

*Example 7 - Rounding : floor and ceil*
`print(math.floor(3.9))`   # 3
`print(math.ceil(3.1))`    # 4


# Table of the most important functions in the math module

| **Function** | **What it does** | **Example** |
| :--- | :--- | :--- |
| math.**sqrt** | Square root | `math.sqrt(25) → 5.0`|
| math.**pow** | Power (always returns float) | `math.pow(2, 3) → 8.0` |
| math.**exp** | Exponential (e^x) | `math.exp(1) → 2.718...` |
| math.**log** | Natural logarithm (base e) | `math.log(10)` |
| math.**log10** | Base‑10 logarithm | `math.log10(1000) → 3` |
| math.**sin** | Sine (radians) | `math.sin(0) → 0` |
| math.**cos** | Cosine | `math.cos(0) → 1` |
| math.**tan** | Tangent | `math.tan(0) → 0` |
| math.**radians** | Degrees → radians | `math.radians(90)` |
| math.**degrees** | Radians → degrees | `math.degrees(math.pi/2)` |
| math.**floor** | 	Round down | `math.floor(3.9) → 3` |
| math.**ceil** | Round up | `math.ceil(3.1) → 4` |
| math.**trunc** | 	Truncate decimals | `math.trunc(3.9) → 3` |
| math.**fabs** | Absolute value (float) | `math.fabs(-5) → 5.0` |
| math.**factorial** | Factorial | `math.factorial(5) → 120` |
| math.**gcd** | Greatest common divisor | `math.gcd(12, 18) → 6` |
| math.**pi** | Constant π | `3.14159...` |
| math.**e** | 	Constant e | `2.71828...` |


# 11 - .sqrt

## What it is:  
`sqrt` is a function from the math module that calculates the square root of a number.

>> “Find the number that, when multiplied by itself, gives the original number.”

**Example:**
- √25 = 5
- √9 = 3
- √49 = 7

In Python:
`import math`
`math.sqrt(25)`   # 5.0


> [!NOTE]
> ### Basic usage:
>    - `import math`
>    - `result = math.sqrt(x)`


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
> - **Always import math** → `pi` is not built‑in
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
| sqrt | 	Square root |
| Requires math module | `import math` |
| Raises ValueError for negatives | No real root |
| Alternative: x**0.5 | Same result |