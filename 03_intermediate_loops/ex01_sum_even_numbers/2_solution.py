# Sum of even numbers from 1 to 50

sum = 0

for number in range(1, 51):  # from 1 to 50 inclusive
    if number % 2 == 0:      # check if the number is even
        sum = sum + number

print(f"The sum of all even numbers from 1 to 50 is: {sum}")

"""
EXPLANATION:

# Sum of even numbers from 1 to 50

sum = 0 # loop to calculate the sum of even numbers from 1 to 50

for number in range(1, 51):  # from 1 to 50 inclusive
    if number % 2 == 0:      # check if the number is even
        sum = sum + number # add the even number to the sum

print(f"The sum of all even numbers from 1 to 50 is: {sum}") # print the final result showing the sum of even numbers from 1 to 50

"""