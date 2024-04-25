class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    #lets crete anoter matrix wirh zero
        res=[[0]*len(matrix) for _ in range(len(matrix[0]))] 
        # which is for every coloumn in the loop when iterates we gona create a [0] woth 
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res[c][r]=matrix[r][c]
        return res