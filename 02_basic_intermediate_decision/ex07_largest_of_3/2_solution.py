# Program that identifies the largest of three integers

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Compare the three values
if num1 >= num2 and num1 >= num3:
    print("Number 1 is the largest.")
elif num2 >= num1 and num2 >= num3:
    print("Number 2 is the largest.")
else:
    print("Number 3 is the largest.")

print("Number 3 is the largest.")