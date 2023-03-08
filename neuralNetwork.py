import tensorflow as tf
from tensorflow import keras
import numpy as np
import stateFactory
import state

"""
fashiondata = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = fashiondata.load_data()
print(x_test.shape)

# Build the NN and define the different layers
model = tf.keras.models.sequential([
    tf.keras.layers.Flatten(input_shape=(9, 9)),
    tf.keras.layers.Dense
])

# Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train the NN
model.fit(x_train, y_train, epochs=5)
"""


def get_max_index(arr):
    max_indices = np.argmax(arr, axis=0)
    return max_indices

s2 = stateFactory.generate_complete_state()
s1 = stateFactory.generate_invalid_box_state()
s3 = stateFactory.generate_invalid_row_state()

a = [s1.board, s2.board, s3.board]

print(get_max_index(a))
