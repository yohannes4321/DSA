# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res=[]
        c=0
        for i in nums:
            heapq.heappush(res,i)
        while len (res) >= 2 :
            if res[0]>=k:
                return c
            a=heapq.heappop(res)
            p=heapq.heappop(res)
            
            x = min(a,p)* 2 + max(a,p)
           
            heapq.heappush(res,x)
             
            c+=1
             
            if res[0]>=k:
                return c 
      
        if len(res) <2:
            if res[0] <=k:
                return c+1

