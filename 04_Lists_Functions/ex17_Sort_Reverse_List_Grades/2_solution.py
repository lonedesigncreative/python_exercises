# initial grades
grades = [14, 8, 17, 12, 9, 18, 11, 16, 7, 13]

# sorted() creates new list
sorted_grades = sorted(grades)

# sort() modifies original list
grades.sort()

# sort descending
grades.sort(reverse=True)

# reverse list
grades.reverse()

# print results
print("Sorted copy:", sorted_grades)
print("Descending:", grades)