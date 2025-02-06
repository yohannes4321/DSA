# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time %= 2 * (n - 1)
        return time + 1 if time <= n - 1 else n - (time - (n - 1))