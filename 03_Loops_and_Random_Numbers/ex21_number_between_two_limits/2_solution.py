# Ask for the two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Ensure a < b
if a > b:
    a, b = b, a

# Print the numbers between them
for i in range(a, b + 1):
    print(i)