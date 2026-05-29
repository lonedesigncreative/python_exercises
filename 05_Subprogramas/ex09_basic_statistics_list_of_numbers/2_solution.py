# function to show sum, count and average
def list_stats(numbers):
    # calculate sum
    total = sum(numbers)
    # count elements
    count = len(numbers)
    # calculate average
    average = total / count
    # print results
    print("Sum:", total)
    print("Count:", count)
    print("Average:", average)


# example call
list_stats([4, 8, 12, 6])