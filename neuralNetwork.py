import tensorflow as tf
from tensorflow import keras

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