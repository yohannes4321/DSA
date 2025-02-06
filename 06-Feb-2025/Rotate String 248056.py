# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            a=""
            a=s[i:]+s[0:i]
            print(a)
            if a == goal:
                return True 
            
        return False