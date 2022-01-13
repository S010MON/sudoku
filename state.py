import numpy as np


class State:

    def __init__(self, board):
        self.board = board
        self.rows = np.shape(board)[1]
        self.cols = np.shape(board)[1]
        self.box_coord = {1: (0, 0), 2: (3, 0), 3: (6, 0),
                          4: (0, 3), 5: (3, 3), 6: (6, 3),
                          7: (0, 6), 8: (3, 6), 9: (6, 6)}

    def is_legal(self) -> bool:
        pass

    def check_row(self, row) -> bool:
        L = []
        for col in range(self.cols):
            if self.board[row][col] != 0:
                L.append(self.board[row][col])
        return not has_duplicate(L)

    def check_col(self, col) -> bool:
        L = []
        for row in range(self.rows):
            if self.board[row][col] != 0:
                L.append(self.board[row][col])
        return not has_duplicate(L)

    def check_square(self, square) -> bool:
        L = []
        sq = self.box_coord[square]
        row_start = sq[0]
        col_start = sq[1]
        for row in range(row_start, row_start + 2):
            for col in range(col_start, col_start + 2):
                if self.board[row][col] != 0:
                    L.append(self.board[row][col])
        return not has_duplicate(L)

    def __str__(self):
        S = ''
        for row in range(self.rows):

            if row == 3 or row == 6:
                S += '---------+---------+---------\n'

            for col in range(self.cols):
                if col == 3 or col == 6:
                    S += '|'
                S += ' ' + str(self.board[row][col]) + ' '
            S += '\n'
        return S


def has_duplicate(L) -> bool:
    """ Takes in a list 'l' and returns if a duplicate number has been found"""
    found = {}
    for element in L:
        if element not in found:
            found[element] = 1
        else:
            found[element] += 1

        if found[element] > 1:
            return True

    return False
