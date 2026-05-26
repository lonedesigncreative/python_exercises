> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `fuel = float(input("Enter the total fuel consumed (in liters): "))`
> - Get input from the user for the total fuel consumed, which will be used to calculate the average fuel consumption based on the total distance travelled. The fuel should be a floating-point number to allow for decimal values, and it represents the total amount of fuel consumed by the vehicle in liters.
> 
> 2. `if distance <= 0:`  
> - Check if the distance entered by the user is less than or equal to 0, which is not a valid input for distance traveled. If this condition is true, the program will execute the code block that prints "The total distance value was less than or equal to 0." indicating that the input for distance is invalid and cannot be used to calculate fuel consumption.
> 
> 3. `print("The total distance value was less than or equal to 0.")` 
> - Provide feedback to the user that the distance value is invalid, as it cannot be zero or negative, which would not make sense in the context of calculating fuel consumption. This check ensures that the program only proceeds with valid input values for distance.
> 
> 4. `elif fuel <= 0:` 
> - Check if the fuel entered by the user is less than or equal to 0, which is not a valid input for fuel consumed. If this condition is true, the program will execute the code block that prints "The total fuel value was less than or equal to 0." indicating that the input for fuel is invalid and cannot be used to calculate fuel consumption.
> 
> 5. `print("The total fuel value was less than or equal to 0.")` 
> - Print the result of the division operation to the user. The output will display the quotient of num1 and num2, and it is formatted as a string to provide a clear message indicating that this is the result of the division. If num2 is not greater than 0, the program will execute the code block in the else statement, which will print a message indicating that division by zero or a negative number is not allowed.

> 6. `else:` 
> - If both distance and fuel values are valid (greater than 0), the program will execute the code block that calculates the average fuel consumption using the formula (fuel / distance) * 100 to convert it to liters per 100 kilometers, and then prints the result formatted to two decimal places.
>
> 7. `consumption = (fuel / distance) * 100` 
> - Calculate the average fuel consumption using the formula (fuel / distance) * 100 to convert it to liters per 100 kilometers. This calculation divides the total fuel consumed by the total distance traveled and then multiplies by 100 to express the consumption in terms of liters per 100 kilometers, which is a common unit for measuring fuel efficiency.
>
> 8. `print(f"The average fuel consumption is: {consumption:.2f} L/100km")` 
> - Display the average fuel consumption in liters per 100 kilometers, formatted to two decimal places for better readability. This calculation is based on the total fuel consumed divided by the total distance travelled, multiplied by 100 to convert it to the standard unit of fuel consumption.