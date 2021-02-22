import unittest


class TestSolution(unittest.TestCase):

    def test_evalRPN(self):
        Solution = __import__('150_EvaluateReversePolishNotation').Solution
        self.assertEqual(
            22,
            Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
        )
        self.assertEqual(
            9,
            Solution().evalRPN(["2", "1", "+", "3", "*"])
        )
        self.assertEqual(
            6,
            Solution().evalRPN(["4", "13", "5", "/", "+"])
        )
