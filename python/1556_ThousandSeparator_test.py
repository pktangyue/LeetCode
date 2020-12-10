import unittest


class TestSolution(unittest.TestCase):

    def test_ThousandSeparator(self):
        Solution = __import__('1556_ThousandSeparator').Solution
        self.assertEqual(
            "987",
            Solution().thousandSeparator(987)
        )
        self.assertEqual(
            "1.234",
            Solution().thousandSeparator(1234)
        )
        self.assertEqual(
            "123.456.789",
            Solution().thousandSeparator(123456789)
        )
        self.assertEqual(
            "0",
            Solution().thousandSeparator(0)
        )
        self.assertEqual(
            "51.040",
            Solution().thousandSeparator(51040)
        )
