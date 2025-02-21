# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    #lets crete anoter matrix wirh zero
        res=[]
        for j in range(len(matrix[0])):
            temp=[]
            for i in range(len(matrix)):
                temp.append(matrix[i][j])
            res.append(temp)
        return res