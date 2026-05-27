import math  # To use pi

# Ask the user for the radius
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume: V = 4/3 * pi * r^3
volume = (4/3) * math.pi * (radius ** 3)

# Round to two decimal places
volume = round(volume, 2)

# Show the result
print(f"The volume of a sphere with radius {radius} is: {volume}")