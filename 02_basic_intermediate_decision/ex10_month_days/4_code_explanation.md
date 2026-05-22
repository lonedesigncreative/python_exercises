> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `month = int(input("Enter a month number (1 to 12): "))`
> - Get input from the user for the month number, which should be an integer between 1 and 12 representing the months of the year (January to December)
> 
> 2. `match month:`  
> - The match/case structure is used to determine the number of days in the month based on the month number entered by the user
> 
> 3. `case 1 | 3 | 5 | 7 | 8 | 10 | 12:` 
> - If the month number is 1, 3, 5, 7, 8, 10, or 12, the program will execute the code block that prints "This month has 31 days." because these months have 31 days in the calendar
> 
> 4. `print("This month has 31 days.")` 
> - Provide feedback to the user that the specified month has 31 days, which applies to January, March, May, July, August, October, and December. This information is important for users who may be trying to determine the number of days in a specific month for planning or scheduling purposes.
> 
> 5. `case 4 | 6 | 9 | 11:` 
> - If the month number is 4, 6, 9, or 11, the program will execute the code block that prints "This month has 30 days." because these months have 30 days in the calendar
> 
> 6. `print("This month has 30 days.")` 
> - Provide feedback to the user that the specified month has 30 days, which applies to April, June, September, and November. This information is important for users who may be trying to determine the number of days in a specific month for planning or scheduling purposes.
>
> 7. `case 2:` 
> - If the month number is 2, the program will execute the code block that prints "February has 28 or 29 days." because February can have either 28 or 29 days depending on whether it is a leap year or not
> 
> 8. `print("February has 28 or 29 days.")` 
> - Note: February has 28 days in a common year and 29 days in a leap year. This information is provided to the user to account for the variability in the number of days in February depending on the year.
>
> 9. `case _:` 
> - If the month number entered by the user does not match any of the cases (1 to 12), the program will execute the default case and print "Invalid month." indicating that the input is not a valid month number
> 
> 10. `print("Invalid month.")` 
> - Provide feedback to the user that the input month number is invalid, as it should be between 1 and 12. This ensures that the program handles incorrect input gracefully and informs the user of the mistake.