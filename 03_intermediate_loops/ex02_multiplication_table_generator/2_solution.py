# Multiplication table from 1 to 10

number = int(input("Enter an integer number: "))

for i in range(1, 11):   # from 1 to 10 inclusive
    print(f"{number} * {i} = {number * i}")