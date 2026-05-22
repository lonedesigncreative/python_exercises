> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `number = int(input("Enter an integer number: "))`
> - Get input from the user for an integer number, which will be used to determine whether it is even or odd based on the remainder when divided by 2
> 
> 2. `if number % 2 == 0:`  
> - Ceck if the number is even by using the modulus operator (%) to find the remainder when the number is divided by 2. If the remainder is 0, it means the number is even, and the program will execute the code block that prints "The number is even."
> 
> 3. `print("The number is even.")` 
> - Check if the number is even by using the modulus operator (%) to determine if the remainder when the number is divided by 2 is zero. If the condition is true, it means that the number is even, and the program will print "The number is even." If the condition is false (i.e., the number has a remainder when divided by 2), it means that the number is odd, and the program will execute the code block in the else statement, which will print "The number is odd."
> 
> 4. `else:` 
> - If the number is not even (i.e., the remainder when divided by 2 is not 0), then it must be odd, and the program will execute the code block that prints "The number is odd."
> 
> 5. `print("The number is odd.")` 
> - Provide feedback to the user indicating that the number they entered is odd, which means it is not divisible by 2 without leaving a remainder. This message will only be displayed if the condition in the if statement (number % 2 == 0) is false, confirming that the number is indeed odd.