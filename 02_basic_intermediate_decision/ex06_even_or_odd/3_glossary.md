# 1 - Print

## What it is:  
`print` is a command that shows something on the screen.

- **Always use parentheses** → print("Hello")
- Text must be inside quotes `" "`
- Missing quotes or parentheses causes an error.

**Example:**
`print("Python!")`

This will display:
- *Python!*

# 2 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

- `input` always returns text, even if the user types a number.
- If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`

# 3 - Integer

## What it is:  
An integer is a whole number, without decimals.

- An integer cannot have decimals.
- **Do NOT use a comma** → Python will think it’s two values.

**Example:**
`age = 25`


# 4 - `==`

## What it is:  
The `==` operator checks if two values are exactly the same.
It returns True when the values are equal and False when they are different.

  - `==` → compares values
  - It does not assign values (that’s =)

- **== is not =**
  - = assigns a value; == compares values.
- **Compare compatible types**
    - avoid comparing numbers with text ("10" == 10 is False).
- **Becareful with `input()`**
    - input returns text, so convert before comparing (`int(input())`).
- **Case sensitivity matters**
    - `"Ana" == "ana"` is False because the letters are different.
- **Spacing matters** —
  - write `a == 10`, not `a==10abc`.

**Example:**
`age = 18`
`print(age == 18)`   # True

`score = 50`
`print(score == 60)` # False


# 5 - Remainder (`%`)
Also called modulo.

- Only works with numbers.
- If you use text, Python gives an error.
- Be careful: % does not give the result of the division - only the remainder.


## What it does:  
Returns the remainder of a division.

**Example:**
`rest = 10 % 3`   # remainder is 1

# 6 - Remainder (`%`)
Also called modulo.

- Only works with numbers.
- If you use text, Python gives an error.
- Be careful: % does not give the result of the division - only the remainder.


## What it does:  
Returns the remainder of a division.

**Example:**
`rest = 10 % 3`   # remainder is 1


# 7 - `If`

## What it is:  
An **if** statement checks a condition.
If the condition is **true**, the code inside **runs**.
If the condition is **false**, Python **skips it**.

- **Indentation is required** → the code inside the `if` must be indented.
- **If without else does nothing when false** → the program continues normally.
- **Condition must be valid** → avoid writing text or invalid expressions inside the `if`.
- **B****e careful with spacing** → `if age >= 18`: works, but `ifage>=18`: is invalid.

**Example:**
`score = 90`
`if score >= 80:`
   `print("Great job")`

# 8 - `Else`

## What it is:  
The **else** block runs **when the if condition is false**.
It is the “backup” or “alternative” action.

  - **if** = what happens when the condition is true
  - **else** = what happens when the condition is false

- **Else must come after an if** → you cannot use `else` alone.
- **Indentation is required** → the code inside `else` must be indented.
- **Else has no condition** → it runs automatically when the `if` is false.
- **Avoid unnecessary else** → use it only when you really need an alternative action.
- **Be careful with `input()`** → convert values before comparing in the `if`.

**Example:**
`age = 16`

`if age >= 18:`
    `print("You can enter")`
`else:`
    `print("You cannot enter")`