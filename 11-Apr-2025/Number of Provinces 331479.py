# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visted=set()
        count=0
        def dfs(i):
            visted.add(i)
            for other in range(len(isConnected)):
                if isConnected[i][other]==1 and other not in visted:
                    dfs(other)
        for i in range(len(isConnected)):
            if i not in visted:
                count+=1
                dfs(i)
        
        return count