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
        self.assertEqual(max_list_iter([1, -5, 3, 9, 0]), 9)

    def test_max_list_iter_mult_max(self):
        self.assertEqual(max_list_iter([-2, 4, 3, 4, 4]), 4)
        self.assertEqual(max_list_iter([0, 40, 3, 1, 40]), 40)
        self.assertEqual(max_list_iter([-20, 0, 0, 0, 0]), 0)
        self.assertEqual(max_list_iter([0, 0, 0, 0, 0]), 0)
        self.assertEqual(max_list_iter([-4, -84, -93, -1, -14]), -1)
        self.assertEqual(max_list_iter([-6849, 8930, -4529, -2589, 434, -19035, 234]), 8930)

    def test_reverse_rec_none(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec_empty(self):
        self.assertEqual(reverse_rec([]), [])

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([3]), [3])
        self.assertEqual(reverse_rec([1, 2]), [2, 1])
        self.assertEqual(reverse_rec([1, 1, 1]), [1, 1, 1])
        self.assertEqual(reverse_rec([1, 2, 1]), [1, 2, 1])
        self.assertEqual(reverse_rec([1, -2, -3]), [-3, -2, 1])
        self.assertEqual(reverse_rec([1, 96, -14, 890, 65, -24, -24]), [-24, -24, 65, 890, -14, 96, 1])

    def test_bin_search_none(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(3, 1, 5, tlist)

    def test_bin_search_target_empty(self):
        list_val = []
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), None)

    def test_bin_search_target_not_found(self):
        list_val = [1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(11, 0, len(list_val)-1, list_val), None)
        self.assertEqual(bin_search(0, 0, len(list_val) - 1, list_val), None)
        self.assertEqual(bin_search(-5, 0, len(list_val) - 1, list_val), None)
        self.assertEqual(bin_search(10, 0, 4, list_val), None)
        self.assertEqual(bin_search(3, 5, len(list_val) - 1, list_val), None)

    def test_bin_search_equal(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        list_val2 = [1]
        list_val3 = [1, 2]

        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(1, 0, 0, list_val2), 0)
        self.assertEqual(bin_search(2, 0, 1, list_val3), 1)

    def test_bin_search_lower(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]

        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0)

    def test_bin_search_higher(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]

        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8)

    def test_bin_search_more(self):
        list_val = [-4190, -480, -12, 3, 4, 78, 90, 1054, 6540]

        self.assertEqual(bin_search(-4190, 0, len(list_val)-1, list_val), 0)
        self.assertEqual(bin_search(-480, 0, len(list_val) - 1, list_val), 1)
        self.assertEqual(bin_search(-12, 0, len(list_val) - 1, list_val), 2)
        self.assertEqual(bin_search(3, 0, len(list_val) - 1, list_val), 3)
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        self.assertEqual(bin_search(78, 0, len(list_val) - 1, list_val), 5)
        self.assertEqual(bin_search(90, 0, len(list_val) - 1, list_val), 6)
        self.assertEqual(bin_search(1054, 0, len(list_val) - 1, list_val), 7)
        self.assertEqual(bin_search(6540, 0, len(list_val) - 1, list_val), 8)
        self.assertEqual(bin_search(78, 3, 6, list_val), 5)
        self.assertEqual(bin_search(90, 6, 8, list_val), 6)
        self.assertEqual(bin_search(-480, 0, 2, list_val), 1)


if __name__ == "__main__":
    unittest.main()
