> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `age = int(input("Enter your age: "))`
> - Get input from the user for their age, which will be used to determine if they are an adult. The input is converted to an integer to allow for numerical comparisons, and it represents the age of the user in years.
> 
> 2. `if age >= 18:`  
> - Check if the age entered by the user is greater than or equal to 18 using the greater than or equal to operator (>=). If this condition is true, it means that the user is considered an adult according to common legal definitions, and the program will execute the code block that prints "You are an adult." If this condition is false (i.e., the age is less than 18), the program will skip the code block in the if statement and proceed to print "End of program." without indicating that the user is an adult.
> 
> 3. `print("You are an adult.")` 
> - Print a message to the user indicating that they are an adult if the condition in the if statement is met (i.e., age >= 18). This message serves as feedback to inform the user of their status based on the age they entered.
> 
> 4. `print("End of program.")` 
> - Display a message indicating the end of the program, regardless of the user's age