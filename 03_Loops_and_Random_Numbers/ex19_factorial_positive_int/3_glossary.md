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


# 7 - Addition (`+`)

## What it does:  
Adds two values.

> [!CAUTION]
> - Only works correctly with numbers.
> - If you add text, Python will join the words instead of doing math.

**Example:**
`total = 5 + 3`


# 8 - *=

## What it is:
`*=` is an **augmented assignment operator** in Python.

>> “Multiply the variable by a value and update the variable with the result.”

> [!NOTE]
> ## It is the same as:
> `x = x * value`
> 
> But shorter and cleaner:
> `x *= value`

> [!IMPORTANT]
> ### Why `*=` is useful:
> - Makes code shorter
> - Easier to read
> - Works with numbers, strings, and lists
> - Very common in loops and calculations
>
> - **Example in a loop:**
> `value = 1`
> `for i in range(5):`
>     `  value *= 2`


> [!CAUTION]
> - **Types must match** → `"text" *= 3` works, but `"text" *= "a"` does NOT
> - **List repetition duplicates elements** → not multiplication
> - **Variable must exist first** → cannot do `x *= 2` before defining `x`

> **Example:**
*Example 1 - With integers*
`x = 4`
`x *= 3`
`print(x)`   # 12

*Example 2 - With floats*
`price = 10.0`
`price *= 1.2`
`print(price)`   # 12.0

*Example 3 - With strings (repetition)*
`text = "Hi"`
`text *= 3`
`print(text)`   # HiHiHi

*Example 4 - With lists (repetition)*
`nums = [1, 2]`
`nums *= 2`
`print(nums)`   # [1, 2, 1, 2]


# Summary

| **Operator** | **Meaning** | **Example** |
| :--- | :--- | :--- |
| += | Add and update | `x += 1` |
| -= | Subtract and update | `x -= 1` |
| *= | Multiply and update | `x *= 2` |
| /= | Multiply and update | `x /= 2` |


# 9 - Range

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



# 10 - For (loop)
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