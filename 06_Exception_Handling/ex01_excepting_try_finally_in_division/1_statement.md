## Program Requirements
- You must create a Python program that performs the following steps:

### - 1. **`try` block**
- Inside the `try` block, the program should:
    - **Ask the user to enter two integer numbers** using the `input()` function.
    - **Convert** the values entered into integers.
    - **Calculate the result of the division** between the two numbers and store it in a variable.
    - **Display the result** to the user.

### - 2. **`except` block**
- You must create an except block that:
    - **Catches any type of exception** using `Exception`;
    - Assigns a **descriptive name** to the error (e.g., `error`) to make it easier to identify;
    - **Displays a message** informing the user that an error occurred and shows the error details.

### - 3. **`finally` block**
- Finally, you must include a `finally` block that will run **regardless** of whether the `try` block succeeded or an exception was raised.
This block must:

  - Display the message:
    **"Program finished"**