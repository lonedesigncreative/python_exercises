> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `while True:`
> - Creates an infinite loop: the code inside this block will keep running repeatedly until a break statement is executed.
> 
> 2. `try:`
> - Starts a try block: the code that might raise an exception is placed under this block.
> 
> 3. `age = int(input("Enter your age: "))` 
> - Asks the user for their age with `input()`, then tries to convert the entered value to an integer using int(). The result is stored in the variable `age`.
> 
> 4. `print(f"The age you entered is: {age}")` 
> - Displays the age entered by the user, using an f-string to insert the value of age into the message.
>
> 5. `break` 
> - Exits the loop if everything worked correctly (no exception was raised), ending the while True cycle.
> 
> 6. `except ValueError:`
> - Catches a ValueError exception, which occurs if the conversion to integer fails (for example, if the user types letters or symbols instead of a number).
> 
> 7. `print("Value Error: You must enter only integer numbers!")`
> - Shows an error message informing the user that only integer numbers are allowed. After this, the loop restarts and asks for the age again.