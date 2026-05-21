# Program that calculates salary deductions in the USA


gross_salary = float(input("Enter your gross salary: "))

social_security = gross_salary * 0.062   # 6.2%
federal_tax = gross_salary * 0.12        # 12%

net_salary = gross_salary - social_security - federal_tax

print(f"Social Security deduction (6.2%): ${social_security:.2f}")
print(f"Federal Tax deduction (12%): ${federal_tax:.2f}")
print(f"Net salary after deductions: ${net_salary:.2f}")

"""

EXPLANATION:

# Program that calculates salary deductions in the USA


gross_salary = float(input("Enter your gross salary: "))

social_security = gross_salary * 0.062  # Calculate the Social Security deduction by multiplying the gross salary by 0.062 (which represents 6.2%). This will give us the amount that will be deducted for Social Security, and the result is stored in the variable social_security.
federal_tax = gross_salary * 0.12       # Calculate the Federal Tax deduction by multiplying the gross salary by 0.12 (which represents 12%). This will give us the amount that will be deducted for Federal Tax, and the result is stored in the variable federal_tax.

net_salary = gross_salary - social_security - federal_tax # Calculate the net salary by subtracting both the Social Security deduction and the Federal Tax deduction from the gross salary. This will give us the amount of money that the person will take home after all deductions, and the result is stored in the variable net_salary.

print(f"Social Security deduction (6.2%): ${social_security:.2f}")
print(f"Federal Tax deduction (12%): ${federal_tax:.2f}")
print(f"Net salary after deductions: ${net_salary:.2f}")

"""