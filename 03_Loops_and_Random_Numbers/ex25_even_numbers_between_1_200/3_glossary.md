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


# 2 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

> [!CAUTION]
> - `input` always returns text, even if the user types a number.
> - If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`


# 3 - Remainder (`%`)
Also called modulo.

> [!CAUTION]
> - Only works with numbers.
> - If you use text, Python gives an error.
> - Be careful: % does not give the result of the division - only the remainder.

## What it does:  
Returns the remainder of a division.

**Example:**
`rest = 10 % 3`   # remainder is 1

# Summary

| **Operator** | **Meaning** | **Example** | **Result** |
| :---: | :--- | :---: | :---: |
| + | Addition | 5 + 3 | 8 |
| - | Subtraction | 10 - 4 | 6 |
| * | Multiplication | 6 * 2 | 12 |
| / | Division | 10 / 4 | 2.5 |
| % | Remainder | 10 % 3 | 1 |


# 4 - `==`

## What it is:  
The `==` operator checks if two values are exactly the same.
It returns True when the values are equal and False when they are different.

  - `==` → compares values
  - It does not assign values (that’s =)

> [!CAUTION]
> - **== is not =**
>   - = assigns a value; == compares values.
> - **Compare compatible types**
>     - avoid comparing numbers with text ("10" == 10 is False).
> - **Becareful with `input()`**
>     - input returns text, so convert before comparing (`int(input())`).
> - **Case sensitivity matters**
>     - `"Ana" == "ana"` is False because the letters are different.
> - **Spacing matters** —
>   - write `a == 10`, not `a==10abc`.

**Example:**
`age = 18`
`print(age == 18)`   # True

`score = 50`
`print(score == 60)` # False


# 5 - `If`

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



# 6 - Range

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


# 7 - For (loop)
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