from contextlib import asynccontextmanager
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List

import random

from starlette.middleware.cors import CORSMiddleware

from cnn.convNet import ConvNet
from dfs.depthFirstSearch import depth_first_search
from dfs.state import State
from .utilites import string_to_np_array, np_array_to_string


class PuzzleSolution(BaseModel):
    puzzle: str
    solution: str

class SudokuRequest(BaseModel):
    algorithm: str
    sudoku: str


class SudokuPost(BaseModel):
    puzzles: List[PuzzleSolution] = []


algorithms = {}
sudoku = {}


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    algorithms["dfs"] = True,
    algorithms["cnn"] = ConvNet()

    with open("sudoku.csv", "r") as file:
        data = file.readlines()
        for line in data:
            parts = line.split(",")
            sudoku[parts[0]] = parts[1]


@app.get("/sudoku", status_code=status.HTTP_200_OK)
async def get_random():
    n = len(sudoku.keys())
    if n == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No sudokus uploaded")

    r = random.randint(0, n - 1)
    return {"puzzle": list(sudoku.keys())[r]}


@app.post("/sudoku", status_code=status.HTTP_200_OK)
async def sudoku_solver(request: SudokuRequest):

    algo = str.lower(request.algorithm)
    if algo not in algorithms:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Algorithm not found.  " +
                                   "Use either dfs (Depth First Search) or cnn (Convolutional Neural Network)")

    query = string_to_np_array(request.sudoku)

    if algo == "cnn":
        solution = algorithms["cnn"].predict(query)
        solution_state = State(solution)
        response = {"algorithm": algo,
                    "solution": np_array_to_string(solution)}
        return response

    elif algo == "dfs":
        state = State(query)
        solution = depth_first_search(state).board
        response = {"algorithm": algo,
                    "solution": np_array_to_string(solution)}
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Algorithm not found")


@app.put("/sudoku", status_code=status.HTTP_200_OK)
async def add_sudoku(puzzleSolution: SudokuPost):

    with open("sudoku.csv", "a") as file:
        for l in puzzleSolution.puzzles:
            # Add input validation

            sudoku[l.puzzle] = l.solution
            file.write(f"{l.puzzle},{l.solution}")
