# Program that performs an arithmetic operation chosen by the user using match/case

# Get input from the user
value1 = float(input("Enter the first number: "))
value2 = float(input("Enter the second number: "))
operator = input("Enter the operation (+, -, *, /): ")

# Decision structure using match/case
match operator:
    case "+":
        print(f"Result of the addition: {value1 + value2}")
    case "-":
        print(f"Result of the subtraction: {value1 - value2}")
    case "*":
        print(f"Result of the multiplication: {value1 * value2}")
    case "/":
        print(f"Result of the division: {value1 / value2}")
    case _:
        print("Invalid operator.")
