try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    division = num1 / num2
    print(f"Division: {division}")
except ZeroDivisionError as error1:
    print("Division Error: It is not possible to divide by zero.")
except ValueError as error2:
    print("Value Error: You must enter only integer numbers.")
except Exception as error:
    print(f"An unexpected error occurred: {error}")
finally:
    print("Operation finished")