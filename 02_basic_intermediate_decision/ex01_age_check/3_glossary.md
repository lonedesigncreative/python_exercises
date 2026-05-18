# 1 - `>=`

## What it is:  
`>=` means greater than or equal to.
It checks if a value is bigger or the same as another value.

- **Compare only numbers** -> do not compare text with numbers.
- **Convert input() first** -> input is text, so convert to `int()` or `float()` before using `>=`.
- **Be clear about the boundary** -> `>=` includes equality; `>` does not.

**Example:**
`age = 18`
`print(age >= 18)`   # True


# 2 - `If`

## What it is:  
An **if** statement checks a condition.
If the condition is **true**, the code inside **runs**.
If the condition is **false**, Python **skips it**.

- **Indentation is required** -> the code inside the `if` must be indented.
- **If without else does nothing when false** -> the program continues normally.
- **Condition must be valid** -> avoid writing text or invalid expressions inside the `if`.
- **B****e careful with spacing** -> `if age >= 18`: works, but `ifage>=18`: is invalid.

**Example:**
`score = 90`
`if score >= 80:`
   `print("Great job")`