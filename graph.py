from state import State


class Node:

    def __init__(self, numbers:list):
        """"Takes in a list of possible numbers between 1 - 9, if only 1 is provided,
        then that value is taken as the confimred number"""
        self.numbers = numbers
        self.neighbours = []

    def add_edge(self, node) -> None:
        self.neighbours.append(node)

    def is_confirmed(self) -> bool:
        return len(self.numbers) == 1


class Graph:

    def __init__(self, initial_state:State):
        nodes = []
        for row in range(initial_state.rows):
            for col in range(initial_state.cols):

