# 🐍 Module 2: Python for AI

Welcome to Python programming! This module will cover Python fundamentals with a focus on AI applications.

## Table of Contents
1. [Python Basics](#python-basics)
2. [Data Structures](#data-structures)
3. [Functions and OOP](#functions-and-oop)
4. [Working with Data](#working-with-data)
5. [Jupyter Notebooks](#jupyter-notebooks)

## Python Basics

### Installation and Setup
- Python installation (from Module 0)
- Setting up your IDE
- Running your first program

### Basic Syntax
```python
# Variables and data types
name = "AI Student"    # String
age = 20              # Integer
height = 1.75         # Float
is_student = True     # Boolean

# Basic operations
print(f"Hello, {name}!")  # f-strings
result = 10 + 5 * 2      # Arithmetic
```

### Control Flow
```python
# If statements
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Loops
for i in range(5):
    print(i)

while condition:
    # do something
    pass
```

## Data Structures

### Lists and Arrays
```python
# Lists
# In Python, a list is an ordered, mutable collection of elements that starts indexing from 0.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers[0] = 10

# NumPy arrays (for AI)
import numpy as np
array = np.array([1, 2, 3, 4, 5])
```

### Dictionaries
```python
# Key-value pairs 
# A dictionary is an unordered collection of key-value pairs, allowing fast retrieval of values.
student = {
    "name": "AI Student",
    "age": 20,
    "courses": ["Python", "ML", "DL"]
}
```

### Sets and Tuples
```python
# Sets (unique elements)
unique_numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}

# Tuples (immutable) 
# A tuple is an ordered, immutable collection of elements.
coordinates = (10, 20)
```

## Functions and OOP

### Functions
```python
def calculate_accuracy(predictions, targets):
    """Calculate model accuracy."""
    correct = sum(p == t for p, t in zip(predictions, targets))
    return correct / len(predictions)
```

### Classes
```python
class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
    
    def forward(self, x):
        # Forward pass
        pass
    
    def backward(self, error):
        # Backward pass
        pass
```

## Working with Data

### File I/O
```python
# Reading files
with open('data.txt', 'r') as f:
    data = f.read()

# Writing files
with open('output.txt', 'w') as f:
    f.write('Results')
```

### Data Processing
```python
# Pandas for data manipulation
import pandas as pd
df = pd.read_csv('data.csv')
df.head()
```

## Jupyter Notebooks

### Getting Started
1. Install Jupyter:
   ```bash
   pip install jupyter
   ```
2. Launch Jupyter:
   ```bash
   jupyter notebook
   ```

## Your First Python File

1. **Create a Python File:**
   - Using a text editor, create a file named `hello.py`.

2. **Write Your First Code:**
   ```python
   print("Welcome to Pathfinders Summer School!")
   ```
   
3. **Run the Python File:**
   ```bash
   $ python hello.py
   ```

## intro.py

You can execute the provided code snippets by running the following command in your terminal:

```bash
$ python intro.py
```

Feel free to modify the `intro.py` file to explore additional Python utilities and enhance your understanding of the language.

### Best Practices
- Use markdown cells for documentation
- Keep cells focused and small
- Use proper variable names
- Document your code

## Hands-on Exercise
1. Create a Python script that:
   - Loads a dataset
   - Performs basic data analysis
   - Implements a simple ML model
2. Convert the script to a Jupyter notebook
3. Add documentation and visualizations

## AI-Focused Examples

### Data Preprocessing
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### Model Training
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Troubleshooting
- [Python Documentation](https://docs.python.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## Additional Resources
- [Python for Data Science](https://www.python.org/about/gettingstarted/)
- [Jupyter Notebook Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
- [Python for AI and ML](https://www.coursera.org/learn/python-for-applied-data-science-ai) 
