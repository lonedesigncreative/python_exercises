# Ask for N
N = int(input("Enter N: "))

total = 0
product = 1

for i in range(1, N + 1):
    total += i
    product *= i

print(f"Sum = {total}")
print(f"Product = {product}")