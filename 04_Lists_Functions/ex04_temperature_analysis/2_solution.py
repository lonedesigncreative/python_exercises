# Import the statistics module
import statistics as st

temperatures = [18.5, 20.0, 19.3, 21.7, 22.1, 17.8, 16.9, 23.4, 24.0, 19.8]

# Find the maximum value using max()
maximum = max(temperatures)

# Find the minimum value using min()
minimum = min(temperatures)

# Sum all values using sum()
total = sum(temperatures)

# Count how many elements are in the list using len()
count = len(temperatures)

# Calculate the average (traditional method)
average_traditional = total / count

# Calculate the average using mean() from the statistics module
average_st = st.mean(temperatures)

# Display the results
print(f"Minimum value: {minimum}")
print(f"Maximum value: {maximum}")
print(f"Sum: {total}")
print(f"Count: {count}")
print(f"Traditional average: {average_traditional}")
print(f"Average using statistics: {average_st}")