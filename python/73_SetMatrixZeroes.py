from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row0 = False
        col0 = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i == 0:
                        row0 = True
                    if j == 0:
                        col0 = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for j in range(1, len(matrix[0])):
            if matrix[0][j]:
                continue
            for i in range(1, len(matrix)):
                matrix[i][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0]:
                continue
            for j in range(1, len(matrix[i])):
                matrix[i][j] = 0

        if row0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if col0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
