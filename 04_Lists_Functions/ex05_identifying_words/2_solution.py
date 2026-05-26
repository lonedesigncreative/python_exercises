words_list = ["New York", "Tokyo", "Paris", "London", "Dubai", "Los Angeles"]

# Find the shortest word (by number of characters)
shortest_word = min(words_list, key=len)

# Find the longest word (by number of characters)
longest_word = max(words_list, key=len)

# Display the results
print(f"Shortest word: {shortest_word}")
print(f"Longest word: {longest_word}")