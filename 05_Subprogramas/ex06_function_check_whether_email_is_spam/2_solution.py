# Create a function to receive an email
def Check_Email(email):
    # Dual decision structure
    if email.endswith("@xpto.pt"):
        print("Email is SPAM")
    else:
        print("Email is NOT SPAM")

# Main program
Check_Email("john.doe@example.com")
Check_Email("maria.santos@xpto.pt")
Check_Email("random.user@testmail.org")
Check_Email("contact@xpto.pt")
Check_Email("support@mydomain.com")