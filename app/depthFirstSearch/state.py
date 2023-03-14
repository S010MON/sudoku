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

    def set_state(self, string: str) -> None:
        i, j = 0, 0

        if len(string) != 81:
            raise Exception("String must contain 81 chars of [0, 9]")

        for char in string:

            value = int(char)
            if value < 0 or value > 9:
                raise ValueError("All values must be in the range [0, 9]")

            self.board[i][j] = value
            i = i + 1
            j = j + 1

            if j == 9:
                j = 0
            if i == 9:
                i = 0


    def is_legal(self) -> bool:
        for row in range(self.rows):
            if not self.check_row(row):
                return False

        for col in range(self.cols):
            if not self.check_col(col):
                return False

        for box in range(1, 10):
            if not self.check_box(box):
                return False
        return True

    def is_complete(self) -> bool:
        for row in range(self.rows):

            for col in range(self.cols):

                if self.board[row][col] == 0:
                    return False
        return True

    def get(self, row, col) -> int:
        return self.board[row][col]

    def set(self, row, col, value) -> None:
        self.board[row][col] = value

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

    def check_box(self, square) -> bool:
        lst = []
        sq = self.box_coord[square]
        row_start = sq[0]
        col_start = sq[1]
        for row in range(row_start, row_start + 2):
            for col in range(col_start, col_start + 2):
                if self.board[row][col] != 0:
                    lst.append(self.board[row][col])
        return not has_duplicate(lst)

    def look_up_box(self, row, col) -> int:
        for i in range(1, 10):
            box = self.box_coord[i]
            if box[0] <= row < box[0] + 4 and box[1] <= col < box[1] + 4:
                return i

    def copy(self):
        board = np.copy(self.board)
        return State(board)

    def __str__(self) -> str:
        s = ''
        for row in range(self.rows):

            if row == 3 or row == 6:
                s += '---------+---------+---------\n'

            for col in range(self.cols):
                if col == 3 or col == 6:
                    s += '|'
                if self.board[row][col] == 0:
                    s += '   '
                else:
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
