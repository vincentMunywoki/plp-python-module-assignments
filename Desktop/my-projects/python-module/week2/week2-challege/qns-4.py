#Write a program that accepts user input to create two sets of integers.
# Then, create a new set that contains only the elements that are common to both sets.

# Accept user input to create the first set of integers
set1 = set(map(int, input("Enter the elements for the first set (separated by spaces): ").split()))

# Accept user input to create the second set of integers
set2 = set(map(int, input("Enter the elements for the second set (separated by spaces): ").split()))

# Find the intersection (common elements) between both sets
common_elements = set1 & set2

# Print the common elements
print("Common elements:", common_elements)
