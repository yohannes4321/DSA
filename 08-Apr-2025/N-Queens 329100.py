# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        cols = set()
        pos = set()
        neg = set()

        def backtrack(i):
            if i == n:
                ans.append(["".join(i) for i in board])
                return ans

            for j in range(n):
                if j in cols or (i + j) in pos or (i - j) in neg:
                    continue

                cols.add(j)
                pos.add(i + j)
                neg.add(i - j)
                board[i][j] = "Q"

                backtrack(i + 1)

                cols.remove(j)
                pos.remove(i + j)
                neg.remove(i - j)
                board[i][j] = "."
                
            return ans

        ans = []
        return backtrack(0)