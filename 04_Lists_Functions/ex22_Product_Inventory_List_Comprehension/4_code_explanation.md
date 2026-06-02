> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `products = ['Keyboard', 'Mouse', 'Monitor', 'Headset', 'Webcam']`
> - Creates a list of product names.
> 
> 2. `prices = [29.99, 14.50, 189.00, 45.00, 32.50]`
> - Creates a list of product prices.
> 
> 3. `formatted = [f"{p}: {pr}€" for p, pr in zip(products, prices)]` 
> - Creates a list of formatted strings combining product names and prices.
> 
> 4. `cheap = [p for p, pr in zip(products, prices) if pr < 40]` 
> - Creates a list of products priced below 40€.
>
> 5. `total = sum(prices)`
> - Calculates the total cost of all products.
> 
> 6. `print(formatted)`
> - Prints the formatted product list.
> 
> 7. `print("Under 40€:", cheap)` 
> - Prints the list of cheaper products.
> 
> 8. `print("Total cost:", total)` 
> - Prints the total cost.