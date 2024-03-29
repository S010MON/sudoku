import numpy as np
from .state import State


def generate_empty_state() -> State:
    return State(np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]]))


def generate_possibilities_test() -> State:
    return State(np.array([[0, 0, 0, 0, 1, 0, 2, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 3, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [4, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]]))


def generate_penultimate_state() -> State:
    return State(np.array([[1, 4, 7, 2, 5, 8, 3, 6, 9],
                          [2, 5, 8, 3, 6, 9, 4, 7, 1],
                          [3, 6, 9, 4, 7, 1, 5, 8, 2],
                          [4, 7, 1, 5, 8, 2, 6, 9, 3],
                          [5, 8, 2, 6, 9, 3, 7, 1, 4],
                          [6, 9, 3, 7, 1, 0, 8, 2, 5],
                          [7, 1, 4, 8, 2, 5, 9, 3, 6],
                          [8, 2, 5, 9, 3, 6, 1, 4, 7],
                          [9, 3, 6, 1, 4, 7, 2, 5, 8]]))


def generate_valid_state() -> State:
    return State(np.array([[1, 4, 0, 2, 5, 8, 3, 0, 9],
                          [2, 5, 8, 3, 6, 9, 4, 7, 1],
                          [3, 0, 9, 4, 7, 1, 0, 8, 2],
                          [4, 7, 1, 5, 0, 2, 6, 9, 3],
                          [5, 8, 2, 6, 9, 3, 7, 1, 4],
                          [6, 9, 3, 7, 1, 0, 8, 2, 5],
                          [7, 1, 4, 8, 2, 5, 9, 3, 6],
                          [0, 2, 5, 9, 3, 6, 1, 4, 7],
                          [9, 3, 0, 1, 4, 7, 2, 5, 8]]))


def generate_invalid_row_state() -> State:
    A = np.array([[1, 1, 7, 2, 5, 8, 3, 6, 9],
                  [2, 2, 0, 3, 6, 0, 4, 7, 1],
                  [3, 3, 9, 4, 7, 1, 5, 8, 2],
                  [4, 4, 1, 5, 8, 2, 0, 9, 3],
                  [5, 5, 2, 6, 9, 3, 7, 1, 4],
                  [6, 6, 0, 7, 1, 0, 8, 2, 5],
                  [7, 7, 4, 8, 2, 5, 9, 3, 6],
                  [8, 8, 5, 9, 0, 6, 1, 0, 7],
                  [9, 9, 0, 1, 4, 7, 0, 5, 8]])
    return State(A)


def generate_invalid_col_state() -> State:
    A = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
                  [3, 6, 9, 4, 7, 1, 5, 8, 2],
                  [0, 7, 1, 5, 8, 2, 0, 9, 3],
                  [5, 8, 2, 6, 9, 3, 7, 1, 4],
                  [6, 9, 0, 7, 1, 0, 8, 2, 5],
                  [7, 1, 4, 8, 2, 5, 9, 3, 6],
                  [0, 2, 5, 9, 0, 6, 1, 0, 7],
                  [9, 3, 0, 1, 4, 7, 0, 5, 8]])
    return State(A)


def generate_invalid_box_state() -> State:
    A = np.array([[1, 0, 0, 0, 4, 0, 0, 0, 7],
                  [0, 1, 0, 0, 4, 0, 0, 7, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 2, 5, 0, 0, 8, 0, 0],
                  [2, 0, 0, 0, 0, 0, 0, 0, 8],
                  [0, 0, 0, 0, 0, 5, 0, 8, 0],
                  [3, 0, 0, 0, 0, 0, 9, 9, 9],
                  [0, 3, 0, 6, 6, 0, 9, 9, 9],
                  [0, 0, 0, 0, 6, 0, 9, 9, 9]])
    return State(A)


def generate_complete_state() -> State:
    A = np.array([[1, 4, 7, 2, 5, 8, 3, 6, 9],
                  [2, 5, 8, 3, 6, 9, 4, 7, 1],
                  [3, 6, 9, 4, 7, 1, 5, 8, 2],
                  [4, 7, 1, 5, 8, 2, 6, 9, 3],
                  [5, 8, 2, 6, 9, 3, 7, 1, 4],
                  [6, 9, 3, 7, 1, 4, 8, 2, 5],
                  [7, 1, 4, 8, 2, 5, 9, 3, 6],
                  [8, 2, 5, 9, 3, 6, 1, 4, 7],
                  [9, 3, 6, 1, 4, 7, 2, 5, 8]])
    return State(A)