class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Determine the dimensions of the matrix
        rows = len(matrix)
        if rows == 0:
            return
        cols = len(matrix[0])

        # Create a cumulative sum matrix with an extra row and column for zeros
        self.res = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Calculate the cumulative sum matrix
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self.res[i][j] = matrix[i - 1][j - 1] + self.res[i][j - 1]

        for j in range(1, cols + 1):
            for i in range(1, rows + 1):
                self.res[i][j] += self.res[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.res[row2][col2] - self.res[row1 - 1][col2] - self.res[row2][col1 - 1] + self.res[row1 - 1][col1 - 1]