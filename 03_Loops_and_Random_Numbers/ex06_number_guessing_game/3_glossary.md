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


# 2 - `!=`

## What it is:  
The **!=** operator means **not equal to**.
It checks if **two values are different**.

- If the values are different → True
- If the values are the same → False

> [!CAUTION]
> - **!= is comparison, not assignment** → don’t confuse with `=`.
> - **Compare compatible types** → `"10" != 10` is True because one is text and the other is a number.
> - **Be careful with input()** → convert before comparing (`int(input())`).
> - **Case sensitivity matters** → `"Ana" != "ana"` is True.
> - **Spacing matters** → write a `!= 5`, `not a!=5abc`.

**Example:**
`age = 18`
`print(age != 20)`   # True

`name = "Ana"`
`print(name != "Ana")`   # False

# 4 - Integer

## What it is:  
An integer is a whole number, without decimals.

> [!CAUTION]
>- An integer cannot have decimals.
> - **Do NOT use a comma** → Python will think it’s two values.

**Example:**
`age = 25`

# 2 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

> [!CAUTION]
> - `input` always returns text, even if the user types a number.
> - If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`


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

# 7 - While (loop)
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

# 8 - import
## What it means:
The import statement is used to bring code from another module or library into your Python program.

>> Use functions, tools, or code that were created somewhere else.

> [!TIP]
> Python has many built‑in modules (like math, random, datetime) and you can also import your own files.

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
import utils # import utils

# 9 - as
## What it is:
In Python, the keyword as is used to create an alias — a nickname — for something you are importing.

>> “Use this shorter or easier name instead of the original one.”

> [!NOTE]
> It is often used for large modules or modules with long names.

> [!CAUTION]
> - **Choose clear aliases** → don’t use random letters that confuse the reader.
> - **Alias replaces the original name** → after using `as`, you must use the alias, not the original name.
> - **Avoid overwriting variables** → don’t use an alias that is already a variable in your code.
> - **Follow conventions** → e.g., `import numpy as np` is standard.

**Example:**
***Example 1 - Alias for a module***
`import math as m`
`print(m.sqrt(25))`   # 5.0

***Example 2 - Alias for a function***
`from math import sqrt as raiz`
`print(raiz(16))`   # 4.0

***Example 3 - Alias for a library (very common)***
`import pandas as pd`
`import numpy as np`

***Example 4 - Alias for a library (very common)***
`import utils as u`
`u.my_function()`

> [!IMPORTANT]
> # **Why use `as`?**
> - To make the code shorter
> - To make names easier to type
> - To avoid name conflicts
> - To follow common conventions (ex.: `pd`, `np`, `plt`)

# 10 - random
## What it means:
The **random** module is a built‑in Python library used to **generate random numbers**, **pick random items**, and **create randomness** in programs.

> [!NOTE]
> To use it, you must import it:
> `import random`

> [!IMPORTANT] - **Most useful functions in random**
> 1. **random.randint — random integer**
> - Returns a random **whole number** between two values (inclusive).
>  **Example:**
>   - `import random`
>   - `print(random.randint(1, 10))`   *# Example: 7*
> 
> 2. **random.random — random float**
> - Returns a random **decimal number** between 0 and 1.
>  **Example:**
>   - `print(random.random())`   *# Example: 0.5321*
>
> 3. **random.choice — pick a random item**
> - Chooses one random element from a list.
>  **Example:**
>   - `colors = ["red", "blue", "green"]`
>   - `print(random.choice(colors))`
>
> 4. **random.shuffle — shuffle a list**
> - Changes the order of items randomly.
>  **Example:**
>   - `cards = [1, 2, 3, 4, 5]`
>   - `random.shuffle(cards)`
>   - `print(cards)`
>
> 5. **random.uniform — random float in a range**
> - Returns a random decimal between two numbers.
>  **Example:**
>   - `print(random.uniform(1, 5))`   *# Example: 3.27*


> [!CAUTION]
> - **Import is required** — you must write `import random` before using it.
> - **randint includes both ends** → `randint(1, 10)` can return 1 and 10.
> - **random.random returns 0–1** → not integers.
> - **shuffle modifies the list** → it changes the original list.
> - **Random is not truly random** → it is pseudo‑random, good for games but not for security.
> - **Use secrets for security** → passwords, tokens, etc.

# 11 - randint
## What it is:
`randint` is a function from the **random** module.
It returns a random integer between two values — **including both limits**.

>> “Give me a random whole number between this minimum and this maximum.”

> [!NOTE]
> To use it, you must import it:
> `import random`
> 

> [!IMPORTANT]
> ## How it works:
>- `randint(a, b)` returns a number **N** such that:
>    - 𝑎 ≤ 𝑁 ≤ 𝑏
>Both **a** and **b** are included.

> [!CAUTION]
> - **Both limits are included** → r`andint(1, 10)` can return 1 and 10.
> - **You must import random first** → otherwise it gives an error.
> - **Only integers** → for decimals, use `random.uniform()`.
> - **Order matters** → the first number must be smaller or equal to the second.
> - **Not for security** → for passwords or tokens, use the `secrets` module.

**Example:**
***Example 1 - Random number from 1 to 10***
`import random`
`print(random.randint(1, 10))`   # 7

***Example 2 - Random dice roll (1 to 6)***
`print(random.randint(1, 6))`

***Example 3 - Random age between 18 and 65***
`age = random.randint(18, 65)`
`print(age)`

***Example 4 - Random negative number***
`print(random.randint(-5, 5))`