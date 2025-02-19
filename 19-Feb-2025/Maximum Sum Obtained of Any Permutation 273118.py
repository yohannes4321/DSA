# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        n = len(nums)
        pf = [0] * (n+1)
        res = 0

        for start,end in requests:
            pf[start] += 1
            pf[end+1] += -1
        
        for i in range(1,n+1):
            pf[i] += pf [i-1]
        
        pf.pop()
        pf.sort()
        
        for i in range(n):
            res += nums[i]*pf[i]
        
        return res%(10**9+7)

        

        
            
        