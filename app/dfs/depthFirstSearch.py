import numpy as np

from app.dfs.state import State


def select_next_move(board: np.ndarray):
    rows = np.count_nonzero(board, axis=1)
    rows[rows == 9] = -1
    row = np.argmax(rows)
    col = np.where(board[row] == 0)[0][0]
    return row, col


def depth_first_search(state: State) -> State:

    if not state.is_legal():
        return None

    # Base case -> if we find the goal
    if state.is_complete():
        return state

    stack = []
    # Get the next best move
    row, col = select_next_move(state.board)
    # run through numbers 1 - 9
    for value in range(1, 10):
        copy = state.copy()     # We do this so as not to change the original state
        copy.set(row, col, value)
        stack.append(copy)

    while len(stack) > 0:
        current_state = stack.pop()

        result = depth_first_search(current_state)
        if result is not None:
            if result.is_complete():
                return result

    return None