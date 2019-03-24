import unittest


class TestSolution(unittest.TestCase):

    def test_RestoreIpAddresses(self):
        Solution = __import__('93_RestoreIPAddresses').Solution
        self.assertEqual(
            ["255.255.11.135", "255.255.111.35"],
            Solution().restoreIpAddresses("25525511135")
        )
        self.assertEqual(
            ["0.0.0.0"],
            Solution().restoreIpAddresses("0000")
        )
        self.assertEqual(
            ["0.10.0.10", "0.100.1.0"],
            Solution().restoreIpAddresses("010010")
        )
