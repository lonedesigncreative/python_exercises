> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `import random as rd`
> - This line imports Python’s built‑in random module and gives it the short name rd. You will use rd to generate a random number later in the program.
>
> 1. `generated_number = rd.randint(1, 10)`
> - rd.randint(1, 10) generates a random integer between 1 and 10, including both 1 and 10. The result is stored in the variable generated_number. This is the secret number the user has to guess.
> 
> 2. `number = 0`  
> - A variable called number is created and set to 0. It will store the user’s guesses. Starting at 0 just gives it an initial value before the loop.
>
> 3. `while number != generated_number:` 
> - This is the start of a while loop. The loop will continue to run as long as number is not equal to generated_number. When the user finally guesses the correct number, the condition becomes false and the loop stops.
> 
> 3. `number = int(input("Enter a number: "))` 
> - The program asks the user to enter a number. input(...) reads what the user types as text (a string). int(...) converts that text into an integer. The value is stored in number, which is then checked by the loop condition.
>
> 4. `if number != generated_number:`
>    `print("Try again!")`
> - if number != generated_number: checks whether the user’s guess is not equal to the secret number. If the guess is wrong, the program prints "Try again!". Then the loop repeats and asks for another guess.
> 4. `print(f"You guessed the number! It was: {generated_number}")`
> - This line runs after the while loop ends. The loop only ends when number == generated_number, meaning the user guessed correctly. The program then prints a success message showing the correct number.