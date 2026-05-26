# 📘 Subprograms in Python

Subprograms are reusable blocks of code designed to perform a specific task.  
In Python, subprograms are implemented using **functions**, which allow you to organize your program into smaller, modular parts.

They help make code cleaner, easier to understand, and more efficient.

---

## 🔹 Why Subprograms Are Important

Subprograms allow you to:

- Avoid repeating code  
- Improve readability and organization  
- Make programs easier to maintain  
- Test parts of the program independently  
- Reuse logic in multiple places  

They are essential for writing scalable and professional Python applications.

---

## 🔹 How Subprograms Work

A subprogram (function) is defined once and can be executed many times.

### ✔️ Example of a simple function

````python`
`def greet(name):`
    `print(f"Hello, {name}!")`

To call (execute) the function:

`greet("Ana")`

## 🔹 Functions With and Without Return Values

### Functions that only perform an action
They execute code but do not return a value.

`def show_info(name, age):`
    `print(f"Name: {name}, Age: {age}")`

### Functions that return a value
They compute something and send the result back using `return`.

`def add(a, b):`
    `return a + b`

### Parameters and Arguments
Subprograms can receive data through **parameters**, making them flexible and dynamic.

`def multiply(x, y):`
    `return x * y`

Calling the function:

`result = multiply(3, 5)`


## 🔹 Summary
Subprograms are a fundamental part of Python programming.
They allow you to:

    - Break large programs into smaller components
    - Reuse code efficiently
    - Improve clarity and structure
    - Build more complex applications with ease

In Python, subprograms = functions, and mastering them is essential for progressing to more advanced programming concepts.