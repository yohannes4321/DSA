# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

from collections import Counter 
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        list_t=[]
        for number in nums:
            index=abs(number)
            if nums[index-1] <0:
                list_t.append(index)
            nums[index-1] *=-1
        return list_t