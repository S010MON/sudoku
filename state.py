import numpy as np


class State:

    def __init__(self, board):
        self.board = board
        self.rows = np.shape(board)[1]
        self.cols = np.shape(board)[1]
        self.box_coord = {1: (0, 0), 2: (3, 0), 3: (6, 0),
                          4: (0, 3), 5: (3, 3), 6: (6, 3),
                          7: (0, 6), 8: (3, 6), 9: (6, 6)}
        self.boxes = len(self.box_coord)

    def is_legal(self) -> bool:
        for row in range(self.rows):
            if not self.check_row(row):
                return False

        for col in range(self.cols):
            if not self.check_col(col):
                return False

        for box in range(self.boxes):
            if not self.check_square(box):
                return False

        return True

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

    def remaining_numbers_in_row(self, row) -> list:
        L = []
        for col in range(self.cols):
            if self.board[row][col] != 0:
                L.append(self.board[row][col])
        return L

    def remaining_numbers_in_col(self, col):
        pass

    def remaining_number_in_square(self, square):
        pass

    def __str__(self) -> str:
        s = ''
        for row in range(self.rows):

            if row == 3 or row == 6:
                s += '---------+---------+---------\n'

            for col in range(self.cols):
                if col == 3 or col == 6:
                    s += '|'
                s += ' ' + str(self.board[row][col]) + ' '
            s += '\n'
        return s


def has_duplicate(lst) -> bool:
    """ Takes in a list 'l' and returns if a duplicate number has been found"""
    found = {}
    for element in lst:
        if element not in found:
            found[element] = 1
        else:
            found[element] += 1

        if found[element] > 1:
            return True
    return False


def get_missing(lst) -> list:
    """Takes in a list L with values between 1 and 9 and returns the values that are missing, i.e.
    input=[1, 4, 7, 8, 9] -> output=[2, 3, 5, 6] """
    missing = [x+1 for x in range(9)]
    for n in lst:
        if n in missing:
            missing.remove(n)
    return missing
