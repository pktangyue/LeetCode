import unittest


class TestSolution(unittest.TestCase):

    def test_NumTrees(self):
        Solution = __import__('96_UniqueBinarySearchTrees').Solution
        self.assertEqual(
            5,
            Solution().numTrees(3)
        )
