# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_bottle=numBottles
        i=numBottles
        while i>=numExchange:
            result=i//numExchange
            max_bottle+=result
            i=result+ i%numExchange
        return max_bottle