# function to return month name
def month_name(number):
    # list of month names
    months = [
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ]
    # check valid range
    if 1 <= number <= 12:
        return months[number - 1]
    # invalid number
    return "Invalid month number"


# example call
print(month_name(4))