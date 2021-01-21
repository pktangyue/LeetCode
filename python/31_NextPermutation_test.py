import unittest


class TestSolution(unittest.TestCase):

    def test_nextPermutation(self):
        Solution = __import__('31_NextPermutation').Solution
        num = [2, 3, 1]
        Solution().nextPermutation(num)
        self.assertEqual([3, 1, 2], num)

        num = [1, 2, 3]
        Solution().nextPermutation(num)
        self.assertEqual([1, 3, 2], num)

        num = [3, 2, 1]
        Solution().nextPermutation(num)
        self.assertEqual([1, 2, 3], num)

        num = [1, 1, 5]
        Solution().nextPermutation(num)
        self.assertEqual([1, 5, 1], num)

        num = [1]
        Solution().nextPermutation(num)
        self.assertEqual([1], num)

        num = [1, 4, 3, 2]
        Solution().nextPermutation(num)
        self.assertEqual([2, 1, 3, 4], num)
