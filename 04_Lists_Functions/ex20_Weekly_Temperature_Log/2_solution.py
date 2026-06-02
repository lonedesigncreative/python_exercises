# temperatures for 7 days
temps = [22, 25, 19, 28, 30, 24, 21]

# highest and lowest
print("Max:", max(temps))
print("Min:", min(temps))

# average
avg = sum(temps) / len(temps)
print("Average:", avg)

# days above average
for i, t in enumerate(temps):
    if t > avg:
        print("Above average on day:", i)