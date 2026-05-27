> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `import math`
> - Imports the `math` module so you can use mathematical constants and functions, such as `math.pi`.
> 
> 2. `radius = float(input("Enter the radius of the sphere: "))`  
> - Reads a value from the user as text, converts it to a floating‑point number with `float()`, and stores it in the variable `radius`.
>
> 3. `volume = (4/3) * math.pi * (radius ** 3)` 
> - Calculates the volume of the sphere using the formula [ V = \frac{4}{3} \cdot \pi \cdot r^3 ] , where `radius ** 3` is the radius raised to the power of 3.
>
> 4. `volume = round(volume, 2)`  
> - Rounds the value stored in `volume` to 2 decimal places and stores the rounded value back in `volume`.
> 
> 5. `print(f"The volume of a sphere with radius {radius} is: {volume}")` 
> - Prints a formatted string showing the radius and the calculated volume, inserting the values of radius and volume.