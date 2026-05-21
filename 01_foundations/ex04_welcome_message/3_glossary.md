# 1 - Input

## What it is:  
`input` is a command that **asks the user to type something**.

## :warning: **Warning:**
- `input` always returns text, even if the user types a number.
- If you want a number, you must convert it.

**Example:**
`name = input("Enter your name: ")`

It waits for the user to write something and press Enter.

# 2 - Text (in Python called string)

## What it is:  
Text inside quotes `" "`.

## :warning: **Warning:**
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


# 3 - f-string (f"")

## What it is:
An f‑string is a special type of text that allows you to insert variables inside the text.

## :warning: **Warning:**
- Don’t forget the **f** before the quotes.
- Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`

# 4 - { }

## What it means:
The `{ }` are used to show the value of a variable inside the text.

## :warning: **Warning:**
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
