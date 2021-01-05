import unittest


class TestSolution(unittest.TestCase):

    def test_maxCount(self):
        Solution = __import__('598_RangeAdditionII').Solution
        self.assertEqual(
            6,
            Solution().maxCount(
                26, 17,
                [[20, 10], [26, 11], [2, 11], [4, 16], [2, 3], [23, 13], [7, 15], [11, 11], [25, 13], [11, 13],
                 [13, 11], [13, 16], [26, 17]]
            )
        )
        self.assertEqual(
            4,
            Solution().maxCount(3, 3, [[2, 2], [3, 3]])
        )
        self.assertEqual(
            4,
            Solution().maxCount(
                3, 3,
                [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]
            )
        )
        self.assertEqual(
            9,
            Solution().maxCount(3, 3, [])
        )
