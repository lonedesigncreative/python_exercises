# Program that calculates the total price of a plot of land

# Declaration of variables to store user input
length = float(input("Enter the length of the land (in meters): "))
width = float(input("Enter the width of the land (in meters): "))
price_per_m2 = float(input("Enter the price per square meter2: "))

# Calculate the area of the land and the total price
area = length * width
total_price = area * price_per_m2

print(f"The total price of the land is: {total_price}")