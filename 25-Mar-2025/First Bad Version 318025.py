# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=1
        right=n
        while left <= right:
            middle=(left+right)//2
            if isBadVersion(middle)== True:
                right=middle-1
            else:
                left=middle+1
        return left
