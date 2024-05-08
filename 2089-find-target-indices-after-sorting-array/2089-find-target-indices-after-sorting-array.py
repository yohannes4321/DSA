class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i  in range(len(nums)):
            for j in range(0,len(nums)):
                if j+1 < len(nums) and nums[j+1] < nums[j]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        return res