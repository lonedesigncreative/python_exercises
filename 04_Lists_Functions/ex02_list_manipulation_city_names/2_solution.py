# 1. Create an empty list named 'cities'
cities = []

# 2. Add four famous cities using append()
cities.append("New York")
cities.append("Tokyo")
cities.append("Paris")
cities.append("London")
print(f"Original list: {cities}")

# 3. Insert a new city between index 2 and 3
cities.insert(2, "Dubai")
print(f"List after insert: {cities}")

# 4. Change the value at index 1
cities[1] = "Los Angeles"
print(f"List after modifying index 1: {cities}")

# 5. Remove the element at index 3
cities.pop(3)
print(f"List after removing index 3: {cities}")

# 6. Show how many elements exist in the list
print(f"Number of elements in the list: {len(cities)}")

# 7. Loop through the list using a FOR loop (show index and value)
print("\nLoop using a normal FOR:")
for i in range(len(cities)):
    print(f"Index {i} : {cities[i]}")

# 8. Loop using enumerate() to generate an automatic counter
print("\nLoop using enumerate():")
for index, value in enumerate(cities):
    print(f"Index {index} : {value}")