> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `expenses_ana = [310, 250, 210, 800, 550]`
> - Creates a list called expenses_ana. This list stores Ana’s expenses for five different months as integer values.
> 
> 2. `expenses_joao = [275, 410, 525, 321, 250]`
> - Creates a list called expenses_joao. This list stores João’s expenses for the same five months.
> 
> 3. `total_ana = sum(expenses_ana)` 
> - The comment explains that you are summing the values. sum(expenses_ana) adds all the numbers in Ana’s list. The result is stored in the variable total_ana, which represents Ana’s total expenses.
> 
> 4. `total_joao = sum(expenses_joao)` 
> - sum(expenses_joao) adds all the numbers in João’s list. The result is stored in total_joao, which represents João’s total expenses.
> 
> 5. `if total_ana > total_joao:`
> `print("Ana spent more than João.")`
> - The comment indicates that a conditional structure follows. The if condition checks whether total_ana is greater than total_joao. If this is true, the program prints the message: "Ana spent more than João."
>
> 6. `elif total_joao > total_ana:`
> `print("João spent more than Ana.")`
> - elif means “else if”. This condition is checked only if the previous if was false. It checks whether total_joao is greater than total_ana. If this is true, the program prints: "João spent more than Ana."
> 
> 7. `else:`
> `print("Ana and João spent the same amount.")`
> - else covers all remaining cases when neither of the previous conditions is true. That means total_ana is equal to total_joao. In this case, the program prints: "Ana and João spent the same amount."