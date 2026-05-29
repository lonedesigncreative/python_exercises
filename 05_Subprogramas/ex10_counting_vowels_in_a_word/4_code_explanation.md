> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `def Check_Email(email):`
> - Defines a function named `Check_Email` that takes one parameter, email, which represents the email address to be checked.
> 
> 2. `if email.endswith("@xpto.pt"):`
> - Checks whether the value stored in `email` ends with the string `"@xpto.pt"`. If it does, the condition is true and the next line will run.
> 
> 3. `print("Email is SPAM")` 
> - Prints the message `"Email is SPAM"` to indicate that any email ending with `"@xpto.pt"` is considered spam.
> 
> 4. `else:` 
> - Defines the alternative path that will execute when the condition in the `if` statement is false (i.e., the email does not end with `"@xpto.pt"`).
>
> 5. `print("Email is NOT SPAM")` 
> - Prints the message `"Email is NOT SPAM"` to indicate that the email is not considered spam.
>
> 6. `Check_Email("john.doe@example.com"` 
> - Calls the `Check_Email` function with the email `"john.doe@example.com"`, triggering the spam check and printing the corresponding message.
>
> 7. `Check_Email("maria.santos@xpto.pt")` 
> - Calls the function with `"maria.santos@xpto.pt"`, which will be classified as spam because it ends with `"@xpto.pt"`.
>
> 8. `Check_Email("random.user@testmail.org")` 
> - Calls the function with `"random.user@testmail.org"`, which does not end with `"@xpto.pt"`, so it will be classified as not spam.
>
> 9. `Check_Email("contact@xpto.pt")` 
> - Calls the function with `"contact@xpto.pt"`, which will again be identified as spam.
>
> 10. `Check_Email("support@mydomain.com")` 
> - Calls the function with `"support@mydomain.com"`, which will be treated as not spam.