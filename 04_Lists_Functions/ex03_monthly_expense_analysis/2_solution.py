expenses_hannah = [310, 250, 210, 800, 550]
expenses_john = [275, 410, 525, 321, 250]

# Sum the values of each list
total_hannah = sum(expenses_hannah)
total_john = sum(expenses_john)

# Double chained decision structure
if total_hannah > total_john:
    print("Ana spent more than João.")
elif total_john > total_hannah:
    print("João spent more than Ana.")
else:
    print("Ana and João spent the same amount.")