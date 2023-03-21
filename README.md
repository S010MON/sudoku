[![CI_Test](https://github.com/S010MON/sudoku/actions/workflows/python-app.yml/badge.svg)](https://github.com/S010MON/sudoku/actions/workflows/python-app.yml)

# Sudoku Solver
A Sudoku solver that uses one of two algorithms:
### 1. Depth First Search.  
A heuristic selection of the next move is done by taking the empty square with the most complete row and column.  This helps prune the search tree which would otherwise be exponential.  All possible valid moves are calculated and used to generate sub-states.  Invalid states are terminated and backtracking occurs to the next valid state

### 2. Convolutional Neural Network.
A CNN of 16 hidden layers was trained to predict the output of the sudoku in one shot.  The input is the sudoku passed in as a (9, 9), this is propagated through the network with the output forming a  one hot encoded into an (81, 10) vector

**Neural Net Data** available from: https://www.kaggle.com/datasets/bryanpark/sudoku?resource=download

### 3. Web Application
Try out the algorithms at https://leondebnath.com/sudoku.html

![web_app.png](https://github.com/S010MON/sudoku/blob/master/web_app.png)


### 4. API Documentation
The API Documentation can be found at https://sudoku.leondebnath.com/docs

URL endpoints are provided to get random sudoku from the list, and to get solutions using a particular algorithm.

![api_docs.png](https://github.com/S010MON/sudoku/blob/master/api_docs.png)
