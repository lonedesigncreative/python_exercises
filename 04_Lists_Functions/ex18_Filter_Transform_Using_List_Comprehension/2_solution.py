# price list
prices = [1.50, 8.90, 0.75, 15.00, 4.20, 12.50, 2.30, 9.99]

# apply 10% discount
discounted = [round(p * 0.9, 2) for p in prices]

# filter prices above 5
high_prices = [p for p in prices if p > 5]

# filter + transform
high_discount = [round(p * 0.85, 2) for p in prices if p > 5]

# print results
print(discounted)
print(high_prices)
print(high_discount)