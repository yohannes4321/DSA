# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result=[]
        for i in range(0,len(nums)+1):
            
            if i not in  nums :
                result.append(i)
        return result[0]
        