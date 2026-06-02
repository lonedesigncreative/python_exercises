# function to reverse list
def invert(lst):
    new_list = []
    for item in lst:
        new_list.insert(0, item)
    return new_list

# test
print(invert([1, 2, 3, 4, 5]))
print(invert(['a', 'b', 'c']))