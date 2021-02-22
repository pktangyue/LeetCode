import unittest


class TestSolution(unittest.TestCase):

    def test_getWinner(self):
        Solution = __import__('1535_FindTheWinnerOfAnArrayGame').Solution
        self.assertEqual(
            5,
            Solution().getWinner(arr=[2, 1, 3, 5, 4, 6, 7], k=2)
        )
        self.assertEqual(
            3,
            Solution().getWinner(arr=[3, 2, 1], k=10)
        )
        self.assertEqual(
            9,
            Solution().getWinner(arr=[1, 9, 8, 2, 3, 7, 6, 4, 5], k=7)
        )
        self.assertEqual(
            99,
            Solution().getWinner(arr=[1, 11, 22, 33, 44, 55, 66, 77, 88, 99], k=1000000000)
        )
