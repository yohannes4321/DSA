# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=[[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                up=matrix[row-1][col] if row >0 else 0
                left=matrix[row][col-1] if col >0 else 0
                milltiple=matrix[row-1][col-1] if col >0 and row >0 else 0
                matrix[row][col]=up+left-milltiple+matrix[row][col]
                self.matrix[row][col]=matrix[row][col]

        print(*self.matrix, sep="\n")




    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        whole=self.matrix[row2][col2]
        left=self.matrix[row2][col1-1] if col1 >0 else 0
        up=self.matrix[row1-1][col2] if row1 >0 else 0
        digonal=self.matrix[row1-1][col1-1] if row1 >0 and col1>0 else 0
        return whole -left-up+digonal


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)