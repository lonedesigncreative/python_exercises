# matrix of students: [name, grade1, grade2, grade3]
students = [
    ['Hannah', 15, 17, 14],
    ['Bruno', 10, 12, 9],
    ['Karla', 18, 16, 19],
    ['David', 13, 11, 15]
]

# print first student
print("First student:", students[0][0])

# print Bruno's second grade
print("Bruno grade 2:", students[1][2])

# calculate averages
for student in students:
    name = student[0]
    grades = student[1:]
    avg = sum(grades) / len(grades)
    print(name, "average:", round(avg, 1))