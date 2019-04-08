import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")
    
    # Add more tests!
    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name, "SLO")
        self.assertAlmostEqual(loc.lat, 35.3)
        self.assertAlmostEqual(loc.lon, -120.7)

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1, loc2)

    def test_eq_different_name(self):
        loc1 = Location("LA", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(loc1, loc2)

    def test_eq_different_lat(self):
        loc1 = Location("SLO", 121.5, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(loc1, loc2)

    def test_eq_different_long(self):
        loc1 = Location("SLO", 35.3, 80.9)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(loc1, loc2)


if __name__ == "__main__":
        unittest.main()
