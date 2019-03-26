import unittest


class TestSolution(unittest.TestCase):

    def test_Trap(self):
        Solution = __import__('42_TrappingRainWater').Solution
        self.assertEqual(
            6,
            Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        )
        self.assertEqual(
            0,
            Solution().trap([])
        )
