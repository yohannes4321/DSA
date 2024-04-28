class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left =0
        n=len(nums)
        for right in range(0,n):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left +=1
        return nums
