import stateFactory
from graph import Graph

if __name__ == "__main__":
    board = stateFactory.generate_valid_state()
    print(str(board))
    graph = Graph(board)
