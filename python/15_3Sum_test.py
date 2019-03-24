import unittest


class TestSolution(unittest.TestCase):

    def test_ThreeSum(self):
        Solution = __import__('15_3Sum').Solution
        self.assertEqual(
            [
                [0, 0, 0]
            ],
            Solution().threeSum([0, 0, 0])
        )
        self.assertEqual(
            [
                [-1, -1, 2],
                [-1, 0, 1]
            ],
            Solution().threeSum([-1, 0, 1, 2, -1, -4])
        )
