# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            s = str(nums[i])
            for c in s:
                ans.append(int(c))
        return ans