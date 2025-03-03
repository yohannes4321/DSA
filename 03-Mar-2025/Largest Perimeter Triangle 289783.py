# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        curr_sum = 0
        nums.sort(reverse=True)
        i=0
        while i+2 < len(nums):
            if nums[i]<nums[i+1]+nums[i+2]:
                print(nums[i],nums[i+1],nums[i+2])
                curr_sum+=nums[i]+nums[i+1]+nums[i+2] 
                return curr_sum
            i+=1
        return 0
              