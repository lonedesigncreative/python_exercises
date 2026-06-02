> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `prices = [1.50, 8.90, 0.75, 15.00, 4.20, 12.50, 2.30, 9.99]`
> - Creates a list named `prices` with several float values.
> 
> 2. `discounted = [round(p * 0.9, 2) for p in prices]`
> - Creates a new list where each price is multiplied by `0.9` and rounded to two decimals.
> 
> 3. `high_prices = [p for p in prices if p > 5]` 
> - Creates a list containing only the prices greater than `5`.
> 
> 4. `high_discount = [round(p * 0.85, 2) for p in prices if p > 5]` 
> - Creates a list of discounted prices, but only for prices greater than `5`.
>
> 5. `print(discounted)`
> - Prints the list of discounted prices.
> 
> 6. `print(high_prices)`
> - Prints the list of prices above `5`.
> 
> 7. `print(high_discount)` 
> - Prints the list of discounted high prices.