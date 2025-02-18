# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pref=0
        max_sum=float(-inf)
        for i in range(len(nums)):
            pref+=nums[i]
            max_sum=max(max_sum,pref)
            if pref <0:
                pref=0
        return max_sum