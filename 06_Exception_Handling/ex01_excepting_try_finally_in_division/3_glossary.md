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
>- An integer cannot have decimals.
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


# 7 – as

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


# 8 - try

## What it is:  
`try` is part of Python’s **error‑handling system**.

>> “Try to run this code, and if something goes wrong, handle the error instead of crashing.”

- `try` is always used together with **except**, and sometimes **else** and **finally**.


> [!NOTE]
> ### Basic structure:
>    - `try:`
>    - code that might cause an error
>    - `except:`
>    - code that runs if an error happens


> [!IMPORTANT]
> **## What each part does**
> - **try** → runs code that might fail
> - **except** → handles the error
> - **else** → runs if no error happens
> - **finally** → always runs (cleanup, closing files, etc.)


> [!TIP]
> **## Why try/except is useful**
> - Prevents your program from crashing
> - Lets you show friendly error messages
> - Helps validate user input
> - Useful for files, conversions, APIs, databases, etc.
>
> **Example:**
>`try:`
>   `age = int(input("Enter your age: "))`
>`except ValueError:`
>    `print("Please enter a number")`
> 

> [!CAUTION]
> - **Don’t use bare except** → always catch specific errors when possible
> - **Code inside try should be minimal** → easier to debug
> - **finally always runs** → even if there is an error
> - **except must match the error** → wrong type won’t catch
> - **Avoid hiding bugs** → don’t catch everything blindly

**Example:**
*Example 1 - Basic try/except*
`try:`
    `x = 10 / 0`
`except:`
    `print("An error happened")`

**Output:**
- `An error happened`

*Example 2 - Catch a specific error*
`try:`
    `number = int("abc")`
`except ValueError:`
    `print("Not a valid number")`

*Example 3 - Using else (runs only if no error)*
`try:`
    x = 5 + 5`
`except:`
    `print("Error")`
`else:`
    `print("Everything worked")`

*Example 4 - Using finally (always runs)*
`try:`
    `file = open("data.txt")`
`except FileNotFoundError:`
    `print("File not found")`
`finally:`
    `print("Done")`

# 9 – as

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


# 10 - ValueError

## When it happens:  
A **ValueError** happens when:

>> “The value you gave is the right type, but it is an invalid value for that operation.”

In other words:
- Python **expected** a certain **kind of value**
- You gave something that **cannot be used**, even though the type is correct


> [!NOTE]
> ### Basic structure:
>    - `try:`
>    - code that might cause an error
>    - `except:`
>    - code that runs if an error happens


> [!IMPORTANT]
> **## ValueError vs TypeError**
> 
> | **ValueError** | **Meaning** |
> | :--- | :--- | :--- |
> | ValueError | Type is correct, value is invalid |
> | TypeError | Type is wrong |
>
> **Example:**
> `int("abc") `    # ValueError (string OK, value invalid)
> `int(["abc"])`   # TypeError (list is wrong type)


> [!TIP]
> **## How to handle a ValueError**
> - Use try/except:
>
>`try:`
>   `age = int(input("Enter your age: "))`
>`except ValueError:`
>    `print("Please enter a number")`
> 


> [!CAUTION]
> - **Always validate user input** → especially numbers
> - **Use try/except** to avoid program crashes
> - **Check if values exist before removing**
> - **Statistics functions need valid data**
> - **Conversions must match the format**


> [!WARNING]
> - Wrong number format
> - Invalid value for a function
> - Removing something that doesn’t exist
> - Empty lists in statistics
> - Wrong format in date/time parsing
> - Wrong format in type conversions


**Example that cause ValueError:**
*Example 1 - Converting text to number*
`int("abc")`   # ❌ ValueError

> Because `"abc"` is a string, but **not a valid number**.

*Example 2 - Converting float text to int*
`int("3.5")`   # ❌ ValueError

> `"3.5"` is a number, but **not an integer**.

*Example 3 - Removing an item that does not exist*
`numbers = [1, 2, 3]`
`numbers.remove(5)`   # ❌ ValueError

*Example 4 - Using invalid values in functions*
`from math import sqrt`
`sqrt(-1)`   # ❌ ValueError

> `sqrt()` cannot calculate the square root of a negative number.

*Example 5 - Using statistics functions incorrectly*
`from statistics import mean`
`mean([])`   # ❌ ValueError (empty list)