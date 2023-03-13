from app.depthFirstSearch.state import State


def depth_first_search(state: State) -> State:

    if not state.is_legal():
        return None

    # Base case -> if we find the goal
    if state.is_complete():
        return state

    stack = []
    # Check through all rows and columns
    for row in range(9):
        for col in range(9):

            # if we find a number that has not been filled in yet
            if state.get(row, col) == 0:

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

