class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        l=len(grid)-2
        res=[[0]*(l) for _ in range(l)]
        for i in range(l):
            for j in range(l):
                res[i][j]=max(grid[r][c] for r in range(i,i+3) for c in range(j,j+3))
        return res