while True:
    number = int(input("Enter a number between 0 and 10: "))

    if 0 <= number <= 10:
        print("Valid number.")
    else:
        print("Number out of range. Program ended.")
        break