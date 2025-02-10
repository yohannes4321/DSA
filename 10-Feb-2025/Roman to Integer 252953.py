# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        freq={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=0
        res=0 
        for i in range (len(s)):
            if i < len(s)-1 and freq[s[i]]<freq[s[i+1]] :
                res-=freq[s[i]]
            else:
                res+= freq[s[i]]
        return res 