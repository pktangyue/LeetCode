import unittest


class TestSolution(unittest.TestCase):

    def test_matrixReshape(self):
        Solution = __import__('566_ReshapeTheMatrix').Solution
        self.assertEqual(
            [[1, 2, 3, 4]],
            Solution().matrixReshape([[1, 2], [3, 4]], 1, 4)
        )
        self.assertEqual(
            [[1, 2], [3, 4]],
            Solution().matrixReshape([[1, 2], [3, 4]], 2, 4)
        )
