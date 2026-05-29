# function to count vowels in a word
def count_vowels(word):
    # list of vowels
    vowels = "aeiouAEIOU"
    # counter
    count = 0
    # loop through characters
    for char in word:
        if char in vowels:
            count += 1
    # return total vowels
    return count


# example call
print(count_vowels("Programming"))