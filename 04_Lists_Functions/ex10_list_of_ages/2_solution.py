# initial list
ages = [25, 15, 19, 22, 37, 78, 46, 2, 67]

# count minors
minors = 0
for age in ages:
    if age < 18:
        minors += 1
print(minors)

# sort descending
ages.sort(reverse=True)
print(ages)

# ask for age
user_age = int(input("Enter an age: "))

# check if age exists
if user_age in ages:
    print("The age is in the list")
else:
    print("There is no one with that age in the list")