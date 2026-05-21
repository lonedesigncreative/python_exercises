# Program to calculate the average fuel consumption of a vehicle

distance = float(input("Enter the total distance travelled (in km): "))
fuel = float(input("Enter the total fuel consumed (in liters): "))

# Decision structure to check for valid input values and calculate fuel consumption
if distance <= 0:
    print("The total distance value was less than or equal to 0.")
elif fuel <= 0:
    print("The total fuel value was less than or equal to 0.")
else:
    consumption = (fuel / distance) * 100
    print(f"The average fuel consumption is: {consumption:.2f} L/100km")


"""
EXPLANATION:

# Program to calculate the average fuel consumption of a vehicle

distance = float(input("Enter the total distance travelled (in km): ")) # Get input from the user for the total distance travelled, which will be used to calculate the average fuel consumption based on the total fuel consumed. The distance should be a floating-point number to allow for decimal values, and it represents the total distance the vehicle has traveled in kilometers.
fuel = float(input("Enter the total fuel consumed (in liters): ")) # Get input from the user for the total fuel consumed, which will be used to calculate the average fuel consumption based on the total distance travelled. The fuel should be a floating-point number to allow for decimal values, and it represents the total amount of fuel consumed by the vehicle in liters.

# Decision structure to check for valid input values and calculate fuel consumption
if distance <= 0: # Check if the distance entered by the user is less than or equal to 0, which is not a valid input for distance traveled. If this condition is true, the program will execute the code block that prints "The total distance value was less than or equal to 0." indicating that the input for distance is invalid and cannot be used to calculate fuel consumption.
    print("The total distance value was less than or equal to 0.")
elif fuel <= 0: # Check if the fuel entered by the user is less than or equal to 0, which is not a valid input for fuel consumed. If this condition is true, the program will execute the code block that prints "The total fuel value was less than or equal to 0." indicating that the input for fuel is invalid and cannot be used to calculate fuel consumption.
    print("The total fuel value was less than or equal to 0.")
else: # If both distance and fuel values are valid (greater than 0), the program will execute the code block that calculates the average fuel consumption using the formula (fuel / distance) * 100 to convert it to liters per 100 kilometers, and then prints the result formatted to two decimal places.
    consumption = (fuel / distance) * 100 # Calculate the average fuel consumption using the formula (fuel / distance) * 100 to convert it to liters per 100 kilometers. This calculation divides the total fuel consumed by the total distance traveled and then multiplies by 100 to express the consumption in terms of liters per 100 kilometers, which is a common unit for measuring fuel efficiency.
    print(f"The average fuel consumption is: {consumption:.2f} L/100km")

"""