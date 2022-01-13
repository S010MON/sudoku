import unittest
import state
import stateFactory


class TestState(unittest.TestCase):

    def test_has_duplicate_false(self):
        L = [1, 2, 3, 4, 5, 6, 7]
        act = state.has_duplicate(L)
        self.assertFalse(act)

    def test_has_duplicate_true(self):
        L = [1, 1, 3, 4, 5, 6, 7]
        act = state.has_duplicate(L)
        self.assertTrue(act)

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
            self.assertTrue(b.check_square(i))

    def test_valid_box_true(self):
        b = stateFactory.generate_valid_state()
        for i in range(1, 9):
            self.assertTrue(b.check_square(i))

    def test_valid_box_neg(self):
        b = stateFactory.generate_invalid_box_state()
        for i in range(1, 9):
            self.assertFalse(b.check_square(i))

if __name__ == '__main__':
    unittest.main()



