# Initialize the sum
total = 0

# Read 4 numbers
for i in range(4):
    number = float(input("Enter a number: "))
    total += number

# Calculate the average
average = round(total / 4, 2)

# Show the result
print(f"The average is: {average}")