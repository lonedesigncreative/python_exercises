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