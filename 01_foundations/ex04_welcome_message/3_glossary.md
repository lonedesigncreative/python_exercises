# 1 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

- `input` always returns text, even if the user types a number.
- If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`

It waits for the user to write something and press Enter.

# 2 - f-string f""

## What it is:
An f‑string is a special type of text that allows you to insert variables inside the text.

- Don’t forget the **f** before the quotes.
- Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`

# 3 - { }

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
| input | Asks the user to type something | 5 + 3 | 8 |
| f-string | Text that can show variables | 10 - 4 | 6 |
| { } | Shows the variable’s value inside the f‑string | 6 * 2 | 12 |
