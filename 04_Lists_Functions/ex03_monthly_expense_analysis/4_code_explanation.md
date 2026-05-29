> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `expenses_hannah = [310, 250, 210, 800, 550]`
> - Creates a list called expenses_ana. This list stores Hannah’s expenses for five different months as integer values.
> 
> 2. `expenses_john = [275, 410, 525, 321, 250]`
> - Creates a list called expenses_john. This list stores John’s expenses for the same five months.
> 
> 3. `total_hannah = sum(expenses_hannah)` 
> - The comment explains that you are summing the values. sum(expenses_Hannah) adds all the numbers in Ana’s list. The result is stored in the variable total_ana, which represents Hannah’s total expenses.
> 
> 4. `total_john = sum(expenses_john)` 
> - sum(expenses_john) adds all the numbers in John’s list. The result is stored in total_john, which represents John’s total expenses.
> 
> 5. `if total_ana > total_john:`
> `print("Ana spent more than John.")`
> - The comment indicates that a conditional structure follows. The if condition checks whether total_ana is greater than total_john. If this is true, the program prints the message: "Ana spent more than John."
>
> 6. `elif total_john > total_hannah:`
> `print("John spent more than hannah.")`
> - elif means “else if”. This condition is checked only if the previous if was false. It checks whether total_john is greater than total_Hannah. If this is true, the program prints: "John spent more than Hannah."
> 
> 7. `else:`
> `print("Hannah and John spent the same amount.")`
> - else covers all remaining cases when neither of the previous conditions is true. That means total_hannah is equal to total_john. In this case, the program prints: "Hannah and John spent the same amount."