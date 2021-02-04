from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ret = [0] * len(queries)
        sumEven = sum(v for v in A if v % 2 == 0)
        for i, query in enumerate(queries):
            val = query[0]
            index = query[1]
            if A[index] % 2 == 0:
                if val % 2 == 0:
                    sumEven += val
                else:
                    sumEven -= A[index]
                A[index] += val
            else:
                A[index] += val
                if A[index] % 2 == 0:
                    sumEven += A[index]
            ret[i] = sumEven

        return ret
