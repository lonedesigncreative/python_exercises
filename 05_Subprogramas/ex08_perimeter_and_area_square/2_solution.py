# function to calculate perimeter and area
def square_info(side):
    # calculate perimeter
    perimeter = 4 * side
    # calculate area
    area = side * side
    # return both values
    return perimeter, area


# example call
print(square_info(6))