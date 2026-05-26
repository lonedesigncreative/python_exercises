# Program that divides two numbers safely

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 > 0:
    result = num1 / num2
    print(f"The result of the division is: {result}")
else:
    print("You cannot divide by a value that is less than or equal to 0.")