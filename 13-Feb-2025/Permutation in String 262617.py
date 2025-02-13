# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1=Counter(s1)
        left=0
        right=len(s1)-1
        while right < len(s2):
            counter2=Counter(s2[left:right+1])
            print(counter2)
            print(counter1)
            if counter1 ==counter2:
                return True
            right+=1
            left+=1
        return False
             
