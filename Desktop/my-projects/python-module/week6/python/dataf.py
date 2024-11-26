import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

print(df)


# Creating a DataFrame from a list of lists
data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

print(df)



import numpy as np

# Creating a DataFrame from a NumPy array
data = np.array([
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
])

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

print(df)

# Common Plot Types in Matplotlib:
# Line Plot: Used to display trends over time or sequences.
# Bar Chart: For comparing discrete categories.
# Scatter Plot: To visualize relationships between two variables.
# Histogram: To show the frequency distribution of data.
# Pie Chart: To represent proportions.
