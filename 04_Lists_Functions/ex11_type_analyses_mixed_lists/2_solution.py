# initial list
nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Lists"]

# counters
ints = floats = strings = booleans = 0

# count types
for item in nums:
    if type(item) == int:
        ints += 1
    elif type(item) == float:
        floats += 1
    elif type(item) == str:
        strings += 1
    elif type(item) == bool:
        booleans += 1

# print counts
print(ints, floats, strings, booleans)

# average of integers
int_values = [x for x in nums if type(x) == int]
average_ints = sum(int_values) / len(int_values)
print(average_ints)

# new list with integers
print(int_values)