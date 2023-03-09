import numpy as np

def one_hot_encode(state: np.ndarray) -> np.ndarray:
    return (np.arange(state.max()) == state[..., None]-1).astype(int).flatten()

def get_max_index(arr):
    max_indices = np.argmax(arr, axis=0)
    return max_indices

