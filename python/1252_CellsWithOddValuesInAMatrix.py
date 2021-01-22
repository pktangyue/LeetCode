from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0] * n
        cols = [0] * m
        for v in indices:
            rows[v[0]] ^= 1
            cols[v[1]] ^= 1

        row_count = sum(rows)
        col_count = sum(cols)
        return row_count * m + col_count * n - 2 * row_count * col_count
