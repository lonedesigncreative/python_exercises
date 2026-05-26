# Create a function to receive and add two numbers
def Sum_Numbers(num1, num2):
    total = num1 + num2
    print(f"Sum: {total}")

# Main program
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

# Call the function and pass the values
Sum_Numbers(n1, n2)