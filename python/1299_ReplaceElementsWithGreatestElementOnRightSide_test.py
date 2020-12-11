import unittest


class TestSolution(unittest.TestCase):

    def test_ReplaceElements(self):
        Solution = __import__('1299_ReplaceElementsWithGreatestElementOnRightSide').Solution
        self.assertEqual(
            [18, 6, 6, 6, 1, -1],
            Solution().replaceElements([17, 18, 5, 4, 6, 1])
        )
