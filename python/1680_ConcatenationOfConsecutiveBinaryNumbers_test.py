import unittest


class TestSolution(unittest.TestCase):

    def test_ConcatenatedBinary(self):
        Solution = __import__('1680_ConcatenationOfConsecutiveBinaryNumbers').Solution
        self.assertEqual(
            1,
            Solution().concatenatedBinary(1)
        )
        self.assertEqual(
            27,
            Solution().concatenatedBinary(3)
        )
        self.assertEqual(
            505379714,
            Solution().concatenatedBinary(12)
        )
