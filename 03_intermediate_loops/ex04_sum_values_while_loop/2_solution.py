# Sum of values from 1 to 5 using a while loop

sum = 1
total = 0

while sum <= 5:
    total = total + sum
    sum = sum + 1   # manual counter update

print(f"The sum of the values from 1 to 5 is: {total}")