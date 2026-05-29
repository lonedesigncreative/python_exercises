# function to classify a triangle
def classify_triangle(a, b, c):
    # check if all sides are equal
    if a == b == c:
        return "Equilateral"
    # check if two sides are equal
    elif a == b or a == c or b == c:
        return "Isosceles"
    # all sides different
    else:
        return "Scalene"


# example call
print(classify_triangle(5, 5, 3))