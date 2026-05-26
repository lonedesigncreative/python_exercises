## 📘 What This Worksheet Introduces (Exceptions & Defensive Programming)

This worksheet introduces the fundamentals of **exception handling**, **defensive programming**, and the basics of working with Python’s error system. It teaches how to prevent program crashes and how to handle unexpected user input or runtime errors.

---

### 🔹 Core Concepts — Exceptions
- **What exceptions are**  
  Errors that occur during program execution and interrupt normal flow.

- **try / except blocks**  
  - `try:` — code that may cause an error  
  - `except:` — code that runs if an error occurs  
  - `except Exception as e:` — capturing the error message  

- **Specific exception types**
  - `ValueError` — invalid type conversion (e.g., converting text to int)  
  - `ZeroDivisionError` — division by zero  
  - `SyntaxError` — incorrect syntax (missing parentheses, quotes, etc.)  
  - `IndentationError` — incorrect indentation  
  - `ModuleNotFoundError` — importing a module that does not exist  

- **Multiple except blocks**  
  Handling different errors separately.

- **finally block**  
  Code that always runs, regardless of whether an error occurred.

---

### 🔹 Core Concepts — Defensive Programming
- Validating user input  
- Preventing invalid operations  
- Displaying clear error messages  
- Ensuring the program continues running safely  

---

### 🔹 Practical Applications in the Exercises
- Handling invalid numeric input  
- Preventing division by zero  
- Using `try / except / finally` to manage program flow  
- Capturing and displaying error messages  
- Testing programs with different error scenarios  
- Validating user age input  
- Using exception handling to improve user experience  

---

### 🔹 Additional Skills Practiced
- Understanding Python’s built‑in exception hierarchy  
- Using error messages to debug programs  
- Writing safer, more robust code  
- Combining input validation with exception handling  

---

### ✅ Summary
This worksheet teaches how to write **safe and reliable Python programs** using exception handling. Students learn to anticipate errors, prevent crashes, validate input, and use `try`, `except`, and `finally` blocks to control program behavior — an essential skill for real‑world software development.