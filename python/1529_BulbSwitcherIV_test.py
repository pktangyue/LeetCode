import unittest


class TestSolution(unittest.TestCase):

    def test_minFlips(self):
        Solution = __import__('1529_BulbSwitcherIV').Solution
        self.assertEqual(
            3,
            Solution().minFlips("10111")
        )
        self.assertEqual(
            2,
            Solution().minFlips("10")
        )
        self.assertEqual(
            3,
            Solution().minFlips("101")
        )
        self.assertEqual(
            0,
            Solution().minFlips("00000")
        )
        self.assertEqual(
            5,
            Solution().minFlips("001011101")
        )
