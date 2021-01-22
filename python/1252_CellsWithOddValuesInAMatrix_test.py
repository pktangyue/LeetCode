import unittest


class TestSolution(unittest.TestCase):

    def test_oddCells(self):
        Solution = __import__('1252_CellsWithOddValuesInAMatrix').Solution
        self.assertEqual(
            6,
            Solution().oddCells(n=2, m=3, indices=[[0, 1], [1, 1]])
        )
        self.assertEqual(
            0,
            Solution().oddCells(n=2, m=2, indices=[[1, 1], [0, 0]])
        )
