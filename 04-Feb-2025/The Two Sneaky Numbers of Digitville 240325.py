# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dict_t=Counter(nums)
        res =[]
        for key ,val in dict_t.items():
            if val>=2:
                res.append(key)
        return res