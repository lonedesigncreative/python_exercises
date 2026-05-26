> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `length = float(input("Enter the length of the land (in meters): "))`
> - Get input from the user for the length of the land, which will be stored in the variable length. The input function prompts the user to enter a value, and the float function converts that input into a decimal number (floating-point number) data type, allowing for more precise measurements of the land's length.
> 
> 2. `width = float(input("Enter the width of the land (in meters): "))`  
> - Get input from the user for the width of the land, which will be stored in the variable width. Similar to length, the input function prompts the user to enter a value, and the float function converts that input into a decimal number (floating-point number) data type, allowing for more precise measurements of the land's width.
> 
> 3. `price_per_m2 = float(input("Enter the price per square meter2: "))` 
> - Get input from the user for the price per square meter, which will be stored in the variable price_per_m2. Again, the input function prompts the user to enter a value, and the float function converts that input into a decimal number (floating-point number) data type, allowing for more precise representation of the price per square meter.
> 
> 4. `area = length * width` 
> - Calculate the area of the land by multiplying the length and width together, and store the result in the variable area. This will give us the total area of the land in square meters.
> 
> 5. `total_price = area * price_per_m2` 
> - Calculate the total price of the land by multiplying the area by the price per square meter, and store the result in the variable total_price. This will give us the total cost of the land based on its area and the price per square meter.
> 
> 6. `print(f"The total price of the land is: {total_price}")` 
> - Display the total price of the land based on the area and price per square meter