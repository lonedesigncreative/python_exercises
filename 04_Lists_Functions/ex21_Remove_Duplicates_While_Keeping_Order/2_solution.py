# initial list
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# new list without duplicates
unique = []
for item in lst:
    if item not in unique:
        unique.append(item)

# removed count
removed = len(lst) - len(unique)

print("Without duplicates:", unique)
print("Removed elements:", removed)