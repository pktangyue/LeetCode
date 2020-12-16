import unittest


class TestSolution(unittest.TestCase):

    def test_SummaryRanges(self):
        Solution = __import__('228_SummaryRanges').Solution
        self.assertEqual(
            ["0->2", "4->5", "7"],
            Solution().summaryRanges([0, 1, 2, 4, 5, 7])
        )
        self.assertEqual(
            ["0", "2->4", "6", "8->9"],
            Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]),
        )
        self.assertEqual(
            [],
            Solution().summaryRanges([])
        )
        self.assertEqual(
            ["-1"],
            Solution().summaryRanges([-1])
        )
        self.assertEqual(
            ["0"],
            Solution().summaryRanges([0])
        )
