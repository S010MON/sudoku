import stateFactory
from state import State


def depth_first_search(state: State) -> State:

    print(state)

    if not state.is_legal():
        return None

    # Base case -> if we find the goal
    if state.is_complete():
        return State

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
        result = depth_first_search(stack.pop())
        if result is not None and result.is_complete():
            return result

    return None


if __name__ == "__main__":
    state = stateFactory.generate_valid_state()
    print(depth_first_search(state))
