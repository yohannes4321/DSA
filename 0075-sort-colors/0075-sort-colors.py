class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(0,len(nums)-1):
                if j+1 <len(nums) and nums[j+1] <= nums[j]:
                    nums[j+1],nums[j]=nums[j],nums[j+1]
        return nums