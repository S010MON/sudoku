import unittest
import numpy as np

from app.dfs.depthFirstSearch import depth_first_search
from app.dfs import stateFactory, state
from app.dfs.state import State
from app.cnn.convNet import one_hot_encode, decode_output, single_best_move
from app.utilites import string_to_np_array, np_array_to_string


class TestState(unittest.TestCase):

    def test_has_duplicate_false(self):
        lst = [1, 2, 3, 4, 5, 6, 7]
        act = state.has_duplicate(lst)
        self.assertFalse(act)

    def test_has_duplicate_true(self):
        lst = [1, 1, 3, 4, 5, 6, 7]
        act = state.has_duplicate(lst)
        self.assertTrue(act)

    def test_get_missing_all(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        exp = []
        act = state.get_missing(lst)
        self.assertEqual(exp, act)

    def test_get_missing_none(self):
        lst = []
        exp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        act = state.get_missing(lst)
        self.assertEqual(exp, act)

    def test_get_missing_alternate(self):
        lst = [1, 3, 5, 7, 9]
        exp = [2, 4, 6, 8]
        act = state.get_missing(lst)
        self.assertEqual(exp, act)

    def test_valid_row_empty(self):
        b = stateFactory.generate_empty_state()
        for i in range(1, 9):
            self.assertTrue(b.check_row(i))

    def test_valid_row_true(self):
        b = stateFactory.generate_valid_state()
        for i in range(1, 9):
            self.assertTrue(b.check_row(i))

    def test_valid_row_neg(self):
        b = stateFactory.generate_invalid_row_state()
        for i in range(1, 9):
            self.assertFalse(b.check_row(i))

    def test_valid_col_empty(self):
        b = stateFactory.generate_empty_state()
        for i in range(1, 9):
            self.assertTrue(b.check_col(i))

    def test_valid_col_true(self):
        b = stateFactory.generate_valid_state()
        for i in range(1, 9):
            self.assertTrue(b.check_col(i))

    def test_valid_col_neg(self):
        b = stateFactory.generate_invalid_col_state()
        for i in range(1, 9):
            self.assertFalse(b.check_col(i))

    def test_valid_box_empty(self):
        b = stateFactory.generate_empty_state()
        for i in range(1, 9):
            self.assertTrue(b.check_box(i))

    def test_valid_box_true(self):
        b = stateFactory.generate_valid_state()
        for i in range(1, 9):
            self.assertTrue(b.check_box(i))

    def test_valid_box_neg(self):
        b = stateFactory.generate_invalid_box_state()
        for i in range(1, 9):
            self.assertFalse(b.check_box(i))

    def test_is_legal_empty(self):
        b = stateFactory.generate_empty_state()
        self.assertTrue(b.is_legal())

    def test_is_legal_complete(self):
        b = stateFactory.generate_complete_state()
        self.assertTrue(b.is_legal())

    def test_is_legal_invalid_box(self):
        b = stateFactory.generate_invalid_box_state()
        self.assertFalse(b.is_legal())

    def test_is_legal_invalid_row(self):
        b = stateFactory.generate_invalid_row_state()
        self.assertFalse(b.is_legal())

    def test_is_legal_invalid_col(self):
        b = stateFactory.generate_invalid_col_state()
        self.assertFalse(b.is_legal())

    def test_lookup_box(self):
        b = stateFactory.generate_empty_state()
        exp = 1
        act = b.look_up_box(2, 2)
        self.assertEqual(exp, act)

    def test_lookup_box_zero(self):
        b = stateFactory.generate_empty_state()
        exp = 1
        act = b.look_up_box(0, 0)
        self.assertEqual(exp, act)

    def test_copy(self):
        a = stateFactory.generate_empty_state()
        b = a.copy()
        self.assertNotEqual(a, b)

    def test_set(self):
        a = stateFactory.generate_empty_state()
        self.assertEqual(0, a.get(1, 1))
        a.set(1, 1, 1)
        self.assertEqual(1, a.get(1, 1))

    def test_decoding(self):
        a = stateFactory.generate_complete_state()
        enc = one_hot_encode(a.board)  # Encoded board
        dec = decode_output(enc)  # Decoded board
        b = State(dec)
        for i in range(len(a.board)):
            for j in range(len(a.board[0])):
                self.assertEqual(a.board[i, j], b.board[i, j])  # Compare each index

    def test_string_to_np_array(self):
        string = "000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        exp = np.zeros((9, 9))
        act = string_to_np_array(string)
        self.assertEqual(exp.shape, act.shape)

    def test_single_best_move(self):
        sudoku = stateFactory.generate_valid_state()
        print(sudoku)
        print(single_best_move(sudoku.board))


if __name__ == '__main__':
    unittest.main()
