import unittest


class TestSolution(unittest.TestCase):

    def test_setZeroes(self):
        Solution = __import__('73_SetMatrixZeroes').Solution
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        Solution().setZeroes(matrix)
        self.assertEqual(
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
            matrix
        )
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        Solution().setZeroes(matrix)
        self.assertEqual(
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
            matrix
        )
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        Solution().setZeroes(matrix)
        self.assertEqual(
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
            matrix
        )
