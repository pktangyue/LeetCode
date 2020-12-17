import unittest


class TestSolution(unittest.TestCase):

    def test_DailyTemperatures(self):
        Solution = __import__('739_DailyTemperatures').Solution
        self.assertEqual(
            [1, 1, 4, 2, 1, 1, 0, 0],
            Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
        )
