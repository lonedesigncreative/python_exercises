# Average of 3 numbers using a for loop

sum = 0

for value in range(1, 4):   # from 1 to 3 inclusive
    number = float(input(f"Enter number {value}: "))
    sum = sum + number

# Calculate the average and print the result
average = sum / 3
print(f"The average of the three numbers is: {round(average, 2)}")