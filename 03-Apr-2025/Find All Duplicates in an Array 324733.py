# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            index=abs(nums[i])-1
            if nums[index]<0:
                result.append(index+1)

            nums[index]*=-1
        return result
