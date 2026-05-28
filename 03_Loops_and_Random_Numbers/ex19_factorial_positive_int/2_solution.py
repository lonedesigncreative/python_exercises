N = int(input("Enter a number to calculate the factorial: "))

factorial = 1

for i in range(1, N + 1):
    factorial *= i

print(f"{N}! = {factorial}")