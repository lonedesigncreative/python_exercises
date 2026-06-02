# initial list
numbers = [10, 25, 7, 42, 15, 7, 33]

# append one element
numbers.append(99)

# extend with multiple elements
numbers.extend([50, 60])

# remove first occurrence of 7
numbers.remove(7)

# pop last element
removed = numbers.pop()

# search values
print("99 in list?", 99 in numbers)
print("100 in list?", 100 in numbers)

# find index of 42
if 42 in numbers:
    print("Index of 42:", numbers.index(42))

# count occurrences of 7
print("Occurrences of 7:", numbers.count(7))

# print final list
print("Final list:", numbers)