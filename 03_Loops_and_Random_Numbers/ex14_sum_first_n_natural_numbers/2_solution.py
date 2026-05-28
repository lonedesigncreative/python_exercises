# Ask for N
N = int(input("Enter the value of N: "))

total = 0

# Sum from 1 to N
for i in range(1, N + 1):
    total += i

print(f"The sum of the first {N} natural numbers is {total}")