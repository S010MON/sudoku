import numpy as np
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


def string_to_np_array(S: str) -> np.ndarray((9, 9)):
    array = np.ndarray((81,))
    for i, s in enumerate(S):
        array[i] = s

    return array.reshape((9, 9))


class SudokuRequest(BaseModel):

    algorithm: str
    sudoku: str


@app.post("/sudoku", status_code=status.HTTP_200_OK)
async def sudoku_solver(request: SudokuRequest):
    if request.algorithm == "DFS" or request.algorithm == "dfs":
        return {"message": "Hello World"}
    if request.algorithm == "CNN" or request.algorithm == "cnn":
        return {"message": "Hello World"}

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Choose either dfs (Depth First Search) or cnn (Convolutional Neural Network)")
