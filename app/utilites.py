import numpy as np


def string_to_np_array(S: str) -> np.ndarray((9, 9)):
    array = np.ndarray((81,))
    for i, s in enumerate(S):
        array[i] = s

    return array.reshape((9, 9))


def np_array_to_string(A: np.ndarray) -> str:
    s = ""
    shape = A.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            s = s + str(A[i][j])

    return s
