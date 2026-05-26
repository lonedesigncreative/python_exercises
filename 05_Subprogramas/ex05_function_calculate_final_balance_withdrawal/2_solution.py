def Calculate_Balance(balance, withdraw):
    # Decision structure to check if the value is negative
    if balance < withdraw:
        print("You cannot withdraw an amount greater than your balance")
    else:
        final_balance = balance - withdraw
        print(f"Balance after withdrawal: {final_balance}")

# Main program
Calculate_Balance(1200, 1500)
Calculate_Balance(2000, 1700)