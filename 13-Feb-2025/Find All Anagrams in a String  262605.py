# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter=Counter(p)
        n=len(p)
        left=0
        right=len(p)-1
        list_t=[]
         
        while right<len(s):
             
            counter2=Counter(s[left:right+1])
            if counter ==counter2:
                list_t.append(left)
            left+=1
            right+=1
        return list_t
