import unittest


class TestSolution(unittest.TestCase):

    def test_findBestValue(self):
        Solution = __import__('1300_SumOfMutatedArrayClosestToTarget').Solution
        self.assertEqual(
            11361,
            Solution().findBestValue([60864, 25176, 27249, 21296, 20204], 56803)
        )
        self.assertEqual(
            5,
            Solution().findBestValue([2, 3, 5], 10)
        )
        self.assertEqual(
            3,
            Solution().findBestValue([4, 9, 3], 10)
        )
