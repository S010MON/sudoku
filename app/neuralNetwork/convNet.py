import numpy as np
import tensorflow as tf


def one_hot_encode(state: np.ndarray) -> np.ndarray:
    return (np.arange(state.max()) == state[..., None] - 1).astype(int).reshape((81, 9))


def decode_output(sud):
    """
    Decode a sudoku with the shape 81x9 (from the one_hot_encoding()) into a readable 9x9 sudoku board.
    """
    sudoku_decoded = np.argmax(sud, axis=1).reshape((9, 9)) + 1
    return sudoku_decoded


def get_max_index(arr):
    max_indices = np.argmax(arr, axis=0)
    return max_indices


def create_model():
    """
    Create model of the Neural Network based on this paper:
    https://cs230.stanford.edu/files_winter_2018/projects/6939771.pdf
    """
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same', input_shape=(81, 9, 1)))

    for i in range(4):
        model.add(tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same'))

    for i in range(4):
        model.add(tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu', padding='same'))

    for i in range(4):
        model.add(tf.keras.layers.Conv2D(16, kernel_size=(3, 3), activation='relu', padding='same'))

    model.add(tf.keras.layers.Conv2D(1, kernel_size=(3, 3), activation='relu', padding='same'))

    return model


class ConvNet:

    def __init__(self):
        self.model = tf.keras.models.load_model('model_2')

    def predict(self, sudoku: np.ndarray((9, 9))) -> np.ndarray((9, 9)):

        if sudoku.shape != (9, 9):
            raise Exception("Sudoku shape must be (9, 9)!")

        prediction = self.model.predict([one_hot_encode(sudoku)])
        return decode_output(prediction[0])
