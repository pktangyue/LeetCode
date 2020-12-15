import unittest


class TestSolution(unittest.TestCase):

    def test_RemoveDuplicates(self):
        Solution = __import__('1047_RemoveAllAdjacentDuplicatesInString').Solution
        self.assertEqual(
            "ca",
            Solution().removeDuplicates("abbaca")
        )
