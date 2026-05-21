# 1 - Print

## What it is:  
`print` is a command that shows something on the screen.

#### :warning: **Warning:**
- Always use parentheses → print("Hello")
- Text must be inside quotes `" "`
- Missing quotes or parentheses causes an error.

**Example:**
`print("Python!")`

This will display:
- *Python!*

# 4 - Text (in Python called string)

## What it is:  
Text inside quotes `" "`.

#### :warning: **Warning:**
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


# 5 - `<=`

## What it is:  
The `<=`  operator means **less than or equal to**.
It checks if a value is **smaller** or **the same** as another value.

### :warning: **Warning:**
- **`<=` includes equality** → different from `<`, which does not.
- **Compare only numbers** → avoid comparing text with numbers.
- **Convert `input()` first** → input is text, so convert before comparing.
- **Spacing matters** → write `a <= 10`, not `a<=10abc`.

**Example:**
`age = 12`
`print(age <= 12)`   # True

`temperature = 18`
`print(temperature <= 15)`   # False


# 6 - Addition (`+`)

## What it does:  
Adds two values.

### :warning: **Warning:**
- Only works correctly with numbers.
- If you add text, Python will join the words instead of doing math.

**Example:**
`total = 5 + 3`

# 7 - f-string (f"")

## What it is:
An f string is a special type of text that allows you to insert variables inside the text.

### :warning: **Warning:**
- Don’t forget the **f** before the quotes.
- Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`

# 8 - { }
## What it means:
The `{ }` are used to show the value of a variable inside the text.

### :warning: **Warning:**
- Inside `{ }` you must put a **variable** or an **expression**.
- If you put text without quotes, it gives an error.
- If you put quotes inside `{ }`, it becomes text again.

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

# 9 - While (loop)
A **while loop** repeats a block of code **as long as the condition is True**.

#### :warning: **Warning:** 
> “Keep doing this while the condition is true.”

#### :bulb: **Nota**
  - When the condition becomes **False**, the loop stops.

> [!IMPORTANT]
## How it works:
- The condition is checked first.
- If True, the loop runs.
- If False, the loop stops.

#### :warning: **Warning:**
- **Avoid infinite loops** → always update the variable inside the loop.
- **Condition must eventually become False** → otherwise the loop never ends.
- **Indentation is required** → everything inside the loop must be indented.
- **Be careful with `input()`** → convert values before comparing.
- **Use while when repetitions are unknown** → if you know the exact number, `for` is usually better.

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