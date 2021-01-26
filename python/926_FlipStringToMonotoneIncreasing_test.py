import unittest


class TestSolution(unittest.TestCase):

    def test_minFlipsMonoIncr(self):
        Solution = __import__('926_FlipStringToMonotoneIncreasing').Solution
        self.assertEqual(
            7,
            Solution().minFlipsMonoIncr("111011100100100")
        )
        self.assertEqual(
            5,
            Solution().minFlipsMonoIncr("10011111110010111011")
        )
        self.assertEqual(
            1,
            Solution().minFlipsMonoIncr("00110")
        )
        self.assertEqual(
            2,
            Solution().minFlipsMonoIncr("010110")
        )
        self.assertEqual(
            2,
            Solution().minFlipsMonoIncr("00011000")
        )
