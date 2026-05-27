# Ask the user for personal data
name = input("Name: ")
age = int(input("Age: "))
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

# BMI calculation
bmi = weight / (height ** 2)

# Round BMI to 2 decimal places
bmi = round(bmi, 2)

# Show BMI value
print(f"{name}, your BMI is: {bmi}")

# BMI classification
if bmi < 17:
    print("Very underweight")
elif 17 <= bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
elif 30 <= bmi < 35:
    print("Obesity I")
elif 35 <= bmi < 40:
    print("Obesity II (severe)")
else:
    print("Obesity III (morbid)")