# Exercise description:

- Develop a Python program that uses **try** / **except** / **finally** to handle errors that may occur when performing a division based on values entered by the user.

### - 1. **`try` block**
- Inside the `try` block, the program must:
    - **Ask the user to enter two integer numbers** using the `input()` function.
    - **Convert** the received values to integers.
    - **Calculate the result of dividing** he first number by the second.
    - **Display the result** to the user.

### - 2. **`except` block**
- The program must include an `except` block that:
    - **Catches any type of exception** using `Exception`;
    - Assigns a **descriptive name** to the error to make it easier to identify.
    - **Displays a message** informing the user that an error occurred and shows the error details.

### - 3. **`finally` block**
- The * * block must run **regardless** of whether the * * block succeeds or an exception is raised.

It must:
  - Display the message:
    **"Program finished"**


## Test Cases
## **Test Case 1**
1. Enter two valid integers → the program should execute only the `try` and `finally` blocks.
2. Run the program again and enter a **decimal number** in one of the inputs.
   - The program should immediately jump to the `except` block due to the exception.
   - It should display the error **“invalid literal for int()…”**, followed by the message from the `finally` block.

## **Test Case 2**
1. Enter two valid integers → the program should execute only the `try` and `finally` blocks.
2. Run the program again and enter **0** as the second value.
   - The program should immediately jump to the `except` block due to the exception.
   - It should display **“division by zero”**, followed by the message from the `finally` block.