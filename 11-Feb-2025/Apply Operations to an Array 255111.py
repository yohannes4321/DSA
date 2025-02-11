# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            if i <len(nums)-1:
                if nums[i]== nums[i+1]:
                    nums[i]=nums[i]*2
                    nums[i+1]=0
        for i in range(len(nums)):
            if nums[i] != 0:
                result.append(nums[i])
        result.extend([0]*(len(nums)-len(result)))
        return result 
