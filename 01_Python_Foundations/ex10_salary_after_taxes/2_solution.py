# Program that calculates salary deductions in the USA


gross_salary = float(input("Enter your gross salary: ")) 

social_security = gross_salary * 0.062   # 6.2%
federal_tax = gross_salary * 0.12        # 12%

net_salary = gross_salary - social_security - federal_tax

print(f"Social Security deduction (6.2%): ${social_security:.2f}") 
print(f"Federal Tax deduction (12%): ${federal_tax:.2f}") 
print(f"Net salary after deductions: ${net_salary:.2f}") 