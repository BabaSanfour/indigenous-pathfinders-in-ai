# 🤖 Module 3: AI Toolkits

## Getting Started with the Examples
Welcome to the world of AI toolkits! This module will introduce you to the essential libraries and frameworks used in AI development.

## Table of Contents
1. [Introduction to AI Libraries](#introduction-to-ai-libraries)
2. [Data Manipulation with Pandas](#data-manipulation-with-pandas)
3. [Machine Learning with Scikit-learn](#machine-learning-with-scikit-learn)
4. [Deep Learning with TensorFlow and PyTorch](#deep-learning-with-tensorflow-and-pytorch)
5. [Working with Hugging Face](#working-with-hugging-face)
6. [Hands-On python file examples](#hands-on-python-file-examples)

## Introduction to AI Libraries

### Essential Libraries
To incorporate a library into your Python script, you must first import it, typically at the beginning of your code.
```python
# Core libraries
import numpy as np          # Numerical computations 
import pandas as pd         # Data manipulation
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns      # Statistical visualization

# Machine Learning
from sklearn import *      # Machine learning tools

# Deep Learning
import tensorflow as tf    # TensorFlow
import torch              # PyTorch

# NLP
from transformers import * # Hugging Face Transformers
```

### NumPy Examples
```python
# Create arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.zeros((3, 3))  # 3x3 array of zeros
arr3 = np.ones((2, 4))   # 2x4 array of ones
arr4 = np.random.rand(3, 3)  # Random array

# Array operations
arr1 * 2  # Multiply all elements by 2
arr1 + arr1  # Add arrays
np.dot(arr1, arr1)  # Dot product

# Reshaping
arr5 = np.arange(12).reshape(3, 4)  # Create 3x4 array
arr6 = arr5.T  # Transpose

# Statistical operations
np.mean(arr1)  # Mean
np.std(arr1)   # Standard deviation
np.max(arr1)   # Maximum value
```

### Plotting Examples
```python
# Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()

# Scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title('Random Points')
plt.show()

# Multiple plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, y)
ax1.set_title('Plot 1')
ax2.scatter(x, y)
ax2.set_title('Plot 2')
plt.show()
```

## Data Manipulation with Pandas

### Basic Operations
```python
# Reading data
df = pd.read_csv('data.csv')

# Data exploration
df.head()
df.info()
df.describe()

# Data cleaning
df.dropna()
df.fillna(value)
```

### Data Analysis
```python
# Grouping and aggregation
df.groupby('column').mean()
df.pivot_table(values='value', index='index', columns='column')

# Visualization
df.plot(kind='scatter', x='x', y='y')
sns.heatmap(df.corr())
```

## Machine Learning with Scikit-learn

### Data Preprocessing
```python
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
```

### Model Training
```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Train model
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = model.score(X_test, y_test)
```

## Deep Learning with TensorFlow and PyTorch

### TensorFlow Basics
```python
# Define model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile and train
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10)
```

### PyTorch Basics
```python
import torch.nn as nn

# Define model
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(784, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )
    
    def forward(self, x):
        return self.layers(x)

# Training loop
model = Net()
optimizer = torch.optim.Adam(model.parameters())
criterion = nn.CrossEntropyLoss()
```

## Working with Hugging Face

### Using Pretrained Models
```python
from transformers import AutoModel, AutoTokenizer

# Load model and tokenizer
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Process text
text = "Hello, AI world!"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
```

### Fine-tuning Models
```python
from transformers import Trainer, TrainingArguments

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
)

# Train model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset
)
trainer.train()
```

## Hands-On python file examples

### Setting Up Your Environment
Before running any examples, make sure you have set up your Python environment correctly:

1. **Create and Activate a Virtual Environment**
   ```bash
   # Create a new virtual environment
   python -m venv ai_env

   # Activate the environment
   # On Windows:
   ai_env\Scripts\activate
   # On macOS/Linux:
   source ai_env/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   # Install all required packages
   pip install -r requirements.txt
   ```

### Running the Examples
This module includes three practical examples that demonstrate different aspects of AI development:

1. **Data Analysis (`data_analysis.py`)**
   - Demonstrates basic data manipulation and visualization
   - Generates synthetic data and creates various plots
   - Run it with: `python data_analysis.py`
   - Try modifying the data generation parameters or adding new visualizations

2. **Machine Learning Pipeline (`ml_pipeline.py`)**
   - Shows a complete machine learning workflow
   - Includes data preprocessing, model training, and evaluation
   - Run it with: `python ml_pipeline.py`
   - Experiment with different models or feature engineering techniques

3. **Neural Network (`neural_network.py`)**
   - Implements a simple neural network using TensorFlow
   - Demonstrates model creation, training, and evaluation
   - Run it with: `python neural_network.py`
   - Try adjusting the network architecture or training parameters

### Experimenting with the Code
Feel free to modify the examples to learn more:
- Change the data generation parameters
- Try different visualization types
- Experiment with different models
- Adjust hyperparameters
- Add new features or functionality

### Troubleshooting
If you encounter any issues:
1. Make sure your virtual environment is activated
2. Verify all dependencies are installed correctly
3. Check the Python version (3.7+ recommended)
4. Ensure you have sufficient memory for TensorFlow

## Best Practices
- Always preprocess your data
- Use cross-validation
- Monitor model performance
- Document your experiments
- Version your models


## Troubleshooting
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [TensorFlow Documentation](https://www.tensorflow.org/api_docs)
- [PyTorch Documentation](https://pytorch.org/docs/stable/)
- [Hugging Face Documentation](https://huggingface.co/docs/transformers/)

## Additional Resources
- [Kaggle Learn](https://www.kaggle.com/learn)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Hugging Face Course](https://huggingface.co/course) 