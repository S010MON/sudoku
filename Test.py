import unittest
import state
import stateFactory


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



