# From sequential_model.ipynb (by Google TensorFlow) 

# Setup
import tensorflow as tf
from tensorflow import keras
from keras import layers

# Using a Sequential model with 3 layers
model = keras.Sequential(
        [
            layers.Dense(2, activation="relu", name="layer1"),
            layers.Dense(3, activation="relu", name="layer2"),
            layers.Dense(4, name="layer3"),
        ])

x = tf.ones((3,3))
y = model(x)

print(model.layers)
