> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `num1 = int(input("Enter the first integer: "))`
> - Convert the input to an integer, as input() returns a string
> 
> 2. `num2 = int(input("Enter the second integer: "))`  
> - Convert the input to an integer, as input() returns a string
> 
> 3. `addition = num1 + num2` 
> - Calculate the sum of num1 and num2 and store the result in the variable addition. This will perform the addition operation and give us the total of the two numbers.
> 
> 4. `subtraction = num1 - num2` 
> - Calculate the difference between num1 and num2 and store the result in the variable subtraction. This will perform the subtraction operation and give us the result of num1 minus num2.
> 
> 5. `multiplication = num1 * num2` 
> - Calculate the product of num1 and num2 and store the result in the variable multiplication. This will perform the multiplication operation and give us the result of num1 multiplied by num2.
> 
> 6. `division = num1 / num2` 
> - Calculate the quotient of num1 divided by num2 and store the result in the variable division. This will perform the division operation and give us the result of num1 divided by num2. It is important to note that if num2 is zero, this will raise a ZeroDivisionError, so in a more robust implementation, you might want to add error handling for that case.
> 
> 7. `remainder = num1 % num2` 
> - Calculate the remainder of num1 divided by num2 using the modulus operator (%) and store the result in the variable remainder. This will give us the value that is left over after dividing num1 by num2.
> 
> 8. `print(f"Addition: {addition}")` 
> - Addition of num1 and num2
> 
> 9. `print(f"Subtraction: {subtraction}")` 
> - Subtraction of num2 from num1
> 
> 10. `print(f"Multiplication: {multiplication}")` 
> - Multiplication of num1 and num2
> 
> 11. `print(f"Division: {division}")` 
> - Division of num1 by num2 (will raise an error if num2 is zero)
> 
> 12. `print(f"Remainder: {remainder}")` 
> - Modulo operator gives the remainder of the division of num1 by num2 (will raise an error if num2 is zero)