# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=-1
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        queue=deque()
        fresh=0
        def bound(row,col):
            return  0<= row< len(grid) and 0<= col<len(grid[0])
       
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                value=grid[row][col]
                # print(value)
                if value==2:
                    queue.append((row,col))
                if value==1:
                    fresh+=1     
        while queue:
            for _ in range(len(queue)):
                row,col=queue.popleft()
            
                for add_row,add_right in direction:
                    new_row=row+add_row
                    new_col=col+add_right
                    if bound(new_row,new_col) and grid[new_row][new_col]==1  :
                            
                            queue.append((new_row,new_col))
                            grid[new_row][new_col]=2
                            fresh-=1
            time+=1
        
        if fresh  >0 :
            return -1
        else:
            return max(time,0)      
                
       
