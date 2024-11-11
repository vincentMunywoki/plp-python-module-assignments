#Create a program that stores a list of words. 
# Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

# List of words
words = ["apple", "banana", "grape", "kiwi", "mango", "orange"]

# List comprehension to find words with odd number of characters
odd_words = [word for word in words if len(word) % 2 != 0]

# Print the result
print("Words with an odd number of characters:", odd_words)
