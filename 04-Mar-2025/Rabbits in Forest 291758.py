# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter 
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter=Counter()
        total_rabbit=0
        for i in answers:
            if counter[i]==0:
                total_rabbit+=i+1
                counter[i]=i
            else:
                counter[i]-=1
        return total_rabbit

        