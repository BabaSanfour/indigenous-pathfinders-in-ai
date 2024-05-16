import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Numpy Examples

# Creating a Numpy array
arr = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", arr)

# Performing operations on the array
mean_value = np.mean(arr)
print("Mean:", mean_value)

# Pandas Examples

# Creating a Pandas DataFrame
data = {'Name': ['John', 'Alice', 'Bob'], 'Age': [25, 30, 22]}
df = pd.DataFrame(data)
print("Pandas DataFrame:")
print(df)

# Accessing columns in Pandas DataFrame
ages = df['Age']
print("Ages Column:")
print(ages)

# Matplotlib Examples

# Creating a simple plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sinusoidal Plot')
plt.show()

