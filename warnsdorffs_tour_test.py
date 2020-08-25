import unittest
from warnsdorffs_tour import *


class TestEdgeList(unittest.TestCase):

    def test_edge_list_small(self):
        self.assertEqual(edge_list(2, 2), [])

    def test_edge_list_length(self):
        self.assertEqual(len(edge_list(8, 8)), 336)


class TestFindNextSquares(unittest.TestCase):

    def test_find_next_squares_none(self):
        self.assertEqual(find_next_squares((0, 0), []), [])

    def test_find_next_squares_all(self):
        self.assertEqual(find_next_squares((0, 0), [((0, 0), (1, 2)),
                                                    ((0, 0), (2, 1))]),
                         [(1, 2), (2, 1)])

    def test_find_next_squares_some(self):
        self.assertEqual(find_next_squares((0, 0), [((0, 0), (1, 2)),
                                                    ((0, 0), (2, 1)),
                                                    ((1, 2), (3, 3))]),
                         [(1, 2), (2, 1)])


class TestFindDeg(unittest.TestCase):

    def test_find_deg_no_edges(self):
        self.assertEqual(find_deg((0, 0), []), 0)

    def test_find_deg_repeated_edge(self):
        self.assertEqual(find_deg((0, 0), [((0, 0), (1, 2)),
                                           ((1, 2), (0, 0))]), 1)

    def test_find_deg_lots(self):
        self.assertEqual(find_deg((0, 0), [((0, 0), (a, a)) for a in range(1000)]), 1000)


if __name__ == '__main__':
    unittest.main()
