class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l=0
        right=sum(nums)
        for i in range(len(nums)):
            right-=nums[i]
            if l==right:
                return i
            l+=nums[i]
        return -1


            