# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue=deque()
        new = [['m' for _ in range(len(isWater[0]))] for _ in range(len(isWater))]

        

        for row in range(len(isWater))   :
            for col in range(len(isWater[0])):
                if isWater[row][col]==1:
                  
                    queue.append((row,col))
                    new[row][col]=0
                
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        def bound(row,col):
            return 0<= row< len(isWater) and 0<= col<len(isWater[0])
        # water is filled in the queue
         
  
        while queue:
            for _ in range(len(queue)):
                row,col=queue.popleft()
               
                for row_dir ,col_dir in direction:
                    new_row=row+row_dir
                    new_col=col+col_dir
                    
                    if bound(new_row,new_col) and new[new_row][new_col]=='m':
                     
                        new[new_row][new_col]=new[row][col]+1
                    
                        queue.append((new_row,new_col))
       
        return new


