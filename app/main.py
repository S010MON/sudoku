from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

from neuralNetwork.convNet import ConvNet
from depthFirstSearch.depthFirstSearch import depth_first_search
from depthFirstSearch.state import State
from .utilites import string_to_np_array, np_array_to_string

app = FastAPI()

algorithms = {"dfs": True,
              "cnn": ConvNet()}


class SudokuRequest(BaseModel):

    algorithm: str
    sudoku: str


@app.post("/sudoku", status_code=status.HTTP_200_OK)
async def sudoku_solver(request: SudokuRequest):

    algo = str.lower(request.algorithm)
    if algo not in algorithms:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Algorithm not found.  " +
                                   "Use either dfs (Depth First Search) or cnn (Convolutional Neural Network)")

    sudoku = string_to_np_array(request.sudoku)

    if algo == "cnn":
        solution = algorithms["cnn"].predict(sudoku)
        solution_state = State(solution)
        response = {"algorithm": algo,
                    "solution": np_array_to_string(solution),
                    "pretty_print": str(solution_state) }
        return response

    elif algo == "dfs":
        state = State(sudoku)
        solution = depth_first_search(state).board
        response = {"algorithm": algo,
                    "solution": np_array_to_string(solution),
                    "pretty_print": str(state)}
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Algorithm not found")
