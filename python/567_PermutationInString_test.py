import unittest


class TestSolution(unittest.TestCase):

    def test_checkInclusion(self):
        Solution = __import__('567_PermutationInString').Solution
        self.assertEqual(
            True,
            Solution().checkInclusion("abb", "eidbbaooo")
        )
        self.assertEqual(
            True,
            Solution().checkInclusion("ab", "eidbaooo")
        )
        self.assertEqual(
            False,
            Solution().checkInclusion("ab", "eidboaoo")
        )
        self.assertEqual(
            False,
            Solution().checkInclusion("abb", "eidbaoo")
        )
        self.assertEqual(
            False,
            Solution().checkInclusion("hello", "ooolleoooleh")
        )
        self.assertEqual(
            True,
            Solution().checkInclusion("ab", "ab")
        )
