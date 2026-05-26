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

# 2 - `If`

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


# 3 - `Elif`

## What it is:  
**elif** means **“else if”**.
It is used when you want to check another condition after the first `if`.

  - `if` → first condition
  - `elif` → second condition (only checked if the first is false)
  - `else` → runs when all previous conditions are false

> [!CAUTION]
> - **Elif must come after an if** → you cannot start with `elif`.
> - **Order matters** → Python checks conditions from top to bottom.
> - **Only one block runs** → once one condition is true, the rest are skipped.
> - **Indentation is required** → keep the structure clean.

**Example:**
`score = 75`

`if score >= 90:`
    `print("Excellent")`
`elif score >= 70:`
    `print("Good")`
`else:`
    `print("Needs improvement")`


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

# 5 - `>`

## What it is:  
The `>` operator means **greater than**.
It checks if a value is **strictly bigger** than another value.

  - If the left value is bigger → True
  - If it is equal or smaller → False

> [!CAUTION]
> - **> is different from >=** → `>` does NOT include equality.
> - **Compare only numbers** → avoid comparing text with numbers.
> - **Convert input() first** → input is text, so convert before comparing.
> - **Spacing matters** → write `a > 10`, not `a>10abc`.

**Example:**
`age = 20`
`print(age > 18)`   # True

`score = 40`
`print(score > 60)` # False

# 5 - Sum

## What it is:  
`sum` is a **built‑in Python function** that adds **all the numbers in an iterable** (like a list, tuple, or set) and returns the **total**.

>> “Add all these values and give me the result.”

> [!NOTE]
> ### Basic structure:
>    - `sum(iterable)`
> **or**
>    - `sum(iterable, start_value)`

> [!TIP]
> **## Common uses**
> **Total of a list**
> **Sum of even/odd numbers**
> **Sum of values in a loop**
> **Sum of dictionary values** (using `.values()`)
> - **Example:**
> `scores = {"Ana": 10, "João": 15, "Maria": 20}`
> `print(sum(scores.values()))`   # 45


> [!CAUTION]
> - **Iterable must contain numbers** → otherwise it errors.
> - **Start value must be a number** → `sum(list, "a")` is invalid.
> - **Large lists are fine** → sum is optimized.
> - **Use sum, not manual loops** → cleaner and faster.
> - **Works only with iterables** → not with single numbers.

> [!WARNING]
> **## What break does NOT do**
> It **cannot** add strings
> It **cannot** add lists
> It **cannot** add mixed types (e.g., number + string)
>   - `sum(["a", "b"])   # ❌ error`


**Example:**
*Example 1 - Sum of a list of numbers*
`numbers = [1, 2, 3, 4]`
`print(sum(numbers))`   # 10


*Example 2 - Sum of a tuple*
`values = (10, 20, 30)`
`print(sum(values))`   # 60