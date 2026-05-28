total = 0

for i in range(20):
    number = float(input(f"Enter number {i + 1}: "))
    total += number

average = total / 20

print(f"Sum = {total}")
print(f"Average = {average}")