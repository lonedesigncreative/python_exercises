> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `students = [`
`['Hannah', 15, 17, 14],`
`['Bruno', 10, 12, 9],`
`['Karla', 18, 16, 19],`
`['David', 13, 11, 15]`
`]`
> - Creates a list named `students` where each element is a sublist containing a name and three grades.
> 
> 2. `print("First student:", students[0][0])`
> - Prints the name of the first student.
> 
> 3. `print("Bruno grade 2:", students[1][2])` 
> - Prints Bruno’s second grade.
> 
> 4. `for student in students:` 
> - Starts a loop that goes through each sublist.
>
> 5. `name = student[0]`
> - Stores the student’s name in the variable `name`.
> 
> 6. `grades = student[1:]`
> - Stores the three grades in the variable `grades`.
> 
> 7. `avg = sum(grades) / len(grades)` 
> - Calculates the average of the three grades.
> 
> 8. `print(name, "average:", round(avg, 1))` 
> - Prints the student’s name and average.