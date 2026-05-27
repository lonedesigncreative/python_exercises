> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `name = input("Name: ")`
> - Reads the user’s name as text and stores it in `name`.
> 
> 2. `age = int(input("Age: "))`  
> - Reads the user’s age as text, converts it to an integer, and stores it in `age`.
> 
> 3. `weight = float(input("Weight (kg): "))` 
> - Reads the user’s weight, converts it to a floating‑point number, and stores it in `weight`.
> 
> 4. `height = float(input("Height (m): "))` 
> - Reads the user’s height, converts it to a floating‑point number, and stores it in `height`.
>
> 5. `bmi = weight / (height ** 2)`
> - Calculates the BMI by dividing the weight by the square of the height and stores the result in `bmi`.
> 
> 6. `bmi = round(bmi, 2)`  
> - Rounds the BMI value to 2 decimal places and stores the rounded value back in `bmi`.
> 
> 7. `print(f"{name}, your BMI is: {bmi}")` 
> - Prints a formatted message showing the user’s name and BMI.
> 
> 8. `if bmi < 17:` 
> - Checks if the BMI is less than 17.
>
> 9. `print("Very underweight")` 
> - Prints the classification “Very underweight” if the condition is true.
>
> 10. `elif 17 <= bmi < 18.5:`
> - Checks if the BMI is between 17 (inclusive) and 18.5 (exclusive).
> 
> 11. `print("Underweight")`  
> - Prints the classification “Underweight” if that range condition is true.
> 
> 12. `elif 18.5 <= bmi < 25:` 
> - Checks if the BMI is between 18.5 (inclusive) and 25 (exclusive).
> 
> 13. `print("Normal weight")` 
> - Prints the classification “Normal weight” if that range condition is true.
>
> 14. `elif 25 <= bmi < 30:` 
> - Checks if the BMI is between 25 (inclusive) and 30 (exclusive).
>
> 15. ` print("Overweight")`
> - Checks if the BMI is between 30 (inclusive) and 35 (exclusive).
> 
> 16. `elif 30 <= bmi < 35:`  
> - Prints the classification “Underweight” if that range condition is true.
> 
> 17. `print("Obesity I")` 
> - Prints the classification “Obesity I” if that range condition is true.
> 
> 18. `elif 35 <= bmi < 40:` 
> - Checks if the BMI is between 35 (inclusive) and 40 (exclusive).
>
> 19. `print("Obesity II (severe)")`  
> - Prints the classification “Obesity II (severe)” if that range condition is true.
> 
> 20. `else:` 
> - Covers all remaining cases where BMI is 40 or higher.
> 
> 21. `print("Obesity III (morbid)")` 
> - Prints the classification “Obesity III (morbid)” for those cases.