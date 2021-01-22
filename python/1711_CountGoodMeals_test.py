import unittest


class TestSolution(unittest.TestCase):

    def test_countPairs(self):
        Solution = __import__('1711_CountGoodMeals').Solution
        self.assertEqual(
            1,
            Solution().countPairs(deliciousness=[1048576, 1048576])
        )
        self.assertEqual(
            4,
            Solution().countPairs(deliciousness=[1, 3, 5, 7, 9])
        )
        self.assertEqual(
            15,
            Solution().countPairs(deliciousness=[1, 1, 1, 3, 3, 3, 7])
        )
