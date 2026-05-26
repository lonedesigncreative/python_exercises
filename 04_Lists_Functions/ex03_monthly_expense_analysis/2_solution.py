expenses_ana = [310, 250, 210, 800, 550]
expenses_joao = [275, 410, 525, 321, 250]

# Sum the values of each list
total_ana = sum(expenses_ana)
total_joao = sum(expenses_joao)

# Double chained decision structure
if total_ana > total_joao:
    print("Ana spent more than João.")
elif total_joao > total_ana:
    print("João spent more than Ana.")
else:
    print("Ana and João spent the same amount.")