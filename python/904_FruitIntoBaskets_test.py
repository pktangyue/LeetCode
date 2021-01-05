import unittest


class TestSolution(unittest.TestCase):

    def test_totalFruit(self):
        Solution = __import__('904_FruitIntoBaskets').Solution
        self.assertEqual(
            6,
            Solution().totalFruit([1, 0, 1, 1, 4, 1, 4, 1, 2, 3])
        )
        self.assertEqual(
            5,
            Solution().totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3])
        )
        self.assertEqual(
            1,
            Solution().totalFruit([0])
        )
        self.assertEqual(
            3,
            Solution().totalFruit([1, 2, 1])
        )
        self.assertEqual(
            3,
            Solution().totalFruit([0, 1, 2, 2])
        )
        self.assertEqual(
            4,
            Solution().totalFruit([1, 2, 3, 2, 2])
        )
        self.assertEqual(
            5,
            Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])
        )
        self.assertEqual(
            2,
            Solution().totalFruit([0, 1, 2])
        )
