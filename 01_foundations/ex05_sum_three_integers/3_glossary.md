# 1 - Int()

## What it does:  
`int()` converts something into an **integer**, meaning it turns a value into a whole number.

- `input` always returns text, even if the user types a number.
- If you want a number, you must convert it.

**Example:**
`age = int("25")`

It takes `"25"` **(text)** and turns it into `25` **(number)**.

# 2 - Integer

## What it is:  
An integer is a whole number, without decimals.

- An integer cannot have decimals.
- Do NOT use a comma → Python will think it’s two values.

**Example:**
`age = 25`

# 3 - Print

## What it is:  
`print` is a command that shows something on the screen.

- Always use parentheses → print("Hello")
- Text must be inside quotes `" "`
- Missing quotes or parentheses causes an error.

**Example:**
`print("Hello!")`

This will display:
- *Hello!*

# 4 - Addition (`+`)

## What it does:  
Adds two values.

- Only works correctly with numbers.
- If you add text, Python will join the words instead of doing math.

**Example:**
`total = 5 + 3`

# 5 - f-string (f"")

## What it is:
An f‑string is a special type of text that allows you to insert variables inside the text.

- Don’t forget the **f** before the quotes.
- Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`

# 6 - { }

## What it means:
The `{ }` are used to show the value of a variable inside the text.

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
| { } | Shows the variable’s value inside the f‑string | `{age}` |