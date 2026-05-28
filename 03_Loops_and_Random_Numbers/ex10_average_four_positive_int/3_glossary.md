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


# 3 - Decimal (in Python called float)

## What it is:  
A decimal number - a number with a dot (.).

> [!CAUTION]
> - Python uses a dot, not a comma.
> - 3.5 is correct, 3,5 is wrong.

**Example:**
`price = 3.50`


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


# 7 - `round()`

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


# 8 - Range

## What it is:
`range` is a built in Python function used to generate a **sequence of numbers**.
It is most commonly used in **for loops**.

>> “Create numbers starting from one value, ending before another value, increasing by a step.”

> [!NOTE]
> ## Three main forms of `range`
> ### 1. range(stop)
> - Starts at **0**, ends at **stop − 1**.
> 
> `**numbers = [1, 2, 3, 4]**`
> `print(i)`
> **Output:** 0, 1, 2, 3, 4
> 
> ### 2. range(start, stop)
> - Starts at **start**, ends at **stop − 1**.
> 
> `for i in range(2, 6):`
> `print(i)`
> 
> **Output:** 2, 3, 4, 5
> 
> `print(fruits[-1])`  # orange
> 
> ### 3. range(start, stop, step)
> - Adds a **step** (increment or decrement).
> 
> `for i in range(1, 10, 2):`
> `print(i)`
>
> **Output:** 1, 3, 5, 7, 9

> [!IMPORTANT]
> ### Important details:
> - `range` **includes the start**
> - `range` **excludes the stop**
> - `range` **can go backwards**
> - `range` **does not create a list**, but a special sequence type
> - Convert to list with `list(range(...))` if needed
> > `print(list(range(5)))`   # [0, 1, 2, 3, 4]
>

> [!CAUTION]
> - **Stop is not included** → `range(1, 5)` gives 1, 2, 3, 4.
> - **Step cannot be zero** → `range(1, 10, 0)` gives an error.
> - **Use negative step to count down** → otherwise it loops forever.
> - **Range works only with integers** → no floats.
> - **Often used in for loops** → but can be converted to a list.


> **Example:**
*Example 1 - Counting backwards*
`for i in range(10, 0, -1):`
    `print(i)`

*Example 2 - Loop from 1 to 10 (inclusive)*
`for i in range(1, 11):`
    `print(i)`

*Example 3 - Loop through even numbers*
`for i in range(0, 21, 2):`
    `print(i)`


# 9 - For (loop)
A **for loop** is used when you want to **repeat a block of code a specific number of times** or **go through each item in a sequence** (like a list, string, or range).

## What it means:
> “For each value in this sequence, do this action.”

> [!CAUTION]
> - **Indentation is required** → everything inside the loop must be indented.
> - **range upper limit is not included** → `range(1, 5)` stops at 4, not 5.
> - **Variable name is temporary** → `i`, `n`, `item` are just loop variables.
> - **Avoid infinite loops** → `for` loops normally don’t go infinite, but wrong ranges can cause issues.
> - **Be careful with input()** → convert values before using them in a range.
> - **Don’t modify the list while looping** → it can break the loop.

**Example:**
*1. Loop from 1 to 5*
`for i in range(1, 6):`
    `print(i)`

*2. Loop through a list*
`fruits = ["apple", "banana", "orange"]`

`for fruit in fruits:`
    `print(fruit)`

*3. Loop through each letter in a string*
`for letter in "Python":`
    `print(letter)`

*4. Sum numbers from 1 to 10*
`total = 0`

`for n in range(1, 11):`
    `total += n`

`print(total)`

> [!IMPORTANT]
> - #### How the `range()` works:
> The function **range** creates a sequence of numbers.
>   - `range(5)` → 0,1,2,3,4
>   - `range(1, 5)` → 1,2,3,4
>   - `range(1, 10, 2)` → 1,3,5,7,9 (step of 2)


# 10 - +=

## What it is:
`+=` is an **augmented assignment operator** in Python.

>> “Add something to the variable and **update** the variable with the new value.”

> [!NOTE]
> ## It is the same as:
> `x = x + value`
> 
> But shorter and cleaner:
> `x += value`


> [!IMPORTANT]
> ### Why `+=` is useful:
> - Makes code shorter
> - Easier to read
> - Common in loops
> - Works with numbers, strings, lists
> - 
> **Example in a loop:**
> `total = 0`
> `for i in range(5):`
>     `total += i`


> [!CAUTION]
> - **Type must match** → you cannot do `"text" += 5`
> - **Lists use += to extend**, not to append a single item
> - **+= modifies the variable** (important with lists)


> **Example:**
*Example 1 - With numbers*
`x = 5`
`x += 3`
`print(x)`   # 8

> **Meaning:**
> - take the current value of x
> - add 3
> - store the result back in x

*Example 2 - With strings (concatenation)*
`text = "Hello"`
`text += " World"`
`print(text)`   # Hello World

*Example 3 - With lists (extend)*
`numbers = [1, 2]`
`numbers += [3, 4]`
`print(numbers)`   # [1, 2, 3, 4]


# Summary

| **Operator** | **Meaning** | **Example** |
| :--- | :--- | :--- |
| += | Add and update | `x += 1` |
| -= | Subtract and update | `x -= 1` |
| *= | Multiply and update | `x *= 2` |
| /= | Multiply and update | `x /= 2` |