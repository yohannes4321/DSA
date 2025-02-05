# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        list_t=0
        for i in range(n+1):
            list_t+=i
        for j  in nums:
            list_t-=j
        return list_t
