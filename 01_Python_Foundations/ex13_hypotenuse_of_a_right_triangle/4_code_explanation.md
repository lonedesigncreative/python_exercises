> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `import math`
> - Imports the `math` module so you can use functions like `math.sqrt()` for square roots.
> 
> 2. `a = float(input("Enter the value of cathetus a: "))`  
> - Reads a value from the user, converts it to a floating‑point number, and stores it in the variable `a`.
>
> 3. `b = float(input("Enter the value of cathetus b: "))` 
> - Reads another value from the user, converts it to a floating‑point number, and stores it in the variable `b`.
>
> 4. `hypotenuse = math.sqrt(a ** 2 + b ** 2)`
> - Calculates the hypotenuse using the Pythagorean theorem: squares `a` and `b`, adds them, then takes the square root of the sum with `math.sqrt()`.
> 
> 5. `hypotenuse = round(hypotenuse, 2)`  
> - Rounds the value of `hypotenuse` to 2 decimal places and stores the rounded result back in `hypotenuse`.
>
> 6. `print(f"The hypotenuse of the triangle with catheti {a} and {b} is: {hypotenuse}")` 
> - Prints a formatted string showing the values of `a`, `b`, and the calculated hypotenuse.