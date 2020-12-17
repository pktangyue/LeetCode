import unittest


class TestSolution(unittest.TestCase):

    def test_DivisorGame(self):
        Solution = __import__('1025_DivisorGame').Solution
        self.assertEqual(
            True,
            Solution().divisorGame(2)
        )
        self.assertEqual(
            False,
            Solution().divisorGame(3)
        )
