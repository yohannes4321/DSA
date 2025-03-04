# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        i=1
        count=0
        while i<=maxDoubles and target >1:
            if target% 2:
                count+=1
            target=target//2
            count+=1
            i+=1
        count+=target-1
        return count

