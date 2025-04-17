# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue=deque()
        count=1
        visted=[[float('inf') for _ in range(len(mat[0]))] for _ in range(len(mat))]
        # seen=set()

        distance=[(0,1),(0,-1),(1,0),(-1,0)]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]==0:
                
                    queue.append((row,col))
                    visted[row][col]=0
                    # seen.add((row,col))
       
        def bound(row,col):
            return 0<= row<len(mat) and 0<=col<(len(mat[0]))
        while queue:
            for _ in range(len(queue)):
                row,col=queue.popleft()
               
                for next_row,next_col in distance:
                    new_row=row+next_row
                    new_col=col+next_col
                    if bound(new_row,new_col)  :     
                        if visted[row][col]+1 <  visted[new_row][new_col]:
                            visted[new_row][new_col]=visted[row][col]+1
                            queue.append((new_row,new_col))
                            # seen.add((new_row,new_col))

                   
        return visted


