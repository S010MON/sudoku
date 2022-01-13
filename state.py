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
        lst = []
        for col in range(self.cols):
            if self.board[row][col] != 0:
                lst.append(self.board[row][col])
        return not has_duplicate(lst)

    def check_col(self, col) -> bool:
        lst = []
        for row in range(self.rows):
            if self.board[row][col] != 0:
                lst.append(self.board[row][col])
        return not has_duplicate(lst)

    def check_square(self, square) -> bool:
        lst = []
        sq = self.box_coord[square]
        row_start = sq[0]
        col_start = sq[1]
        for row in range(row_start, row_start + 2):
            for col in range(col_start, col_start + 2):
                if self.board[row][col] != 0:
                    lst.append(self.board[row][col])
        return not has_duplicate(lst)

    def get_possibilities(self, row, col) -> list:
        poss_row = self.possible_numbers_in_row(row)
        poss_col = self.possible_numbers_in_col(col)
        poss_box = self.possible_number_in_square(self.look_up_square(row, col))

        lst = []
        for i in range(1, 10):
            if i in poss_box and i in poss_col and i in poss_row:
                lst.append(i)
        return lst

    def possible_numbers_in_row(self, row) -> list:
        lst = []
        for col in range(self.cols):
            if self.board[row][col] != 0:
                lst.append(self.board[row][col])
        return get_missing(lst)

    def possible_numbers_in_col(self, col) -> list:
        lst = []
        for row in range(self.rows):
            if self.board[row][col] != 0:
                lst.append(self.board[row][col])
        return get_missing(lst)

    def possible_number_in_square(self, square) -> list:
        lst = []
        sq = self.box_coord[square]
        row_start = sq[0]
        col_start = sq[1]
        for row in range(row_start, row_start + 2):
            for col in range(col_start, col_start + 2):
                if self.board[row][col] != 0:
                    lst.append(self.board[row][col])
        return get_missing(lst)

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

    def look_up_square(self, row, col) -> int:
        for i in range(1, 9):
            box = self.box_coord[i]
            if box[0] <= row < box[0] + 4 and box[1] <= col < box[1] + 4:
                return i


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
