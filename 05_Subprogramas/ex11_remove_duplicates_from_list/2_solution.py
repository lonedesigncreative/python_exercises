# function to remove duplicates
def remove_duplicates(items):
    # convert to set and back to list
    unique_list = list(set(items))
    # return list without duplicates
    return unique_list


# example call
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))