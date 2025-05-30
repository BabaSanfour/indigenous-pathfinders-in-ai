"""
Neural Network Example
This script demonstrates how to create and train a simple neural network using TensorFlow.
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Set random seeds for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Generate data
print("Generating data...")
X = np.linspace(-10, 10, 100)
y = np.sin(X) + np.random.normal(0, 0.1, 100)

# Reshape data for neural network
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# Create model
print("\nCreating neural network model...")
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile model
print("Compiling model...")
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# Train model
print("\nTraining model...")
history = model.fit(
    X, y,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# Plot results
plt.figure(figsize=(15, 5))

# Plot training history
plt.subplot(121)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

# Plot predictions
plt.subplot(122)
plt.scatter(X, y, label='Data', alpha=0.5)
plt.plot(X, model.predict(X), 'r-', label='Predictions', linewidth=2)
plt.title('Model Predictions')
plt.xlabel('Input')
plt.ylabel('Output')
plt.legend()

plt.tight_layout()
plt.show()

# Print model summary
print("\nModel Summary:")
model.summary()

# Evaluate model
print("\nModel Evaluation:")
test_loss, test_mae = model.evaluate(X, y, verbose=0)
print(f"Test MAE: {test_mae:.4f}") 