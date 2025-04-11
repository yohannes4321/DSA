# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        matrices = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        max_count = 0

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            nonlocal matrices
            nonlocal grid
            matrices[row][col] = True
            area = 1  # Start with current cell
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if (inbound(new_row, new_col) and
                    not matrices[new_row][new_col] and
                    grid[new_row][new_col] == 1):
                    area += dfs(new_row, new_col)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not matrices[i][j]:
                    area = dfs(i, j)
                    max_count = max(max_count, area)

        return max_count
