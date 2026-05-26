while True:
    try:
        age = int(input("Enter your age: "))
        print(f"The age you entered is: {age}")
        break
    except ValueError:
        print("Value Error: You must enter only integer numbers!")