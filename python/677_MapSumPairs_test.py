import unittest


class TestSolution(unittest.TestCase):

    def test_LengthOfLongestSubstring(self):
        MapSum = __import__('677_MapSumPairs').MapSum

        m = MapSum()
        m.insert("apple", 3)
        self.assertEqual(3, m.sum("ap"))
        m.insert("app", 2)
        m.insert("apple", 2)
        self.assertEqual(4, m.sum("ap"))

        m = MapSum()
        m.insert("apple", 3)
        self.assertEqual(3, m.sum("ap"))
        m.insert("app", 2)
        self.assertEqual(5, m.sum("ap"))
