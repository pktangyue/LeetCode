import unittest


class TestSolution(unittest.TestCase):

    def test_canVisitAllRooms(self):
        Solution = __import__('841_KeysAndRooms').Solution
        self.assertEqual(
            True,
            Solution().canVisitAllRooms([[1], [2], [3], []])
        )
        self.assertEqual(
            False,
            Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
        )
