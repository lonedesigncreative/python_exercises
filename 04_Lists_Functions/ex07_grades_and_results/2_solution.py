# Create list to store numbers
notes = []

# Loop to request values until the user enters 0
number = -1

while number != 0:
    number = float(input("Enter a new grade: "))
    if number != 0:
        notes.append(number)

# Highest grade
print(f"Highest grade: {max(notes)}")

# Lowest grade
print(f"Lowest grade: {min(notes)}")

# Average of grades
print(f"Average of grades: {sum(notes) / len(notes)}")

# Total number of grades
print(f"Total number of grades: {len(notes)}")