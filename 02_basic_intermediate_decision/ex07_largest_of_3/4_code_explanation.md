> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `num1 = int(input("Enter the first integer: "))`
> - Get input from the user for the first integer, which will be used to compare with the other two integers to determine which one is the largest
> 
> 2. `num2 = int(input("Enter the second integer: "))`  
> - Get input from the user for the second integer, which will be used to compare with the first and third integers to determine which one is the largest
> 
> 3. `num3 = int(input("Enter the third integer: "))` 
> - Get input from the user for the third integer, which will be used to compare with the first and second integers to determine which one is the largest
> 
> 4. `if num1 >= num2 and num1 >= num3:` 
> - If num1 is greater than or equal to both num2 and num3, then num1 is the largest number among the three integers entered by the user, and the program will execute the code block that prints "Number 1 is the largest."
> 
> 5. `print("Number 1 is the largest.")` 
> - Provide feedback to the user that the first number is the largest among the three integers entered, indicating that it is greater than or equal to both the second and third numbers. This comparison ensures that the program correctly identifies the largest value based on the user's input.
>
> 6. `elif num2 >= num1 and num2 >= num3:` 
> - If num2 is greater than or equal to both num1 and num3, then num2 is the largest number among the three integers entered by the user, and the program will execute the code block that prints "Number 2 is the largest."
>
> 7. `print("Number 2 is the largest.")` 
> - Provide feedback to the user that number 2 is the largest if it is greater than or equal to both number 1 and number 3. This condition ensures that if there are duplicate values, the program will still correctly identify the largest number, even if it is not unique.
>
> 8. `else:` 
> - If neither num1 nor num2 is the largest, then num3 must be the largest number among the three integers entered by the user, and the program will execute the code block that prints "Number 3 is the largest."
>
> 9. `print("Number 3 is the largest.")` 
> - Provide feedback to the user indicating that the third number is the largest among the three integers entered, confirming that it has the greatest value compared to the first and second numbers. This message will only be displayed if the conditions in the previous if and elif statements are not met, meaning that num3 is greater than or equal to both num1 and num2.