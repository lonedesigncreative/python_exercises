> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `def classify_triangle(a, b, c):`
> - Defines a function named classify_triangle with three parameters: `a`, `b`, and `c`.
> 
> 2. `if a == b == c:`
> - Checks if all three sides `a`, `b`, and `c` are equal.
> 
> 3. `return "Equilateral"` 
> - Returns the string `"Equilateral"` if all sides are equal.
> 
> 4. `elif a == b or a == c or b == c:` 
> - Checks if at least two of the sides are equal.
>
> 5. `return "Isosceles"` 
> - Returns the string `"Isosceles"` if exactly two sides are equal.
>
> 6. `else:` 
> - Covers the case where no sides are equal.
>
> 7. `return "Scalene"` 
> - Returns the string `"Scalene"` when all sides are different.
>
> 8. `print(classify_triangle(5, 5, 3))` 
> - Calls the function with sides `5`, `5`, and `3`, and prints the returned triangle type.