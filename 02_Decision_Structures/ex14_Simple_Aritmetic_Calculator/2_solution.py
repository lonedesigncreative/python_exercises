# Ask the user for the desired operation
operation = input("Choose the operation (+, -, *, /): ")

# Ask the user for two numeric values
n1 = float(input("Enter the first value: "))
n2 = float(input("Enter the second value: "))

# Check which operation was chosen
if operation == "+":
    result = n1 + n2
    print(f"Result: {result}")

elif operation == "-":
    result = n1 - n2
    print(f"Result: {result}")

elif operation == "*":
    result = n1 * n2
    print(f"Result: {result}")

elif operation == "/":
    # Check for division by zero
    if n2 == 0:
        print("Error: division by zero is not allowed!")
    else:
        result = n1 / n2
        print(f"Result: {result}")

else:
    print("Invalid operation.")