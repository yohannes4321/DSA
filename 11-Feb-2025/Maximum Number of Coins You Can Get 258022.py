# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i=len(piles)//3
        sum_value=0
        for i in range(len(piles)//3,len(piles),2):
            sum_value+=piles[i]
        return sum_value
 
          