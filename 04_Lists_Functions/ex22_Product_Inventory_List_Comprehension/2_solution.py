# product lists
products = ['Keyboard', 'Mouse', 'Monitor', 'Headset', 'Webcam']
prices = [29.99, 14.50, 189.00, 45.00, 32.50]

# formatted list
formatted = [f"{p}: {pr}€" for p, pr in zip(products, prices)]

# products under 40€
cheap = [p for p, pr in zip(products, prices) if pr < 40]

# total cost
total = sum(prices)

print(formatted)
print("Under 40€:", cheap)
print("Total cost:", total)