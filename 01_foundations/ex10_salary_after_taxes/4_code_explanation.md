> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `gross_salary = float(input("Enter your gross salary: "))`
> - Prompt the user to enter their gross salary and convert it to a float for calculations
> 
> 2. `social_security = gross_salary * 0.062`  
> - Calculate the Social Security deduction by multiplying the gross salary by 0.062 (which represents 6.2%). This will give us the amount that will be deducted for Social Security, and the result is stored in the variable social_security.
> 
> 3. `federal_tax = gross_salary * 0.12` 
> - Calculate the Federal Tax deduction by multiplying the gross salary by 0.12 (which represents 12%). This will give us the amount that will be deducted for Federal Tax, and the result is stored in the variable federal_tax.
> 
> 4. `net_salary = gross_salary - social_security - federal_tax` 
> - Calculate the net salary by subtracting both the Social Security deduction and the Federal Tax deduction from the gross salary. This will give us the amount of money that the person will take home after all deductions, and the result is stored in the variable net_salary.
> 
> 5. `print(f"Social Security deduction (6.2%): ${social_security:.2f}")` 
> - Display the Social Security deduction based on the gross salary
> 
> 6. `print(f"Federal Tax deduction (12%): ${federal_tax:.2f}")` 
> - Display the Federal Tax deduction based on the gross salary
> 
> 7. `print(f"Net salary after deductions: ${net_salary:.2f}")` 
> - Display the net salary after subtracting the Social Security and Federal Tax deductions from the gross salary