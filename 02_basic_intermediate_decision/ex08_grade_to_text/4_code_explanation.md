> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `grade = int(input("Enter a grade: "))`
> - Get input from the user for the grade, which should be an integer between 1 and 3 representing the numeric grade that will be converted into a textual description (1 for Poor, 2 for Average, and 3 for Good)
> 
> 2. `match grade:`  
> - Decision structure using match/case to determine the textual description of the grade based on the numeric value entered by the user
> 
> 3. `case 1:` 
> - If the grade is 1, the program will execute the code block that prints "Poor" because a grade of 1 corresponds to a poor performance in the grading system
> 
> 4. `print("Poor")` 
> - If the grade is 1, the program will execute the code block that prints "Poor" because a grade of 1 corresponds to a poor performance in the grading system
> 
> 5. `case 2:` 
> - If the grade is 2, the program will execute the code block that prints "Average" because a grade of 2 corresponds to an average performance in the grading system
> 
> 6. `print("Average")` 
> - If the grade is 2, the program will execute the code block that prints "Average" because a grade of 2 corresponds to an average performance in the grading system
>
> 7. `case 3:` 
> - If the grade is 3, the program will execute the code block that prints "Good" because a grade of 3 corresponds to a good performance in the grading system
>
> 8. `print("Good")` 
> - If the grade is 3, the program will execute the code block that prints "Good" because a grade of 3 corresponds to a good performance in the grading system
>
> 9. `case _:` 
> - If the grade is not 1, 2, or 3, we can use a wildcard case to handle invalid input. If the grade entered by the user does not match any of the cases (1, 2, or 3), the program will execute the default case and print "Invalid grade. Please enter a grade between 1 and 3." indicating that the input is not a valid numeric grade for this grading system.
> 
> 9. `print("Invalid grade. Please enter a grade between 1 and 3."):` 
> - Handle invalid input by providing feedback to the user that the entered grade is not valid, prompting them to enter a grade within the specified range (1 to 3) for the program to function correctly.