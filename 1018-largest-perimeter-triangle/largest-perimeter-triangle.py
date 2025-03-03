class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i + 2 < len(nums):
            if nums[i] < nums[i+1] + nums[i+2] :
                sum_value=nums[i]+nums[i+1] + nums[i+2]
                return sum_value
            i += 1
        
        return 0
            
        


            

