# Average of 3 numbers using a for loop

sum = 0

for value in range(1, 4):   # from 1 to 3 inclusive
    number = float(input(f"Enter number {value}: "))
    sum = sum + number

# Calculate the average and print the result
average = sum / 3
print(f"The average of the three numbers is: {round(average, 2)}")

"""

EXPLANATION:

# Average of 3 numbers using a for loop

sum = 0 # initialize the sum variable, which will be used to accumulate the total of the three numbers entered by the user

for value in range(1, 4):   # from 1 to 3 inclusive
    number = float(input(f"Enter number {value}: ")) # get input from the user
    sum = sum + number # add the number to the sum

# Calculate the average and print the result
average = sum / 3 # calculate the average by dividing the sum by 3 (the number of values)
print(f"The average of the three numbers is: {round(average, 2)}") # print the average rounded to 2 decimal places for better readability

"""