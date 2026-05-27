# Ask the user for hours, minutes, and seconds
hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

# Convert everything to seconds
total_seconds = hours * 3600 + minutes * 60 + seconds

# Show the result
print(f"The total in seconds is: {total_seconds}")