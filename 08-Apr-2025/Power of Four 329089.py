# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        
        for i in range(16):
            if 4 ** i == n:
                return True

        return False