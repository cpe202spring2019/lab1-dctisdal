import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_empty(self):
        self.assertEqual(max_list_iter([]), None)

    def test_max_list_iter_one_max(self):
        self.assertEqual(max_list_iter([4, 5, 3, 1, 4]), 5)

    def test_max_list_iter_mult_max(self):
        self.assertEqual(max_list_iter([4, 4, 3, 1, 4]), 4)

    def test_reverse_rec_none(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])

    def test_bin_search_none(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(3, 1, 5, tlist)

    def test_bin_search_target_not_found(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(11, 0, len(list_val)-1, list_val), None)

    def test_bin_search_equal(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

    def test_bin_search_lower(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1)

    def test_bin_search_higher(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8)


if __name__ == "__main__":
    unittest.main()
