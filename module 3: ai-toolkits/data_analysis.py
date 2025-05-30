"""
Data Analysis and Visualization Example
This script demonstrates basic data analysis and visualization techniques using pandas and matplotlib.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample data
data = {
    'age': np.random.normal(30, 5, 100),
    'salary': np.random.normal(50000, 10000, 100),
    'experience': np.random.normal(5, 2, 100)
}
df = pd.DataFrame(data)

# Basic analysis
print("Data Summary:")
print(df.describe())

# Create visualizations
plt.figure(figsize=(12, 4))

# Histogram
plt.subplot(131)
plt.hist(df['age'], bins=20)
plt.title('Age Distribution')

# Scatter plot
plt.subplot(132)
plt.scatter(df['experience'], df['salary'])
plt.title('Experience vs Salary')
plt.xlabel('Experience (years)')
plt.ylabel('Salary ($)')

# Correlation heatmap
plt.subplot(133)
sns.heatmap(df.corr(), annot=True)
plt.title('Correlation Matrix')

plt.tight_layout()
plt.show() 