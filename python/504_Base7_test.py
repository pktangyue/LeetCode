import unittest


class TestSolution(unittest.TestCase):

    def test_convertToBase7(self):
        Solution = __import__('504_Base7').Solution
        self.assertEqual(
            "-11",
            Solution().convertToBase7(-8),
        )
        self.assertEqual(
            "202",
            Solution().convertToBase7(100),
        )
        self.assertEqual(
            "-10",
            Solution().convertToBase7(-7),
        )
