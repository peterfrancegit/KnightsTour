import unittest
from recursive_tour import *


class TestNextSquare(unittest.TestCase):
    def test_next_square_middle(self):
        self.assertEqual(set(next_square((4, 4), 8, 8)),
                         {(5, 6), (5, 2), (3, 6), (3, 2),
                          (6, 5), (6, 3), (2, 5), (2, 3)})

    def test_next_square_edge(self):
        self.assertEqual(set(next_square((0, 4), 8, 8)),
                         {(1, 6), (1, 2), (2, 5), (2, 3)})

    def test_next_square_corner(self):
        self.assertEqual(set(next_square((0, 0), 8, 8)),
                         {(1, 2), (2, 1)})

    def test_next_square_small(self):
        self.assertEqual(set(next_square((1, 1), 3, 3)),
                         set())

class TestIsTour(unittest.TestCase):
    def test_is_tour_classic(self):
        self.assertTrue(is_tour(7, 7))

if __name__ == '__main__':
    unittest.main()
