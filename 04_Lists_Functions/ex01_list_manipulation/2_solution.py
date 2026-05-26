# Create an empty list of numbers
numbers = []

# Insert data into the list
numbers.append(4)
numbers.append(6)
numbers.append(2)
numbers.append(9)
print(f"Original list: {numbers}")

# Insert a value at a specific index position
numbers.insert(1, 100)
print(f"List after insert: {numbers}")

# Change the value at index 2
numbers[2] = 31
print(f"List after modifying index 2: {numbers}")

# Remove the element at index 1
numbers.pop(1)
print(f"List after removing index 1: {numbers}")

# Return the number of elements in the list
print(f"Number of elements in the list: {len(numbers)}")

# Loop through each value in the list using a FOR loop
for value in numbers:
    print(f"Index {numbers.index(value)} : {value}")

# Use the enumerate() function to count items with a custom starting index
for index, value in enumerate(numbers, 5):
    print(f"Index {index} : {value}")